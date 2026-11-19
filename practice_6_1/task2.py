# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# кількість символів
# чи є там слово python
# кількість шиплячих літер – szh
text = input("Введіть рядок: ")

length = len(text)
print(f"Кількість символів: {length} ")

text_lower = text.lower()
if "python" in text_lower:
    print("Слово python є в рядку")
else:
    print("Слово python немає в рядку")

szh_count = 0
for symbol in "szh":
    szh_count += 1

print(f"Кількість літер s, z, h: {szh_count}")
