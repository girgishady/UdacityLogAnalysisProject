#!/usr/bin/env python3
import psycopg2

# What are the most popular three articles of all time?
def Popular_articles():
	conn = psycopg2.connect("dbname=news")
	cursor = conn.cursor()
	cursor.execute("select slug, count(slug) as num \
					from article_log \
					where status = '200 OK' \
					group by slug \
					order by num desc \
					limit 3;")
	Answer1 = cursor.fetchall()
	conn.close()
	return Answer1

# Who are the most popular article authors of all time?
def Popular_author():
	conn = psycopg2.connect("dbname=news")
	cursor = conn.cursor()
	cursor.execute("select name, count(name) as num \
					from author_log \
					where status = '200 OK' \
					group by name \
					order by num desc")
	Answer2 = cursor.fetchall()
	conn.close()
	return Answer2

# On which days did more than 1% of requests lead to errors?
def error_day():
	conn = psycopg2.connect("dbname=news")
	cursor = conn.cursor()
	cursor.execute("select t1.date, (t1.error * 100 / t2.total) as percent \
					from Errors_per_day as t1 join total_per_day as t2 \
					on t1.date = t2.date \
					where (t1.error * 100 / t2.total) > 1 \
					order by percent;")
	Answer3 = cursor.fetchall()
	conn.close()
	return Answer3
	
def printing(list):
	for i in list:
		print (i[0] , ":" , i[1])
	print ("============================================")
	return

AnswerQ1 = Popular_articles()
AnswerQ2 = Popular_author()
AnswerQ3 = error_day()
print ("the most popular three articles of all time:")
print ("--------------------------------------------")
printing(AnswerQ1)
print ("the most popular article authors of all time:")
print ("---------------------------------------------")
printing (AnswerQ2)
print ("days did more than 1% of requests lead to errors:")
print ("-------------------------------------------------")
printing (AnswerQ3)
