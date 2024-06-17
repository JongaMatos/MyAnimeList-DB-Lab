USE MyAnimeList;

select table_name as 'table', 
    table_rows as 'rows'
from information_schema.tables
where table_schema = 'MyAnimeList' -- put your database name here
    and table_type = 'BASE TABLE'
order by table_rows desc;
