CREATE DATABASE School;
USE School;

CREATE TABLE Class(ID INT PRIMARY KEY NOT NULL, Name VARCHAR(5));
CREATE TABLE Student(ID INT PRIMARY KEY NOT NULL, Number INT, Name VARCHAR(25), Surname VARCHAR(25), Birthdate DATE, RD DATE, ClassID INT, FOREIGN KEY(ClassID) REFERENCES Class(ID) ON UPDATE CASCADE ON DELETE SET NULL);
CREATE TABLE Teacher(ID INT PRIMARY KEY NOT NULL, Name VARCHAR(25), Surname VARCHAR(25), Birthdate DATE, DW DATE, Branch VARCHAR(25));
CREATE TABLE Lesson(ID INT PRIMARY KEY NOT NULL, Name VARCHAR(25));
CREATE TABLE TeacherLesson(TeacherID INT, LessonID INT, PRIMARY KEY(TeacherID, LessonID), FOREIGN KEY(TeacherID) REFERENCES Teacher(ID) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(LessonID) REFERENCES Lesson(ID) ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE TeacherClassLesson(TeacherID INT, LessonID INT, ClassID INT, PRIMARY KEY(LessonID, ClassID), FOREIGN KEY(TeacherID) REFERENCES Teacher(ID) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY(LessonID) REFERENCES Lesson(ID) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(ClassID) REFERENCES Class(ID) ON UPDATE CASCADE ON DELETE CASCADE);

INSERT INTO Class(ID,Name) VALUES (1,'11-A'), (2,'10-C'), (3,'12-E');
INSERT INTO Student(ID,Number,Name,Surname,Birthdate,RD,ClassID) VALUES (1, 112, 'ZÜHTÜ', 'ÇALIŞ', '2002-01-03', '2022-06-10', 2), (2, 113, 'ŞEYDA', 'KURTEL', '2002-04-15', '2022-06-10', 2), (3, 114, 'FUAT', 'ÖZÇAM', '2001-07-01', '2022-06-08', 1), (4, 115, 'BELGİN', 'BURHANLI', '2001-09-12', '2022-06-08', 1), (5, 116, 'NURHAN', 'SAĞLAM', '2000-02-19', '2022-06-09', 3),(6, 117, 'GÜRKAN', 'YENİDOĞAN', '2000-10-23', '2022-06-09', 3);
INSERT INTO Teacher(ID,Name,Surname,Birthdate,DW,Branch) VALUES (1, 'HALİME', 'KAPÇAK', '1990-05-04', '2019-08-01', 'Matematik'), (2, 'MELTEM', 'ALBOĞA', '1987-05-04', '2017-08-05', 'Biyoloji'), (3, 'DENİZALİ', 'AKBUDAK', '1986-03-04', '2019-04-16', 'Fizik'), (4, 'EYLÜL', 'ERTAN', '1991-03-26', '2020-07-05', 'Fizik');
INSERT INTO Lesson(ID,Name) VALUES (1,'Matematik'), (2,'Fizik'), (3,'Biyoloji'), (4,'Seçmeli Matematik');
INSERT TeacherLesson(TeacherID, LessonID) VALUES (1,1), (2,3), (3,2), (4,2), (1,4);
INSERT TeacherClassLesson(TeacherID, LessonID, ClassID) VALUES (1,1,1), (3,2,1), (2,3,1), (4,2,2), (1,4,2), (2,3,3);

