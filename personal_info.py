name = input("Enter your name: ")
career = input("Enter your dream career: ")
language = input("Enter your favourite programming language: ")


def introduce_user(name, career, language):
    print("\n--- YOUR PERSONAL PROFILE ---")
    print(f"Hello, {name}!")
    print(f"Your dream career is {career}.")
    print(f"Your favourite programming language is {language}.")
    print("Keep learning and building your future!")


introduce_user(name, career, language)


with open("user_info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Dream career: {career}\n")
    file.write(f"Favourite programming language: {language}\n")

print("\nYour information has been saved successfully!")
