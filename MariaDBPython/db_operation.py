#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 13:29:17 2018

@author: n0r0082
"""
import migration_const
import database
from contextlib import closing

def get_connection(db = 'maria_local'):
    #Get database config
    db_config = database.read_db_config(migration_const.DB_CONFIG_FILE_NAME,db)
    #Get Cconnection object
    conn = database.get_connetion(db_config)
    return conn

def update_entity():
    phone = '041-237645'
    email = 'rao@gmail.com'
    conn = get_connection()
    #SQl Query prep
    sql_update_customer = "UPDATE Customer SET phone= {} where email = {}"
    email = "'{}'".format(email)
    phone = "'{}'".format(phone)
    sql_update_customer = sql_update_customer.format(phone, email)
    print(sql_update_customer)
    try:
        with closing(conn.cursor()) as cur:
           # Execute the SQL command
           cur.execute(sql_update_customer)
           conn.commit()
    except Exception as e:
            print(e)
    database.close_connetion(conn)

def delete_entity():
    phone = '041-237645'
    email = 'rao@gmail.com'
    conn = get_connection()
    #SQl Query prep
    sql_update_customer = "UPDATE Customer SET phone= {} where email = {}"
    email = "'{}'".format(email)
    phone = "'{}'".format(phone)
    sql_update_customer = sql_update_customer.format(phone, email)
    print(sql_update_customer)
    try:
        with closing(conn.cursor()) as cur:
           # Execute the SQL command
           cur.execute(sql_update_customer)
           conn.commit()
    except Exception as e:
            print(e)
    database.close_connetion(conn)


def select_entity():
    conn = get_connection()
    email = 'nikhilranjan235@gmail.com'
    #SQl Query prep
    sql_select_employee = "select * from Customer where email = {}"
    email = "'{}'".format(email)
    sql_select_employee = sql_select_employee.format(email)
    print(sql_select_employee)
    try:
        with closing(conn.cursor()) as cur:
           # Execute the SQL command
           cur.execute(sql_select_employee)
           # Fetch all the rows in a list of lists.
           results = cur.fetchall()
           if len(results) > 0:
              row = results[0]
              name = row[1]
              phone = row[2]
              print("Name: " + str(name) + " and Phone: "+ str(phone))
    except Exception as e:
            print(e)
    database.close_connetion(conn)

def insert_entity():
    conn = get_connection()
    name = 'Kumkum'
    email= 'kumkum23@devinline.com'
    phone = '8769814567'
    sql_insert_customer = "INSERT INTO Customer (NAME , EMAIL, PHONE) values ({},{},{})"
    email = "'{}'".format(email)
    name = "'{}'".format(name)
    phone = "'{}'".format(phone)
    sql_insert_customer = sql_insert_customer.format(name,email,phone)
    print(sql_insert_customer)
    try:
        with closing(conn.cursor()) as cur:
           # Execute the SQL command
           cur.execute(sql_insert_customer)
           conn.commit()
    except Exception as e:
            print(e)
    database.close_connetion(conn)

def na():
    print("Invalid choice")

switcher = {
        1: select_entity,
        2: insert_entity,
        3: update_entity
    }

def execute_db_operation(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "na")
    # Execute the function
    return func()

def db_operations():
    x = 1
    while True:
        print( "Operation (1: Select, 2: Insert, 3: Update)")
        data = input("Enter a number 1-3 : ")
        execute_db_operation(data)
        x += 1

#starts here.....
if __name__=="__main__":
    print ("************** Starting DB Operation ****************")
    db_operations()
    print ("************** Finished DB Operation ****************")
