import sqlite3 
import pandas as pd
from sqlite3 import Error

def sql_connection():
	try:
		con = sqlite3.connect('database.db')
		return con
	except Error:	
		print(Error)

def number_of_user(con):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT COUNT (userid) FROM user_table")
	usernumber = cursorObj.fetchone()[0]
	print("Number of user : ",usernumber)

def sql_fetch(con, dboy_name):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM delivery_boy where d_boy_name = "{}"'.format(dboy_name))
	rows = cursorObj.fetchone()
	print(rows) 

def user_make_order(con):
	cursorObj = con.cursor()
	print("userid - username - number of order")
	for i in range(1, 100):
		cursorObj.execute('SELECT COUNT (userid) FROM order_table where userid ="{}"'.format(i))
		rows = cursorObj.fetchone()[0]
		if rows >= 10:
			cursorObj.execute('SELECT username FROM user_table WHERE userid = "{}"'.format(i))
			name_ = cursorObj.fetchone()[0]
			print(i, " - ", name_," -",rows)

def top_ten_dboy(con):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * FROM order_table where rating_ = 5 AND delivery_time = '10' GROUP BY d_boy_id HAVING COUNT(d_boy_id) > 1 ORDER BY d_boy_id desc LIMIT 10")
	rows = cursorObj.fetchall()
	print("d_boy_nameboy_id - Name - Mobile number")
	for row in rows:
		cursorObj.execute('SELECT * FROM delivery_boy where d_boy_id = "{}"'.format(row[2]))		
		data = cursorObj.fetchone()
		print(data[0], "  -  ", data[1], " - ", data[2])


def restaurant(con):
	cursorObj = con.cursor()
	week = {'01/10/2019': '07/10/2019', '08/10/2019': '14/10/2019', '15/10/2019': '21/10/2019', '22/10/2019': '28/10/2019', '29/10/2019':'31/10/2019'}
	for i,j in week.items(): 
		cursorObj.execute("SELECT *, COUNT(userid) FROM order_table WHERE date_ BETWEEN '{}' AND '{}' GROUP BY userid HAVING COUNT(userid) > 3 ORDER BY userid".format(i, j))	
		rows = cursorObj.fetchall()
		print("\n\nNew week")
		print("User NAME", " - ", "User ID", " - ", "Number of order in a week\n ")
		for i in rows:
			cursorObj.execute('SELECT username FROM user_table WHERE userid = "{}"'.format(i[1]))		
			name_ = cursorObj.fetchone()[0]
			print(name_, " - ",i[1], " - ", i[7])	
