import json 

# Загрузка данных из файла
with open("strike.json", 'r', encoding='utf-8') as file: 
    car_data = json.load(file) 

# Счетчик использований программы
counter = 0 


#Зацикливание программы
while True:
    print("""
       1: Вывести все записи n
       2: Вывести запись по полю n
       3: Добавить запись n
       4: Удалить запись по полю n
       5: Выйти из программы
    """)


#Ввод нужной операции
    point = int(input("Введите номер действия, которое хотите выполнить: "))


#Вывод всех записей
    if point == 1:
        for car in car_data:
            print(f"""
            Код: {car['id']}, 
            Имя: {car['name']},                       
            Фабрика: {car['manufacturer']}, 
            Заправлена: {car['is_petrol']},    
            Объем Бака: {car['tank_volume']} 
            """)
        counter += 1


#Вывод по айди записи
    elif point == 2:
        idnum = int(input("Введите номер машины: "))
        yea = False  
        index = 0  
        for car in car_data:
            if idnum == car['id']:
                print(f"""
                Код: {car['id']}, 
                Имя: {car['name']},                       
                Фабрика: {car['manufacturer']}, 
                Заправлена: {car['is_petrol']},    
                Объем Бака: {car['tank_volume']}
                Индекс в списке: {index}
                """)
                yea = True  
                break  
            index += 1
        counter += 1
        if not yea:
            print("Запись не найдена.")


#Ввод с клавиатуры новой машины 
    elif point == 3:
        ids = int(input("Введите номер машины: "))
        
        exists = False
        for car in car_data:
            if car['id'] == ids:
                exists = True
                break
        
        if exists:
            print("Ошибка: машина с таким номером уже существует.")
        else:
            name = input("Введите имя машины: ")  
            manufacturer = input("Введите завод изготовитель: ")  
            is_petrol = input("Введите, заправлена ли машина (да/нет): ")  
            tank_volume = float(input("Введите объем бака машины: "))  

            new_car = {
                'id': ids,
                'name': name,
                'manufacturer': manufacturer,
                'is_petrol': True if is_petrol.lower() == 'да' else False, 
                'tank_volume': tank_volume
            }

            car_data.append(new_car) 
            with open("strike.json", 'w', encoding='utf-8') as output_file: 
                json.dump(car_data, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно добавлена.")
        counter += 1


#Удаление опрделенной машины
    elif point == 4:
        iddel = int(input("Введите номер машины: "))
        yea = False  

        for car in car_data:
            if iddel == car['id']:
                car_data.remove(car)  
                yea = True  
                break 

        if not yea:
            print("Запись не найдена.")
        else:
            with open("strike.json", 'w', encoding='utf-8') as output_file:
                json.dump(car_data, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно удалена.")
        counter += 1


#Выход из программы
    elif point == 5:
        print(f"Программа завершена. Количество выполненных операций с записями равно: {counter}")
        break  # Выход из цикла

#Некорректный ввод пункта
    else:
        print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")
