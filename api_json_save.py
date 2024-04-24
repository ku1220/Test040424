#!C:\Anaconda2_32bit\python.exe
# -*- coding: utf-8 -*-

"""
Ajax経由でデータを取得し，データベースへ保存
"""

import cgitb
cgitb.enable()


import cgi
import os
import sys
import json
import os

##########################################
# レスポンス
##########################################
# (おまじない)
# print "Content-type: text/javascript; charset=utf-8"
# print
print ('Content-type: text/html; charset=UTF-8')
print ("\r\n\r\n")

##########################################
# POSTからデータ取得
##########################################
#POSTデータ判定
if ( os.environ['REQUEST_METHOD'] != "POST" ):
    print (u"METHOD不正")
# # POSTのオブジェクトを取得
form = cgi.FieldStorage()
for key in form.keys():
	variable = str(key)
	value = str(form.getvalue(variable))
	# print "<p>"+ variable +", "+ value +"</p>\n" 

xml_data = json.loads(value)
print xml_data["trk"]["trkseg"]["trkpt"][0]
print xml_data["trk"]["trkseg"]["trkpt"][0]["lat"]
print xml_data["trk"]["trkseg"]["trkpt"][0]["time"]
print xml_data["trk"]["trkseg"]["trkpt"][0]["lon"]
print xml_data["trk"]["trkseg"]["trkpt"][0]["ele"]

datas = xml_data["trk"]["trkseg"]["trkpt"]


##########################################
# DBへアクセス
##########################################
import sqlite3

conn = sqlite3.connect('./db_gpx')
c = conn.cursor()

# テーブルを削除するなら
c.execute('''DROP TABLE IF EXISTS tbl_gpx ''')

# テストなので，DBを新しく作る
c.execute('''CREATE TABLE IF NOT EXISTS tbl_gpx (
	id integer primary key,
	lat,
	time,
	lon,
	ele
	)''')

for data in datas:
	lat = data["lat"]
	time = data["time"]
	lon = data["lon"]
	ele = data["ele"]
	# Ajaxで受けたデータをDBに保存
	c.execute("""INSERT INTO tbl_gpx (lat,time,lon,ele) VALUES (?,?,?,?)""", (lat,time,lon,ele))

# Save (commit) the changes
conn.commit()
# We can also close the cursor if we are done with it
c.close()
