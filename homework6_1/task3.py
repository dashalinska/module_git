# Завдання 3
# Користувач вводить текст. Порахуйте скільки в ньому
# речень
text = input("Введіть текст: ")

count = 0
for symbol in text:
    if symbol in ".?!":
        count += 1

print(count)
