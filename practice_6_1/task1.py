# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# методом count
# з циклом for
text = input("Введіть текст: ")
target_char = input("Введіть символ: ")

count_method = text.count(target_char)
print(f'В "{text}" символ "{target_char}" зустрічається {count_method} рази')

count = 0
for symbol in text:
    if symbol == target_char:
        count += 1

print(f'В "{text}" символ "{target_char}" зустрічається {count} рази')
