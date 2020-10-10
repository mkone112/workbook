ДЕМОНСТРАЦИОННАЯ БД
    #8 таблиц с правдоподобными данными + 4 представления
    #авиакомпания
    #aviacompany.png на рабочем столе
    #временный срез ~ бекапу реальной сис-мы(if рейс departed=> на момент среза борт в воздухе)
    #текущая версия 15.08.2017
    СУЩНОСТИ
    #не связанные столбцы в разных таблицах|сущностях имеют разные названия(напр amount|total_amount) видимо для исключения неявных связей
    пассажир
    #не отдельная сущность
    #для простоты - все пассажиры уникальны
    карта городов - просто данные, не имеет смысла их разбирать
    очевидно что поля с использованием timezone - local
        СХЕМЫ
            bookings(не таблица)
            public
        материализованных представлений нет
        при подключении бд параметр search_path устанавливается автоматом
        представления показывает данные на языке установленном в конфигурационном параметре booking.lang(default - русский)
        ПРЕДСТАВЛЕНИЯ
            aircrafts
                     CREATE VIEW aircrafts AS
                     SELECT ml.aircraft_code,
                        (ml.model ->> lang()) AS model,
                        ml.range
                       FROM aircrafts_data ml;
            airports
                    CREATE VIEW airports AS
                     SELECT ml.airport_code,
                        (ml.airport_name ->> lang()) AS airport_name,
                        (ml.city ->> lang()) AS city,
                        ml.coordinates,
                        ml.timezone
                       FROM airports_data ml;
            flights_v
            --представление для рейсов
                CREATE VIEW flights_v AS
                 SELECT f.flight_id,
                    f.flight_no,
                    #МЕСТНОЕ ВРЕМЯ ВЫЛЕТА
                    f.scheduled_departure,
                    timezone(dep.timezone, f.scheduled_departure) AS scheduled_departure_local,
                    #МЕСТНОЕ ВРЕМЯ ПРИБЫТИЯ
                    f.scheduled_arrival,
                    #ПРОДОЛЖИТЕЛЬНОСТЬ ПОЛЕТА
                    timezone(arr.timezone, f.scheduled_arrival) AS scheduled_arrival_local,
                    (f.scheduled_arrival - f.scheduled_departure) AS scheduled_duration,
                    #РАСШИФРОВКА ДАННЫХ О АЭРОПОРТАХ
                    f.departure_airport,
                    dep.airport_name AS departure_airport_name,
                    dep.city AS departure_city,
                    f.arrival_airport,
                    arr.airport_name AS arrival_airport_name,
                    arr.city AS arrival_city,
                    f.status,
                    #3x-значный id самолета
                    f.aircraft_code,
                    f.actual_departure,
                    timezone(dep.timezone, f.actual_departure) AS actual_departure_local,
                    f.actual_arrival,
                    timezone(arr.timezone, f.actual_arrival) AS actual_arrival_local,
                    (f.actual_arrival - f.actual_departure) AS actual_duration
                   FROM flights f,
                    airports dep,
                    airports arr
                  WHERE ((f.departure_airport = dep.airport_code) AND (f.arrival_airport = arr.airport_code));
            routes
            --представление для маршрутов
                CREATE VIEW routes AS
                 WITH f3 AS (
                         SELECT f2.flight_no,
                            f2.departure_airport,
                            f2.arrival_airport,
                            f2.aircraft_code,
                            f2.duration,
                            array_agg(f2.days_of_week) AS days_of_week
                           FROM ( SELECT f1.flight_no,
                                    f1.departure_airport,
                                    f1.arrival_airport,
                                    f1.aircraft_code,
                                    f1.duration,
                                    #массив дней по которым совершаются полеты(один рейс может происходить не каждый день)
                                    f1.days_of_week
                                   FROM ( SELECT flights.flight_no,
                                            flights.departure_airport,
                                            flights.arrival_airport,
                                            flights.aircraft_code,
                                            (flights.scheduled_arrival - flights.scheduled_departure) AS duration,
                                            (to_char(flights.scheduled_departure, 'ID'::text))::integer AS days_of_week
                                           FROM flights) f1
                                  GROUP BY f1.flight_no, f1.departure_airport, f1.arrival_airport, f1.aircraft_code, f1.duration, f1.days_of_week
                                  ORDER BY f1.flight_no, f1.departure_airport, f1.arrival_airport, f1.aircraft_code, f1.duration, f1.days_of_week) f2
                          GROUP BY f2.flight_no, f2.departure_airport, f2.arrival_airport, f2.aircraft_code,
                          #плановая продолжительность рейса
                          f2.duration
                        )
                 SELECT f3.flight_no,
                    f3.departure_airport,
                    dep.airport_name AS departure_airport_name,
                    dep.city AS departure_city,
                    f3.arrival_airport,
                    arr.airport_name AS arrival_airport_name,
                    arr.city AS arrival_city,
                    f3.aircraft_code,
                    f3.duration,
                    f3.days_of_week
                   FROM f3,
                    airports dep,
                    airports arr
                  WHERE ((f3.departure_airport = dep.airport_code) AND (f3.arrival_airport = arr.airport_code));

        ТАБЛИЦЫ
        #(s) Указание что это экземпляр(строка?) сущности (не избыточен - позволяет исключить опечатки)
            aircrafts_data
            --самолет/борт
                #id
                aircraft_code character(3) NOT NULL
                #название модели
                model jsonb NOT NULL
                #дальность полета[км]
                range integer NOT NULL
                CONSTRAINT aircraft_range_check CHECK ((range > 0))
            airports_data
                CREATE TABLE airports_data (
                airport_code character(3) NOT NULL,
                airport_name jsonb NOT NULL,
                #можно исп для идентификации аэропортов в одном городе(напр для пересадок?)
                city jsonb NOT NULL,
                #долгота и широта
                coordinates point NOT NULL,
                timezone text NOT NULL
            );
            boarding_passes
            --посадочный талон
            --пассажир может зарегистрироваться только на рейс который есть в Ticket_filight(s)
            --выдача возможна за сутки до scheduled_departure(при регистрации)
            --комбинация ticket_no(seat_no)&flight_id д.б. уникальна(одно место - один пассажир)
            --pk = Ticket_flights pk
                CREATE TABLE boarding_passes (
                    ticket_no character(13) NOT NULL,
                    flight_id integer NOT NULL,
                    # присваивается в порядке регистрации пассажиров
                    # уникален в пределах рейса
                    boarding_no integer NOT NULL,
                    # место
                    # схема данных не контролирует что места в посадочных талонах соответствуют имеющимся в салоне
                    seat_no character varying(4) NOT NULL
                );
            bookings
            --бронирование/бронь(билетов)
            --основная сущность
            --одна Booking(s) может ВКЛЮЧ неск. пассажиров с отдельными Ticket(s)(билетами)
            --предпологается что ВСЕ Ticket(s)(билеты) в Booking(s)(брони) ВКЛЮЧ = набор Flight(s)(несмотря на отсутствие ограничений)
                CREATE TABLE bookings (
                    book_ref character(6) NOT NULL,                 #идентификатор
                    book_date timestamp with time zone NOT NULL,    #пассажир max за месяц делает бронь
                    total_amount numeric(10,2) NOT NULL             #общая стоимость Flight(s)(перелетов) ВСЕХ пассажиров в брони
                );

            flights
            --перелеты/рейсы
            --КАЖД Flight(s)(рейс) следует из departure_airport в arrival_airport
            --Flight(s)(рейс) с одинаковым flight_no(номером рейса) имеют одинаковые departure_airport и arrival_airport, но разные scheduled_departure
            --Flight(s)(рейсы) с пересадками отсутствуют - вместо этого при отсутствии прямого маршрута(route(s)?) в Ticket(s) включается несколько Flight(s)
            --избыточна - позволяет получить информацию о маршруте независимо от дат рейсов
                CREATE TABLE flights (
                    #первичный суррогатный ключ для обеспечения компактности внешних(Foreign) ключей
                    #ВКЛЮЧ два поля: flight_no & sheduled_departure(чтобы было проще ссылаться на строку из других таблиц)
                    flight_id integer NOT NULL,
                    flight_no character(6) NOT NULL,            #номер рейса
                    scheduled_departure timestamp with time zone NOT NULL, #плановая дата, время вылета, походу local
                    scheduled_arrival timestamp with time zone NOT NULL, #плановые дата, время прибытия, походу local
                    departure_airport character(3) NOT NULL,    #код аэропорта вылета
                    arrival_airport character(3) NOT NULL,      #код аэропорта прибытия
                    # статус Flight(s)(рейса), одно из val:
                    #     Scheduled
                    #         доступен для брони не более чем за месяц до scheduled_departure
                    #         НЕСУЩ в бд более чем за месяц до scheduled_departure
                    #     On Time
                    #         доступен для регистрации(за сутки до scheduled_departure)
                    #         не задержан
                    #     Delayed
                    #         доступен для регистрации(за сутки до scheduled_departure)
                    #         задержан
                    #     Departed
                    #         aircraft(борт) в воздухе
                    #     Arrived
                    #         aircraft(борт) прибыл в arrival_airport(пункт назначения)
                    #     Cancelled
                    #         Flight(s) отменен
                    status character varying(20) NOT NULL,
                    aircraft_code character(3) NOT NULL,
                    #может отличаться на неск часов от scheduled_departure
                    actual_departure timestamp with time zone,
                    #может отличаться на неск часов от scheduled_arrival
                    actual_arrival timestamp with time zone,
                    CONSTRAINT flights_check CHECK ((scheduled_arrival > scheduled_departure)),
                    CONSTRAINT flights_check1 CHECK (((actual_arrival IS NULL) OR ((actual_departure IS NOT NULL) AND (actual_arrival IS NOT NULL) AND (actual_arrival > actual_departure)))),
                    CONSTRAINT flights_status_check CHECK (((status)::text = ANY (ARRAY[('On Time'::character varying)::text, ('Delayed'::character varying)::text, ('Departed'::character varying)::text, ('Arrived'::character varying)::text, ('Scheduled'::character varying)::text, ('Cancelled'::character varying)::text])))
                );

            seats
            --pk seat_no&aircraft_code => одно место - один пассажир
            --определяет схему салона КАЖД модели самолета(схема мест в салоне(кол-во мест и распределение по классам))
                CREATE TABLE seats (
                    aircraft_code character(3) NOT NULL,
                    #кажд место имеет свой номер
                    #схема данных не контролирует что места в посадочных талонах соответствуют имеющимся в салоне
                    seat_no character varying(4) NOT NULL,
                    fare_conditions character varying(10) NOT NULL,
                    CONSTRAINT seats_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
                );

            ticket_flights
            --перелет
            --связывает КАЖД Ticket(s) с Flight(s) идентифицируясь их pk(номерами)
                CREATE TABLE ticket_flights (
                    ticket_no character(13) NOT NULL,
                    flight_id integer NOT NULL,
                    fare_conditions character varying(10) NOT NULL,                                 #класс
                    amount numeric(10,2) NOT NULL,                                                  #стоимость
                    CONSTRAINT ticket_flights_amount_check CHECK ((amount >= (0)::numeric)),
                    CONSTRAINT ticket_flights_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
                );

            tickets
            --билет
            --ВСЕ Ticket(s)(пассажиры) уникальны
            --КАЖД Ticket(s) ВКЛЮЧ один|неск Tickets_flight(s)
                --неск if:
                    --нет прямого рейса между пунктами(Airports|?Airports.city)
                    --билет туда-обратно
            --passager_id & passager_name != const => нельзя однозначно найти билеты одного пассажира
                CREATE TABLE tickets (
                    ticket_no character(13) NOT NULL,                  #уникален
                    book_ref character(6) NOT NULL,                    #номер брони
                    passenger_id character varying(20) NOT NULL,       #номер удостоверения личности
                    passenger_name text NOT NULL,                      #first_name&last_name
                    contact_data jsonb                                 #контакты
                );

        ПОСЛЕДОВАТЕЛЬНОСТИ
            flights_flight_id_seq
                CREATE SEQUENCE flights_flight_id_seq
                    START WITH 1
                    INCREMENT BY 1
                    NO MINVALUE
                    NO MAXVALUE
                    CACHE 1;
        FUNCTIONS
            now
                --принадлеж Bookings
                --позиция среза ПРИНАДЛЕЖ Bookings(Bookings.now)(bookings?bookings.now?(видимо в книге опечатка))
                --может использоваться now() на реальной бд
                --val fx определяет текущую версию бд(на момент среза)
    суммарный размер схемы bookings около 1.3 гб => возможно остальное в схеме public
