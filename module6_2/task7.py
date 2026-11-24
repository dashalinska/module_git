# Завдання 7
# Користувач вводить рядок та символ. Виведіть індекс цього символу.
text = input("Введіть текст: ")
symbol = input("Введіть символ: ")

for i in range(len(text)):
    if text[i] == symbol:
        print("Текст символу:, i ")
        break
else:
    print("Такого символу немає в рядку")
