name = input("Привет! Введите ваше полное имя:")
birth_year = int(input("Введите год рождения:"))
year_now = 2025

age = year_now - birth_year

#print(name, age)

def func_life_stage (age):
    if age > 0 and age <= 12:
        return "Ребенок"
    elif age <= 13 and age >=19:
        return "Подросток"
    elif age >= 20:
        return "Взрослый"
    else:
        return "error age"

life_stage = func_life_stage(age)
#print(f"Вы: {life_stage}\n")



hobbies = []

print("Введите ваши хобби! Напишите «stop», чтобы закончить..")

while True:
    hobby = input("Введите хоби: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

#print(hobbies)

profile = {
    "name": name,
    "birth_year": birth_year,
    "age": age,
    "life_stage": life_stage,
    "hobbies": hobbies
}

print("\nПрофиль пользователя")
print(f"Имя: {profile['name']}")
print(f"Возраст: {profile['age']}")
print(f"Жизненный этап: {profile['life_stage']}")
print(f"Хобби: {profile['hobbies']}")

if not hobbies:
    print("\nВы не указали ни одного хобби.")
else:
    print(f"\nВы ввели {len(hobbies)} хобби:")
    for i in hobbies:
        print(f"- {i}")