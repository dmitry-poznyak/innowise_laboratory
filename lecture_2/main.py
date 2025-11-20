name = input("Привет! Введите ваше полное имя:")
birth_year = int(input("Введите год рождения:"))
year_now = 2025

age = year_now - birth_year

#print(name, age)

def func_life_stage (age):
    if age > 0 and age <= 12:
        return "ребенок"
    elif age <= 13 and age >=19:
        return "Подросток"
    elif age >= 20:
        return "Взрослый"
    else:
        return "error age"

life_stage = func_life_stage(age)
print(f"Вы: {life_stage}\n")

