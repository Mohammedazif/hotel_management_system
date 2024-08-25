import mysql.connector

try:
    # Substitute your credentials here
    username = "root"
    password = "Login@321"

    # MySQL connection code
    init_conn = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password,

    )

    init_curs = init_conn.cursor()

    init_curs.execute('CREATE DATABASE IF NOT EXISTS hms')
    init_conn.commit()

    # Close the connection after creating the database
    init_conn.close()

    my_db = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password,
        database='hms',

    )

    my_conn = my_db.cursor()

    # Create 'room' table if not exists
    sql = "CREATE TABLE IF NOT EXISTS room (rno INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(25), price INT, vacancy VARCHAR(15))"
    my_conn.execute(sql)

    # Reset the auto-increment value for 'room' table
    sql = "ALTER TABLE room AUTO_INCREMENT=100"
    my_conn.execute(sql)

    # Create 'customer' table if not exists
    sql = "CREATE TABLE IF NOT EXISTS customer (cid INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), proof VARCHAR(25), checkin DATE, checkout DATE, room INT, cost INT, status VARCHAR(25), FOREIGN KEY(room) REFERENCES room(rno))"
    my_conn.execute(sql)

    # Reset the auto-increment value for 'customer' table
    sql = "ALTER TABLE customer AUTO_INCREMENT=1000"
    my_conn.execute(sql)

    # Commit the changes
    my_db.commit()

    print("Prerequisites completed successfully")

except mysql.connector.Error as err:
    print("Error:", err)
