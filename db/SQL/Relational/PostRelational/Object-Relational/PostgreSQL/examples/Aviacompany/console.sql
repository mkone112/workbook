-- по идее схема это набор связанных obj(таблиц, представлений, etc)
SELECT * FROM aircrafts;

-- Для различия now и bookings.now нужно указывать схему
SELECT bookings.now();
-- названия локализованы
SELECT airport_code, city FROM airports;

-- Для использования английских названий нужно установить параметр
-- bookings.lang на en
-- ALTER <DATABASE> SET <v> = <val>
ALTER DATABASE demo SET bookings.lang = en;
SELECT city FROM airports;
-- Настройка действует только для новых сеансов(видимо v пишется в mem
-- при подключении
ALTER DATABASE demo SET bookings.lang = ru;
SELECT city FROM airports;
-- Кто летел позавчера рейсом москва(svo) - новосибирск(ovb) на месте 1A
-- и когда он забронировал билет?
SELECT t.passenger_name,
       b.book_date
FROM   bookings b
       JOIN tickets t
         ON t.book_ref = b.book_ref
       JOIN boarding_passes bp;