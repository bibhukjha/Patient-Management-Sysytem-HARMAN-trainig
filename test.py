import sqlite3
conn = sqlite3.connect('Hospital.db')
c = conn.cursor()

sqlite_query = '''CREATE TABLE if not exists Patient_table(Patient_id INTEGER PRIMARY KEY AUTOINCREMENT ,
                         name TEXT NOT NULL,
                         Address TEXT NOT NULL,
                         Phone_no INTEGER NOT NULL )'''
c.execute(sqlite_query)
print("Executed Successfully")

selection = 0
while selection<4:
    print("1. add patient details")
    print("2. view all the patients")
    print("3. Exit")

    selection = int(input("Pick a menu option"))

    if (selection == 1):
        n = int(input("Enter no of patients"))
        for i in range(n):
            patient_id = int(input("Enter ID: "))
            name = input("Enter the name: ")
            Address = input("Enter the Address: ")
            Phone_no = int(input("Enter the phone No: "))
            insert_query = f"insert into Patient_table values({patient_id},'{name}','{Address}',{Phone_no})"
            c.execute(insert_query)
            conn.commit()



    elif (selection == 2):
        print('Data of the patient table:')
        c.execute(''' SELECT * FROM Patient_table''')
        print(c.fetchall())

    elif(selection == 3):
        exit()


    else:
        print("wrong")

conn.close()