# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:07:29 2023

@author: lisav
"""


#Library 
import psycopg2 as pg2

secret ='insert your postgresSQL password here'
#Connect to the database , default to the user profil name

#database named dvdrental
connexion= pg2.connect(database = 'dvdrental', user = 'postgres', password = secret)


#Connect object : curseur
cur = connexion.cursor()
#SQL QUERY : select everything from payment table e
cur.execute("SELECT * FROM film")

#Return first row, n rows, all :
#cur.fetetchone
#cur.fetchmany(10)
#cur.fetchall

#Save and index results
data = cur.fetchmany(10) #list 
data[0][4]

#Best pratice to have  a single string as one query 
#creating a new table with constraints, primary and foreign key
query1 = 'CREATE TABLE essai(\
            essai_id SERIAL PRIMARY KEY,\
            phone VARCHAR(250) NOT NULL UNIQUE,\
            email VARCHAR(250) NOT NULL,\
            title VARCHAR(250),\
            login_time TIMESTAMP NOT NULL,\
            film_id INTEGER REFERENCES film(film_id))'


#Exeting the query 
cur.execute(query1)
# commit the changes to the database
cur.commit()

#close the kernel
cur.close()
