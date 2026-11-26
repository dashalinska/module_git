# Завдання 6
# Створіть застосунок банк. Є список з рахунками
# клієнтів.
accounts = []

while True:
    print("Додати клієнта - 1")
    print("Видалити клієнта -2")
    print("Поповнити рахунок - 3")
    print("Зняти кошти - 4")
    print("Вихід - 5")

    choice = int(input("Оберіть команду: "))
    if choice == 5:
        break
    elif choice == 1:
        accounts.append(0)
    elif choice in [2, 3, 4]:
        client_id = int(input("Введіть ID клієнта: "))
        if 0 <= client_id < len(accounts):
            if choice == 2:
                accounts.pop(client_id)
            elif choice == 3:
                amount = float(input("Введіть суму: "))
                accounts[client_id] += amount
            elif choice == 4:
                amount = float(input("Введіть суму: "))
                if accounts[client_id] >= amount:
                    accounts[client_id] -= amount
                else:
                    print("Недостатньо коштів")
        else:
            print("Невірний ID")

    print("Поточні рахунки:", accounts)
