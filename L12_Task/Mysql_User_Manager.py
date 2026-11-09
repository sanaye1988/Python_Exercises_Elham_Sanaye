import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1',
     port = 3306,                                
     user='user_manager',
     password='admin123',
     database='users')


cursor = connection.cursor()

cursor.execute("""CREATE TABLE user_information(
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(50),
               password VARCHAR(20),
               status VARCHAR(10));""")

connection.commit()

cursor.execute("""INSERT INTO user_information(username,password,status)
                  VALUES ('elham', '24342', 'active');""")

connection.commit()


cursor.execute("SELECT * FROM user_information;")
result = cursor.fetchall()
print(result)
