#!C:\Anaconda2_32bit\python.exe
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

import cgi
import os
import sys
import json

##########################################
# DBへアクセス
##########################################
import sqlite3

conn = sqlite3.connect('./db_example')

c = conn.cursor()

# Create table
c.execute('SELECT * FROM tbl_gpx')

data = []
for row in c:
	data.append(row)
	pass
json_data = json.dumps(data)

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()


##########################################
# レスポンス
##########################################
print "Content-Type: text/javascript\n\n"
print


print json_data
