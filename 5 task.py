# Создаем словарь с информацией о букетах
flower_shop = {
    "Розы": ["Красные розы", 100, 50],
    "Гвоздики": ["Белые гвоздики", 80, 30],
    "Тюльпаны": ["Розовые тюльпаны", 60, 40],
    "Лилии": ["Оранжевые лилии", 120, 20]
}

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        flower_name = input("Введите название букета: ")
        if flower_name in flower_shop:
            print("Описание:", flower_shop[flower_name][0])
        else:
            print("Букет с таким названием не найден.")

    elif choice == "2":
        flower_name = input("Введите название букета: ")
        if flower_name in flower_shop:
            print("Цена:", flower_shop[flower_name][1])
        else:
            print("Букет с таким названием не найден.")

    elif choice == "3":
        flower_name = input("Введите название букета: ")
        if flower_name in flower_shop:
            print("Количество:", flower_shop[flower_name][2])
        else:
            print("Букет с таким названием не найден.")

    elif choice == "4":
        print("Информация о букетах:")
        for flower_name, flower_info in flower_shop.items():
            print(
                "Название: ", flower_name, "Описание: ", flower_info[0], "Цена: ", flower_info[1],
                "Количество: ", flower_info[2])

    elif choice == "5":
        flower_name = input("Введите название букета: ")
        if flower_name in flower_shop:
            quantity = int(input("Введите количество штук: "))
            if quantity <= flower_shop[flower_name][2]:
                total_price = quantity * flower_shop[flower_name][1]
                flower_shop[flower_name][2] -= quantity
                print("Вы купили", quantity, "штук букета", flower_name, ". Сумма покупки:", total_price)
            else:
                print("Извините, недостаточно товара в наличии.")
        else:
            print("Букет с таким названием не найден.")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите пункт меню от 1 до 6.")
