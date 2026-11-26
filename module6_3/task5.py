# Завдання 5
# Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.
# Виправіть помилку в коді
temperatures = []
days = int(input("Введіть кількість днів: "))

for i in range(days):
    temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
    temperatures.append(temperature)

print("Температури:", temperatures)

for i in range(1, days):
    difference = temperatures[i] - temperatures[i - 1]
    print(f"Різниця температур за {i + 1}-й день: {difference}")
