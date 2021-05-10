агрегирование
# конвертакия нескольких строк в одну
# обычно используются с group by
    SELECT count(*), avg(score), count(DISTINCT s_id)
    FROM exams;

select <cols>, count(cond) AS count
...
GROUP BY <список полей которые должны содержать одинаковые val для группировки>

вроде как алиасы подменяют исходное имя - нельзя использовать их вместе

Всегда используй алиасы
    многие таблицы в plural, а строки в singular
    потом все-равно понядобятся.

from generate_series(1, 10) as i; ~ for i in range