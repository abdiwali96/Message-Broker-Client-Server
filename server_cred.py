import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database='MessageBroker',
  user="root",
  password=""
)

sql_select_Query = "select * from messages"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
    # get all records
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:
        print("TopicID = ", row[0], )
        print("Topic_Name = ", row[1])
        print("Message_values = ", row[2],"\n")
      

