from app_test import *
con = sql_connection()


def switch_case(val):
	if val == 'A':
		number_of_user(con)
	elif val == 'B':
		dboy_name = input("Enter the name of Delivery Boy!")
		sql_fetch(con, dboy_name)
	elif val == 'C':
		user_make_order(con)
	elif val == 'D':
		top_ten_dboy(con)
	else:
		restaurant(con)




print("A : Number of Users")
print("B : Details of delivery a boy")
print("C : User who made orders more than 10 times in a month")
print("D : Top ten delivery boys")
print("E : user who ordered more than 3 times in a week from same restaurant")

value = input("Enter from A, B, C, D, E :  ")
switch_case(value)	