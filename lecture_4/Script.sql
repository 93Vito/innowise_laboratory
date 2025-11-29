-- 1. Создание таблиц
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	full_name TEXT,
	birth_year INT);

CREATE TABLE grades (
	id INT PRIMARY KEY,
	student_id INT,
	subject TEXT,
	grade INT,
	FOREIGN KEY (student_id) REFERENCES students(id));
-- 2. Вставка данных
INSERT INTO students (full_name, birth_year)
VALUES
	('Alice Johnson', 2005),
	('Brian Smith', 2004),
	('Carla Reyes', 2006),
	('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
	('Felix Nguyen', 2007),
	('Grace Patel', 2005),
	('Henry Lopez', 2004),
	('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade)
VALUES
	(1, 'Math', 88),
	(1, 'English', 92),
	(1, 'Science', 85),
	(2, 'Math', 75),
	(2, 'History', 83),
	(2, 'English', 79),
	(3, 'Science', 95),
	(3, 'Math', 91),
	(3, 'Art', 89),
	(4, 'Math', 84),
	(4, 'Science', 88),
	(4, 'Physical Education', 93),
	(5, 'English', 90),
	(5, 'History', 85),
	(5, 'Math', 88),
	(6, 'Science', 72),
	(6, 'Math', 78),
	(6, 'English', 81),
	(7, 'Art', 94),
	(7, 'Science', 87),
	(7, 'Math', 90),
	(8, 'History', 77),
	(8, 'Math', 83),
	(8, 'Science', 80),
	(9, 'English', 96),
	(9, 'Math', 89),
	(9, 'Art', 92);

-- 3. Вывод оценок Alice Johnson
SELECT students.full_name, grades.grade AS grade FROM students, grades 
WHERE students.id=grades.student_id AND students.full_name='Alice Johnson';

-- 4. Вывод средней оценки каждого студента
SELECT students.full_name, ROUND(AVG(grades.grade),2) AS avg_grade FROM students
JOIN grades ON students.id=grades.student_id
GROUP BY full_name;

-- 5. Вывод студентов младше 2004 года рождения
SELECT full_name, birth_year FROM students
WHERE birth_year > 2004;

-- 6. Вывод всех предметов со средней оценкой по ним
SELECT subject, ROUND(AVG(grade),2) AS avg_subjects_grade FROM grades
GROUP BY subject;

-- 7. Вывод 3 лучших студентов по средней оценке
SELECT students.full_name, ROUND(AVG(grades.grade),2) AS avg_grade FROM students
JOIN grades ON students.id=grades.student_id
GROUP BY full_name
ORDER BY avg_grade DESC LIMIT 3;

-- 8. Вывод студентов, у которых по любому предмету оценка ниже 80
SELECT DISTINCT students.full_name FROM students
JOIN grades ON students.id=grades.student_id
WHERE grades.grade < 80;

