# Завдання 7
# Користувач вводить пароль поки не введе його правильно.
# Правильний пароль повинен:
# Бути довшим за 8 символів
# Містити хоча б одну цифру
#  Містити хоча б одну літеру
while True:
    password = input("Введіть пароль: ")

    for symbol in password:
        if symbol.isdigit():
            has_digit = True
        elif symbol.isalpha():
            has_letter = True

    if len(password) > 8 and has_digit and has_letter:
        print("Пароль прийнято")
        break
    else:
        print("Пароль не підходить")
