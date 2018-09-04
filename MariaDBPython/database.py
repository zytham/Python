# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:40:55 2018

@author: n0r0082
"""

from mysql.connector import MySQLConnection, Error
import six
import os
#To sypport pyhton 2 and 3 
try:
    from configparser import ConfigParser
except:
    import ConfigParser

def read_db_config(filename='db_config.ini', section='maria_local'):
   #Read database configuration file and return a dictionary object
    # create parser and read ini configuration file 
    if six.PY2: #pyhton 2
        parser = ConfigParser.ConfigParser()
        curr_dir_path = os.path.dirname(os.path.realpath(__file__))
        config_full_path = os.path.join(curr_dir_path, filename)
        parser.read(config_full_path)
    else: #pyhton 3
        parser = ConfigParser()
        parser.read(filename)
    
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return db

def get_connetion(db_config):
    try:
        #conn = MySQLdb.connect(host=migration_const.DB_HOST_NAME,user=migration_const.DB_USER_NAME,passwd=migration_const.DB_USER_PASSWORD)
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database ' + db_config['host'])
        return conn
    except Error as e:
        print("Exception occured while creating database connection with host" + db_config['host'] +" and port#" + db_config['port'] )
        print(e)
        #log.exception('Error from throws():')
        raise
    finally:
        pass
        #conn.close()

def close_connetion(connection):
    try:
        connection.close()
    except Exception:
        print("Error occured while closing connection!!")

