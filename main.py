import sqlite3

conn = sqlite3.connect('Hospitals.db')
c = conn.cursor()

# 1 Adding the patients details into table

c.execute("""CREATE TABLE if not exists Hospital1(
                  Patient_Code INTEGER PRIMARY KEY AUTOINCREMENT,
                  Patient_name TEXT NOT NULL,
                  Patient_address TEXT NOT NULL,
                  Patient_phone INTEGER NOT NULL UNIQUE ) """)

check = 1
while check:
    c = int(input(" Main Menu\n1) Add Patient\n2) View all Records  \n3) Exit\n"))
    if c == 1:
        n = int(input("Enter How Many Record You Want To Enter? "))
        for i in range(n):
            Patient_Code = int(input("Enter Id:"))
            Patient_name = (input("Enter Name: "))
            Patient_address = (input("Enter Address: "))
            Patient_phone = int(input("Enter Phone Number: "))
            sqlite_insert_query = f"insert into Hospital VALUES ({Patient_Code},'{Patient_name}','{Patient_address}','{Patient_phone}')"
            cur.execute(sqlite_insert_query)
            con.commit()
    elif c == 2:
            select_query = "SELECT * FROM Hospital"
            cur.execute(select_query)
            result = cur.fetchall()
            for record in result:
                print(record)
            else:
                print("terminated")
                check = 0
                print("THANK YOU")
