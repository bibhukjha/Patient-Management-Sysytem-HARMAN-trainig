import unittest
import sqlite3

class Patients(unittest.TestCase):
    def setUp(self):
        self.connection=sqlite3.connect("Hospital.db")
        self.Patient_Code= "101"
        self.Patient_name= "Sachin"

    def tearDown(self):
        self.Patient_Code="0"
        self.Patient_name= ""
        self.connection.close()

    def test_case1(self):
        result = self.connection.execute("SELECT Patient_name FROM Hospital where Patient_Code ="+self.Patient_Code)
        for i in result:
            fetchname =i[0]
        self.assertEqual(fetchname,self.Patient_name)




if __name__=="__main__":
    unittest.main()