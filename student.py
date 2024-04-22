import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
#mycursor.execute("Create database student")
#mycursor.execute("Create table t1(id int(2) PRIMARY KEY AUTO_INCREMENT, name varchar(155), address varchar(155), phone_number int(10), E_mail varchar(155))")
sql="insert into t1(id,name,address,phone_number,E_mail)VALUES(%s,%s,%s,%s,%s)"
val=[
    ('',"Kashyap Thakuri","Simkuna","8967214791","kashyapthakuri@gmail.com"),
    ('',"Nikkon Das","Kurseong","8959473547","nikkon.dasgmail.com"),
    ('',"Faraz Asim","Kurseong","56487925857","farazasimgmail.com"),
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database ceated successfully")