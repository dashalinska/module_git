# Завдання 6
# Користувач вводить текст. Порахуйте скільки в ньому літер та цифр.
text = input("Введіть текст: ")

letter_count = 0
num_count = 0
for symbol in text:
    if symbol.isalpha():
        letter_count += 1
    elif symbol.isdigit():
        num_count += 1
print(f"Кількість літер: {letter_count}")
print(f"Кількість цифр: {num_count}")
