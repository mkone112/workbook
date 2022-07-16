/* Mozilla and Lumosity Hybrid Style */  # единообразные комменты, если что - можно легко развернуть
CREATE FUNCTION func(char, int) RETURNS record AS
$$  # на новой строке - явно отделяет сигнатуру от тела
    SELECT $1, $2;
$$ LANGUAGE plpgsql;  # указание яп на последней строке не перегружает сигнатуру

# две строки между запросами
WITH
  table_name AS (  # cte с отступами и каждое на новой строке
    SELECT  # тело с отступом в два пробела
      *,  # элементы select переносятся всегда
      b,
    FROM
      range(100)
  ),
  table_name2 AS (
    ...
  )
SELECT
  submission_date,
  experiment.key AS experiment_id,  # явный AS читабельнее, AS не выровнен, для избежания проблем с переименованием
  experiment.value AS experiment_branch,  -- inline коммент
  count(*) AS count
FROM  # формирует единую таблицу - выделим это отступом
  telemetry.clients_daily  # единственное число, описательное имя
  CROSS JOIN  # явное указание джойнов
    unnest(experiments.key_value) AS experiment  # fx - lower underscore, experiments - bad
  CROSS JOIN
    unnest(
      experiments.key_value  # аргументы 2 пробела отбивка
    ) AS experiment2
  INNER JOIN
    foreigner
    ON a < 1
    AND b > 2
WHERE
  submission_date > '2019-07-01'
  AND sample_id = '10'
GROUP BY
  submission_date,
  experiment_id,
  experiment_branch
HAVING
  boolean_value
  AND
  (
    first_name = 'Mike'
    AND
    last_name = 'Jones'
  )
  OR
  (
    was_tipping = 1
    AND
    is_still_tippin_on_four_fours = 1
    AND
    (
      is_still_wrapped_in_four_vogues = 1
      OR
      is_wood_grain_gripping = 0
    )
  );