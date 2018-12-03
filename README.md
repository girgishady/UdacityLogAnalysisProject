# Logs Analysis Project
Logs Analysis application is a pyhton application created to connect to SQL DataBase and answer some questions.

## Quickstart
To run this application:
* you should have Postgresql running in your machine.
* create the views located in SQL Views section below.
* Download **Python** from [here](https://www.python.org/downloads/release/python-2714/)
* Install **Python**
* from cli, go to the directory which the log_analysis.py file located.
* run the applicaiton by typing './log_analysis.py'

## SQL Views
### first view for matching
~~~~
create view article_log as 
select log.id, log.status, articles.slug, articles.author 
from log, articles 
where log.path LIKE '%' || articles.slug || '%';
~~~~
~~~~
create view author_log as 
select article_log.*, authors.name 
from article_log, authors 
where article_log.author = authors.id;
~~~~
~~~~
create view Errors_per_day as 
select date(time) as date, count(*) as error 
from log 
where status = '404 NOT FOUND' 
group by date 
order by date;
~~~~
~~~~
create view Total_per_day as 
select date(time) as date, count(*) as total 
from log 
group by date 
order by date;
~~~~

## Notes
for application to be run smoothly, be sure that views are correctly run in postgresql.
you can use "select * from article_log;" to check the output of view.


## License
**Logs Analysis** is a public domain work, Feel free to do whatever you want with it.