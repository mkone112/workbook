/* Mozilla and Lumosity Hybrid Style */  # единообразные комменты, если что - можно легко развернуть
WITH
  table_name AS (
    SELECT
      *,
      b,
    FROM
      range(100)
  )
SELECT
  submission_date,
  experiment.key AS experiment_id,  # явный AS читабельнее, AS не выровнен, для избежания проблем с переименованием
  experiment.value AS experiment_branch,  -- inline коммент
  count(*) AS count
FROM  # формирует единую таблицу - выделим это отступом
  telemetry.clients_daily
  CROSS JOIN  # явное указание джойнов
    UNNEST(experiments.key_value) AS experiment
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