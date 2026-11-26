# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
positive = []
negative = []
while True:
    number = int(input("Введіть число (0 для завершення): "))

    if number == 0:
        break
    elif number > 0:
        positive.append(number)
    else:
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)
