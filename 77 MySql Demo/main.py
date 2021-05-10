import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="sandy_user",
    passwd="vr2h7oQdG2unuJCl",
    database="india_DB"
)
print(mydb)

mycursor = mydb.cursor()

# Fetch Dada From Database Table
mycursor.execute("select * from users")
result = mycursor.fetchall()

# Print Data From Database Table
for i in result:
    print(i)

# Insert data into table
sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = ("sandy", "My World")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
