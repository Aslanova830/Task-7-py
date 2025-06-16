import sqlite3

conn=sqlite3.connect("mydb.sqlite")
cur=conn.cursor()

# cur.execute(
#     '''
#     CREATE  TABLE IF NOT EXISTS Students(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER  
#     )'''
# )

# cur.execute(
#     '''
#     CREATE  TABLE IF NOT EXISTS Courses(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT
#     )'''
# )

# cur.execute('''
# CREATE TABLE IF NOT EXISTS Reg(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     student_id INTEGER,
#     course_id INTEGER, 
#     FOREIGN KEY(student_id) REFERENCES Students(id),
#     FOREIGN KEY(course_id) REFERENCES Courses(id)             
# )''')

# conn.commit()

# cur.execute("INSERT INTO Students(name,age) VALUES('Lale',14)")
# cur.execute("INSERT INTO Students(name,age) VALUES('Fatime',99)")
# cur.execute("INSERT INTO Students(name,age) VALUES('Mefkure',44)")

# cur.execute("INSERT INTO Courses(title) VALUES('Math')")
# cur.execute("INSERT INTO Courses(title) VALUES('Python')")
# cur.execute("INSERT INTO Courses(title) VALUES('AI')")

# cur.execute("INSERT INTO Reg(student_id,course_id) VALUES(1,2)")
# cur.execute("INSERT INTO Reg(student_id,course_id) VALUES(2,3)")
# cur.execute("INSERT INTO Reg(student_id,course_id) VALUES(3,1)")
# conn.commit()

# cur.execute(
# '''
#     SELECT r.id,s.name,c.title FROM Reg as r
#     JOIN Students as s ON r.student_id = s.id
#     JOIN Courses as c ON r.course_id = c.id
# '''
# )
# print(cur.fetchall())
# conn.commit()

def add_student(name, age):
    cur.execute(f"INSERT INTO Students(name, age) VALUES ('{name}', {age})")
    conn.commit()

def add_course(title):
    cur.execute(f"INSERT INTO Courses(title) VALUES ('{title}')")
    conn.commit()

def register_student(student_id, course_id):
    cur.execute(f"INSERT INTO Reg(student_id, course_id) VALUES ({student_id}, {course_id})")
    conn.commit()

def get_course_students(course_id):
    cur.execute(f'''
        SELECT s.name, c.title FROM Reg AS r
        JOIN Students AS s ON r.student_id = s.id
        JOIN Courses AS c ON r.course_id = c.id
        WHERE c.id = {course_id}
    ''')
    print(cur.fetchall())

def menu():
    while True:
        print(" Menu.")
        print("1.Telebe elave et.")
        print(" 2.kurs elave et.")
        print(" 3.Register")
        print("4.kurslardaki telebeler")
        print("5.Cixis")

        secim=int(input("Seciminizini daxil edin"))

        if secim ==1:
            name=input("Adinizi daxil edin")
            age=int(input('Yasinizi daxil edin'))
            add_student(name,age)

        elif secim==2:
            title=input("Kurs daxil edin")
            add_student(title)

        elif secim == 3:
            student_id=int(input("ID ni daxil et"))
            course_id=int(input("ID ni daxil et"))

            register_student(student_id, course_id)
        
        elif secim==4:
            course_id=int(input("ID ni daxil et"))
            get_course_students(course_id)
        
        elif secim==5:
            break
        else:
            print("Bele bir secim yoxdur")
    
menu()
