import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "14811481",
    database = "school"
)

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,ID,Number,Name,Surname,Birthdate,RD,ClassID):
        if ID is None:
            self.ID = 0
        else:
            self.ID = ID
        
        if len(Name) > 25:
            raise Exception("Name değeri için 25 karakter sınırı aşıldı!")

        if len(Surname) > 25:
            raise Exception("Surname değeri için 25 karakter sınırı aşıldı!")

        self.Number = Number 
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.RD = RD
        self.ClassID = ClassID

    def InsertStudent(self):
        sql = "INSERT INTO Student(ID, Number, Name, Surname, Birthdate, RD, ClassID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        value = (self.ID,self.Number,self.Name,self.Surname,self.Birthdate,self.RD,self.ClassID)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Student.connection.close()

    def UpdateStudent(self):
        sql = "UPDATE Student SET Number = %s, Name = %s, Surname = %s, Birthdate = %s, RD = %s, ClassID = %s WHERE ID = %s"
        value = (self.Number, self.Name, self.Surname, self.Birthdate, self.RD, self.ClassID, self.ID)
        Student.mycursor.execute(sql,value)

        try: 
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo(ID):
        sql = "SELECT * FROM Student WHERE ID = %s"
        value = (ID,)
        Student.mycursor.execute(sql,value)

        try: 
            obj = Student.mycursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Student.connection.close()

    @staticmethod
    def DeleteStudent(ID):
        sql = "DELETE FROM Student WHERE ID = %s"
        value = (ID,)

        Student.mycursor.execute(sql,value)

        try: 
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            Student.connection.close()

class Teacher:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,ID,Name,Surname,Birthdate,DW,Branch):
        if ID is None:
            self.ID = 0
        else:
            self.ID = ID
        
        if len(Name) > 25:
            raise Exception("Name değeri için 25 karakter sınırı aşıldı!")

        if len(Surname) > 25:
            raise Exception("Surname değeri için 25 karakter sınırı aşıldı!")

        if len(Branch) > 25:
            raise Exception("Branch değeri için 25 karakter sınırı aşıldı!")

        self.Name = Name
        self.Surname = Surname
        self.Branch = Branch
        self.Birthdate = Birthdate
        self.DW = DW

    def InsertTeacher(self):
        sql = "INSERT INTO Teacher(ID, Name, Surname, Birthdate, DW, Branch) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (self.ID,self.Number,self.Name,self.Surname,self.Birthdate,self.RD,self.ClassID)
        Teacher.mycursor.execute(sql,value)

        try:
            Teacher.connection.commit()
            print(f'{Teacher.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Teacher.connection.close()

    def UpdateTeacher(self):
        sql = "UPDATE Teacher SET Name = %s, Surname = %s, Birthdate = %s, DW = %s, Branch = %s WHERE ID = %s"
        value = (self.Name, self.Surname, self.Birthdate, self.DW, self.Branch, self.ID)
        Teacher.mycursor.execute(sql,value)

        try: 
            Teacher.connection.commit()
            print(f'{Teacher.mycursor.rowcount} tane kayıt güncellendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Teacher.connection.close()

    @staticmethod
    def TeacherInfo(ID):
        sql = "SELECT * FROM Teacher WHERE ID = %s"
        value = (ID,)
        Teacher.mycursor.execute(sql,value)

        try: 
            obj = Teacher.mycursor.fetchone()
            return Teacher(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Teacher.connection.close()

    @staticmethod
    def DeleteTeacher(ID):
        sql = "DELETE FROM Teacher WHERE ID = %s"
        value = (ID,)

        Teacher.mycursor.execute(sql,value)

        try: 
            Teacher.connection.commit()
            print(f'{Teacher.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            Teacher.connection.close()

class Class:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,ID,Name):
        if ID is None:
            self.ID = 0
        else:
            self.ID = ID
        
        if len(Name) > 5:
            raise Exception("Name değeri için 5 karakter sınırı aşıldı!")

        self.Name = Name

    def InsertClass(self):
        sql = "INSERT INTO Class(ID, Name) VALUES (%s,%s)"
        value = (self.ID,self.Name)
        Class.mycursor.execute(sql,value)

        try:
            Class.connection.commit()
            print(f'{Class.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Class.connection.close()

    def UpdateClass(self):
        sql = "UPDATE Class SET Name = %s WHERE ID = %s"
        value = (self.Name, self.ID)
        Class.mycursor.execute(sql,value)

        try: 
            Class.connection.commit()
            print(f'{Class.mycursor.rowcount} tane kayıt güncellendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Class.connection.close()

    @staticmethod
    def ClassInfo(ID):
        sql = "SELECT * FROM Class WHERE ID = %s"
        value = (ID,)
        Class.mycursor.execute(sql,value)

        try: 
            obj = Class.mycursor.fetchone()
            return Class(obj[0], obj[1])

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Class.connection.close()

    @staticmethod
    def DeleteClass(ID):
        sql = "DELETE FROM Class WHERE ID = %s"
        value = (ID,)

        Class.mycursor.execute(sql,value)

        try: 
            Class.connection.commit()
            print(f'{Class.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            Class.connection.close()

class Lesson:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,ID,Name):
        if ID is None:
            self.ID = 0
        else:
            self.ID = ID
        
        if len(Name) > 25:
            raise Exception("Name değeri için 25 karakter sınırı aşıldı!")

        self.Name = Name

    def InsertLesson(self):
        sql = "INSERT INTO Lesson(ID, Name) VALUES (%s,%s)"
        value = (self.ID,self.Name)
        Lesson.mycursor.execute(sql,value)

        try:
            Lesson.connection.commit()
            print(f'{Lesson.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Lesson.connection.close()

    def UpdateLesson(self):
        sql = "UPDATE Lesson SET Name = %s WHERE ID = %s"
        value = (self.Name, self.ID)
        Lesson.mycursor.execute(sql,value)

        try: 
            Lesson.connection.commit()
            print(f'{Lesson.mycursor.rowcount} tane kayıt güncellendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Lesson.connection.close()

    @staticmethod
    def LessonInfo(ID):
        sql = "SELECT * FROM Lesson WHERE ID = %s"
        value = (ID,)
        Teacher.mycursor.execute(sql,value)

        try: 
            obj = Lesson.mycursor.fetchone()
            return Lesson(obj[0], obj[1])

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            Lesson.connection.close()

    @staticmethod
    def DeleteLesson(ID):
        sql = "DELETE FROM Lesson WHERE ID = %s"
        value = (ID,)

        Lesson.mycursor.execute(sql,value)

        try: 
            Lesson.connection.commit()
            print(f'{Lesson.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            Lesson.connection.close()

class TeacherLesson:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,TeacherID,LessonID):
        if TeacherID is None:
            raise Exception("TeacherID değeri verilmeli!")
        else:
            self.TeacherID = TeacherID
        
        if LessonID is None:
            raise Exception("LessonID değeri verilmeli!")
        else:
            self.LessonID = LessonID


    def InsertTeacherLesson(self):
        sql = "INSERT INTO TeacherLesson(TeacherID, LessonID) VALUES (%s,%s)"
        value = (self.TeacherID, self.LessonID)
        TeacherLesson.mycursor.execute(sql,value)

        try:
            TeacherLesson.connection.commit()
            print(f'{TeacherLesson.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            TeacherLesson.connection.close()

    @staticmethod
    def DeleteTeacherLesson(TeacherID):
        sql = "DELETE FROM TeacherLesson WHERE TeacherID = %s"
        value = (TeacherID,)

        TeacherLesson.mycursor.execute(sql,value)

        try: 
            TeacherLesson.connection.commit()
            print(f'{TeacherLesson.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            TeacherLesson.connection.close()

class TeacherClassLesson:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,TeacherID,LessonID,ClassID):
        if TeacherID is None:
            raise Exception("TeacherID değeri verilmeli!")
        else:
            self.TeacherID = TeacherID
        
        if LessonID is None:
            raise Exception("LessonID değeri verilmeli!")
        else:
            self.LessonID = LessonID

        if ClassID is None:
            raise Exception("ClassID değeri verilmeli!")
        else:
            self.ClassID = ClassID

    def InsertTeacherClassLesson(self):
        sql = "INSERT INTO TeacherClassLesson(TeacherID, LessonID, ClassID) VALUES (%s,%s,%s)"
        value = (self.TeacherID, self.LessonID, self.ClassID)
        TeacherClassLesson.mycursor.execute(sql,value)

        try:
            TeacherClassLesson.connection.commit()
            print(f'{TeacherClassLesson.mycursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)

        finally:
            TeacherClassLesson.connection.close()

    @staticmethod
    def DeleteTeacherClassLesson(TeacherID):
        sql = "DELETE FROM TeacherClassLesson WHERE TeacherID = %s"
        value = (TeacherID,)

        TeacherClassLesson.mycursor.execute(sql,value)

        try: 
            TeacherClassLesson.connection.commit()
            print(f'{TeacherClassLesson.mycursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as Error:
            print("Hata oluştu: ", Error)
          
        finally:
            TeacherClassLesson.connection.close()
