#!/usr/bin/env python3
"""FSND_DMM_P1_12"""

import psycopg2


db = psycopg2.connect("dbname=news")
Cursor = db.cursor()
DBNAME = "news"

"""db connection"""
def connect_database(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)

    return c.fetchall()

# Queries part_where we retrive the data from db

q1 = """SELECT title, count(title) AS num FROM articles, log
         WHERE log.path = concat('/article/', articles.slug)
         GROUP BY title
         ORDER BY num DESC LIMIT 3;"""

q2 = """SELECT name, count(name) AS num FROM authors, articles,log
         WHERE articles.author = authors.id
         and log.path = concat('/article/', articles.slug)
         GROUP BY name
         ORDER BY num desc;"""

q3 = """ SELECT * FROM(
         select all_queries.date  ,
         (cast(error_queries.errors *100 AS float)/all_queries.all) AS ratio
         FROM (
         (SELECT DATE(time), count(status) AS errors
         FROM log WHERE status != '200 OK'
         GROUP BY DATE(time))error_queries
         FULL JOIN
         (SELECT DATE(time), count(status) AS all FROM log
         GROUP BY DATE(time)) all_queries
         on all_queries.date = error_queries.date
         )) ratio_table
         WHERE ratio_table.ratio > 1;
         """

# defining the function

# Function_for_question_1
def mostPopularArticle(query):
    answers = connect_database(query)
    print('What are the most popular three articles of all time? ')
    for answer in answers:
        print('\t"' + str(answer[0]) + '" - ' + str(answer[1]) + ' views')

# Function for question 2
def topAuthor(query):
    answers = connect_database(query)
    print('Who are the most popular article authors of all time? ')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + ' views')


# Function for question 3
def errorsreporting(query):
    answers = connect_database(query)
    print('On which days did more than 1% of requests lead to errors?')
    for answer in answers:
        print('\t' + '{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(date=answer[0],
               error_rate=answer[1]))
      

# calling the functions

mostPopularArticle(q1)

topAuthor(q2)

errorsreporting(q3)

db.close()
