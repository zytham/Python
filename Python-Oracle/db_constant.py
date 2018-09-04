#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:55:18 2018

@author: n0r0082
"""

#############
# DB CONFIG CONSTANTS
# Update DB Details below.
#############
USERNAME = ''
PASSWORD=''
DATABASE_URL = ''
PORT = ''
SERVICE_POINT = 'usmppp1_ro.gecwalmart.com'
SELECT_ADDRESS= 'select * from DBS_ADDRESS where ROWNUM>= 1 and ROWNUM <= 2'
SEELCT_VERSION = 'SELECT * FROM v$VERSION'
