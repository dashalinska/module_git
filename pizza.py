while True:
    print("1. Вибрати піцу")
    print("2. Вихід")
    choice = input("Оберіть дію: ")

    if choice == "1":
        pizza_name = input("Введіть назву піци: ")
        pizza_amount = int(input("Введіть назву піци: "))
        print(f"Замовлено {pizza_name}, {pizza_amount} шт")
    elif choice == "2":
        print("До побачення")
        break
    else:
        print("Невірний вибір")
