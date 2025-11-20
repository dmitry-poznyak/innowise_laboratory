def generate_profile (age: int):
    if age > 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <=19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"


user_name = input("Enter your full name: ")
birth_year_str = int(input("Enter your birth year: "))

current_year = 2025
current_age = current_year - birth_year_str

hobbies = []


while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break

    hobbies.append(hobby)


life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies
}

print("\nProfile summary")
print(f"Name: {user_profile['name']}")
print(f"Current Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")


if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies {len(hobbies)}:")
    for i in hobbies:
        print(f"- {i}")