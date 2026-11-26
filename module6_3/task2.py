# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len
numbers = []
while True:
    num = int(input("Введіть число: "))
    if num == -1:
        break
    else:
        numbers.append(num)

print("Кількість:", len(numbers))
print("Сума:", sum(numbers))
print("Мінімальне:", min(numbers))
print("Максимальне:", max(numbers))
print("Середнє:", sum(numbers) / len(numbers))
