#students = []  #Главный список
#stud_grade = {}  #Словарь. Помещается в список students
#stud_grade["name"] = ""  #Ключ словаря stud_grade
#stud_grade["grades"] = []  #Ключ словаря stud_grade. Является списком
students = []
def menu(students):
    print("-----Student Grade Analyzer-----")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit the program")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid data type. You must enter a number between 1 and 5.")
            continue
        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            full_report(students)
        elif choice == 4:
            best_student(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("You must enter a number between 1 and 5.")

# добавление студентов
def add_student(students):
    student_name = (input("Enter student name: ").title())
    if any(student_name==stud_grade["name"] for stud_grade in students): # проверяем, что не вводим дубликаты имён
        print(f"The Student {student_name} is already exist.")
        return students
    stud_grade={"name":student_name,"grades":[]} # создаём словарь
    students.append(stud_grade) # добавляем словарь в список


# добавление оценок
def add_grades(students):
    student_name=(input("Enter student name: ").title()) # вводим имя студента
    for stud_grade in students:
        if student_name == stud_grade["name"]: # если имя совпадает, запускаем цикл по вводу оценок
            print(f"You chose the student {student_name}.")
            while True:
                grade = input("Enter grade(or 'done' to finish): ")
                grade = grade.lower()
                if grade =='done': # стоп-слово для цикла
                    break
                try:
                    grade=int(grade)
                    if 0 <= grade <=100: # контролируем диапазон вводимых данных
                        stud_grade["grades"].append(grade)
                    else:
                        print("You must enter grade between 0 and 100.")
                except ValueError: # исключаем ввод данных другого типа
                    print("Invalid data type. You must enter grade between 0 and 100.")
            return
    print(f"The student {student_name} not found.") # если нет совпадений по имени студента


# выводим всех студентов
def full_report(students):
    average_list = [] # создаём пустой список, для того чтобы добавлять туда среднюю оценку каждого студента
    for stud_grade in students:
        try:
            average_grade =round(sum(stud_grade["grades"]) / len(stud_grade["grades"]),2)
            print(f"{stud_grade['name']}'s average grade is {average_grade}")
            average_list.append(average_grade) # добавляем среднюю оценку в список
        except ZeroDivisionError: # исключаем деление на 0
            print(f"{stud_grade['name']}'s average grade is N/A")
    min_average = round(min(average_list),2) # минимальное значение avg
    print(f"Min average: {min_average}")
    max_average = round(max(average_list),2) # максимальное значение avg
    print(f"Max average: {max_average}")
    overall_average = round(sum(average_list) / len(average_list),2) # среднее значение по средним значениям
    print(f"Overall average: {overall_average}")

# вывод лучшего студента со средним баллом
def best_student(students):
    best_list=[] # создаём новый список, для того чтобы убрать пользователей без оценок
    for stud_grade in students:
        if stud_grade["grades"] == []: # если оценок нет, выводим в принт
            print(f"Error! The Student {stud_grade['name']} has no grades.")
            continue # пропускаем этот словарь
        best_list.append(stud_grade) # добавляем студентов с оценками в новый список
    try:
        best_stud_grade = max(best_list, key=lambda stud: sum(stud["grades"]) / len(stud["grades"])) # находим словарь с максимальным avg
        high_avg = round(sum(best_stud_grade["grades"]) / len(best_stud_grade["grades"]),2)
        print(f"The student with the highest average is {best_stud_grade['name']} with a grade {high_avg}.")
    except ZeroDivisionError: # исключаем деление на 0
            print(f"Error! The Student {stud_grade['name']} has no grades.")
    return best_list

menu(students)








