import sqlite3
conn = sqlite3.connect('student_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students(studentid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,
                subject1 INTEGER,
                subject2 INTEGER,
                subject3 INTEGER,
                subject4 INTEGER,
                subject5 INTEGER,
                Totalmarks INTEGER,
                percentage REAL,
                grade TEXT)''')
name = input("enter student's name:")
subject1 = int(input("enter mark for subject1:"))
subject2 = int(input("enter mark for subject2:"))
subject3 = int(input("enter mark for subject3:"))
subject4 = int(input("enter mark for subject4:"))
subject5 = int(input("enter mark for subject5:"))
totalmarks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = totalmarks/5
if percentage>= 80:
   grade = 'A'
elif percentage>= 70:
    grade = 'B'
elif percentage>= 60:
    grade = 'C'
else:
    grade = 'E'
cursor.execute('''INSERT INTO students
              (name,subject1,subject2,subject3,subject4,subject5,totalmarks,percentage,grade)
              VALUES(?,?,?,?,?,?,?,?,?)''',
               (name,subject1,subject2,subject3,subject4,subject5,totalmarks,percentage,grade))
conn.commit()
cursor = conn.execute("select*from students")
for row in cursor:
    print(row)
conn.close()
    
