shop = {"Торт": [["Мука","Яйца","Клубника","Сгущенка"],2,2000],
"Пирожное": [["Сахар","Яйца","Сметана","Мед"],1,200],
"Маффин": [["Изюм","Мука","Яйца","Разрыхлитель"],1.50,100]}
print('Для выбора введите:1-Состав, 2-Цена, 3 - Количество, 4-Вся информация" 5-Приступить к покупке')
while True:
    a = int(input('Ваш выбор: '))
    if a == 1:
        for key,value in shop.items():
            print(key,'-',','.join(value[0]))
    if a == 2:
        for key,value in shop.items():
            print(key,f'- {value[1]}р. за 100гр.')
    if a == 3:
        for key,value in shop.items():
            print(key,f'- {value[2]} гр.')
    if a == 4:
        for key,value in shop.items():
            print(f'\n {key}', '\nСостав:', ",".join(value[0]),
            f'\nЦена: {value[1]}р. за 100гр.', f'\nКоличество: {value[2]} гр.')
    if a==5:
        cost = 0
        while True:
            choice = input('Что вы хотите купить? "Торт", "Кекс", "Пирожное" или '
            'введите n для завершения покупок')
            if choice == 'n':
                break
            gram = float(input('Сколько грамм вы хотите купить? '))
            if gram > shop[choice][2]:
                print("У нас столько нет")
                continue
            cost = cost + (gram/100 * shop[choice][1])
            shop[choice][2] -= gram
            print("Вам надо заплатить", cost )
            for key, value in shop.items():
                print(f'\n{key}', f'\nОсталось {value[2]} гр.')
            print("До свидания")