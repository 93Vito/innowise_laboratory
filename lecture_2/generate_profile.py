# Создаем функцию, которая определяет возрастную группу
def generate_profile(age):
    if 0 < age <= 12:
        return "Child"
    elif 13 < age <= 19:
        return "Teenager"
    else: return "Adult"

# Получаем полное имя
user_name=input("Enter your full name: ")

# Получаем год рождения пользователя
birth_year_str=input("Enter your birth year: ")
birth_year=int(birth_year_str)
current_year=2025
current_age=current_year-birth_year

# Получаем список хобби
hobbies=[]
hobby=input("Enter a favorite hobby or type 'stop' to finish: ")
while hobby!='stop':
    hobbies.append(hobby)
    hobby=input("Enter a favorite hobby or type 'stop' to finish: ")

# Создаём словарь
user_profile= {"name": user_name, "age": current_age, "stage": generate_profile(current_age), "hobbies": hobbies}

#Оформляем красивый вывод
print("-----")
print("Profile summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Stage: {user_profile['stage']}")
if user_profile["hobbies"]:
    print(f"Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f"- {hobby}")
else:
    print("You didn't mention any hobbies")
print("-----")