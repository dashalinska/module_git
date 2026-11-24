order_details = ""
total_cost = 0

while True:
    print("Маргарита - 150 грн")
    print("Пепероні - 180 грн")
    print("Чотири сири - 200 грн")
    print("1. Вибрати піцу")
    print("2. Вихід")
    print("3. Показати все замовлення")
    choice = input("Оберіть дію: ")

    if choice == "1":
        pizza_name = input("Введіть назву піци: ")
        if pizza_name == "Маргарита":
            price = 150
        elif pizza_name == "Пепероні":
            price = 180
        elif pizza_name == "Чотири сири":
            price = 200
        else:
            print("Такої піци немає")
            continue

        quantity = int(input("Введіть кількість: "))
        cost = price * quantity
        total_cost += cost
        order_details += f"{pizza_name} - {quantity} шт, вартість: {cost} грн\n"
        print(f"Замовлено {pizza_name}, {quantity} шт")

    elif choice == "2":
        print("До побачення!")
        break

    elif choice == "3":
        print("Ваше замовлення:")
        print(order_details)
        print(f"Загальна вартість: {total_cost} грн")

    else:
        print("Невірний вибір, спробуйте ще раз.")
