import json 


# Загрузка данных из файла
with open("strike.json", 'r', encoding='utf-8') as file: 
    car_data = json.load(file) 


# Счетчик использований программы
counter=0
close = True


def error(er):
    print("Возникла ошибка." + " " + er)
 

#меню программы
def menu():
    print("""
       1: Вывести все записи n
       2: Вывести запись по полю n
       3: Добавить запись n
       4: Удалить запись по полю n
       5: Выйти из программы
        """)
     



# Вывод всего
def out_all():
    global counter
    for car in car_data:
        print(f"""
        Код: {car['id']}, 
        Имя: {car['name']},                       
        Фабрика: {car['manufacturer']}, 
        Заправлена: {car['is_petrol']},    
        Объем Бака: {car['tank_volume']} 
        """)
    counter += 1



#Вывод по индексу 
def out_index():
    global counter
    idnum = int(input("Введите номер машины: "))
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
            break  
    else:
        error("Машина не найдена")

        index += 1
    counter += 1
       

#Ввод нового значения
def input_new():
    global counter  
    ids = int(input("Введите номер машины: "))
    
    exists = False
    for car in car_data:
        if car['id'] == ids:
            exists = True
            break
    
    if exists:
        error("Машина с таким номером уже существует.")
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


#Удаление по индексу
def del_id():
      global counter
      iddel = int(input("Введите номер машины: "))
      yea = False  
      for car in car_data:
        if iddel == car['id']:
            car_data.remove(car)  
            yea = True  
            break 
        if yea:
            with open("strike.json", 'w', encoding='utf-8') as output_file:
                json.dump(car_data, output_file, ensure_ascii=False, indent=2)
                print("Машина успешно удалена.")
        else:
              error("Запись не найдена.")
        counter += 1


#Выход из программы
def leave():
    global counter
    global close
    print(f"Программа завершена. Количество выполненных операций с записями равно: {counter}")
    close = False 


#Главная функция
def main():
    while close:
        menu()

        point = int(input("Введите номер действия, которое хотите выполнить: "))

        if point == 1:
            out_all()


        elif point == 2:
            out_index()


        elif point == 3:
            input_new()


        elif point == 4:
           del_id()


        elif point == 5:
            leave()
        else:
            error("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")

main()
