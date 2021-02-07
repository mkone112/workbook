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


-- 10 самых задержавшихся рейсов
SELECT f.flight_no, (f.actual_departure - f.scheduled_departure)::time AS delay
  FROM flights f
 WHERE f.actual_departure IS NOT NULL
 ORDER BY delay DESC
 LIMIT 5;

CREATE FUNCTION abs(interval) RETURNS interval AS
$$
SELECT CASE WHEN ($1 < INTERVAL '0') THEN -$1 ELSE $1 END;
$$
  LANGUAGE sql IMMUTABLE;
