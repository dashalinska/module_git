# Завдання 4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати
salaries = []

while True:
    num = float(input("Введіть зарплату: "))
    if num == -1:
        break
    else:
        salaries.append(num)

percent = float(input("Введіть відсоток: "))
for i in range(len(salaries)):
    salaries[i] = salaries[i] + salaries[i] * percent / 100

print(salaries)
