import sqlite3 # библиотека скачивание идет через vs code или pip 

# Подключение к БД при отсутствии БД она создается.
con = sqlite3.connect("school.db") # подключение к БД "school.db" или "school.sqlite3"

# совершение действий с БД
curcor = con.cursor()

# Добавление в  таблицы  БД 
# curcor.execute("CREATE TABLE pupils(fname TEXT, lname TEXT, mark INT )") # действия(кодовые слова) пишутся через caps lock
# добавление строк в БД
curcor.execute('''INSERT INTO pupils VALUES(
                                            'Дима', 
                                            'Евсеев',
                                                5)''') # INSERT добавлять VALUES значения
curcor.execute('''INSERT INTO pupils VALUES(
                                            'Андрей', 
                                            'Кунда',
                                                4)''')
curcor.execute('''INSERT INTO pupils VALUES(
                                            'Рома', 
                                            'Романов',
                                                3)''')
# изменение значений строк в БД
# curcor.execute('''UPDATE pupils SET fname='Антон' WHERE lname = "Евсеев"''')
# удаление из БД
# curcor.execute('''DELETE FROM pupils WHERE fname='Андрей' ''')

curcor.execute(''' SELECT * FROM pupils ''') # * обращение ко всей БД
# fetch - get - взять что-либо
list_of_pupils = curcor.fetchone() # вывод первого элемента
print(list_of_pupils)
list_of_pupils = curcor.fetchmany(4) # вывод нескольких элементов
print(list_of_pupils)
list_of_pupils = curcor.fetchall() # Вывод всей таблицы
print(list_of_pupils)

for i in list_of_pupils:
    print(i)

print("*" * 100)

print(*list_of_pupils, sep="\n")

print("*" * 100)

name = list_of_pupils[0][0], list_of_pupils[0][1], list_of_pupils[0][2]

print(name)

con.commit() # обновление БД