
### Reqiurements  :
  ### Install: 
   ### python - 3.7 or 3.8
   ### python(packages)-sqlite3, pandas


<p><b>Run file</b> - app4.py</p>
		

<h2>Sql queries - </h2>

1. Write a SQL query to find the number of Zomato users.
    SELECT COUNT (userid) FROM user_table

2. Write a SQL query to find details of Zomato delvery Boy.    		SELECT * FROM delivery_boy where d_boy_name = "{}"'.format(dboy_name)

3. Write a SQL query to find the list of Zomato users who made more than 10 orders in a particular month.
    A: SELECT COUNT (userid) FROM order_table where userid ="{}"'.format(i)

    B: SELECT username FROM user_table WHERE userid = "{}"'.format(i)

4. Write a SQL query to find top 10 Zomato delivery Boy on basis of customer rating and time to deliver the item.
   A: SELECT * FROM order_table where rating_ = 5 AND delivery_time = '10' GROUP BY d_boy_id HAVING COUNT(d_boy_id) > 1 ORDER BY d_boy_id desc LIMIT 10    

   B:  SELECT * FROM delivery_boy where d_boy_id = "{}"'.format(row[2])

5. Write a SQL query to find the list of Zomato users who order food from the same restaurants more than 3 times in a week.
   A:  SELECT *, COUNT(userid) FROM order_table WHERE date_ BETWEEN '{}' AND '{}' GROUP BY userid HAVING COUNT(userid) > 3 ORDER BY userid".format(i, j)

   B:  SELECT username FROM user_table WHERE userid = "{}"'.format(i[1])   
