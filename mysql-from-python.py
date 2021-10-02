import os
import pymysql
#Get username from workspace

#(modify this var if running on another env)
username = os.getenv('C9_USER')


#connect to db
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
try:
    #run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result   = cursor.fetchall()
        print(result)
finally:
    #close connection 
    connection.close()