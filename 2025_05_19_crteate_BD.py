<<<<<<< HEAD
import sqlite3 
import datetime
import os
db_path='C:\\Users\\admin\\test_01.db'
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE active_energy_registers (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL, serial_number INT, sum_import_active_energy FLOAT, total_import_active_energy FLOAT)''')  #створти базу
#conn.commit() 
#curs.close() 
#conn.close()
#now=str(datetime.datetime.now())
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('INSERT INTO active_energy_registers (data, serial_number, sum_import_active_energy,total_import_active_energy) VALUES (?, ?, ?, ?)',  #записати даннів базу
#             (now, 202498000601, 7.85, 7.85)) #записати даннів базу
#conn.commit() 
#curs.close()
#conn.close()
#вивести таблицю поточні значень
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('SELECT * FROM active_energy_registers')
#for row in curs:
#    print(row)
#conn.commit()
#rows = curs.fetchall()
#print(rows)
#conn = sqlite3.connect(db_path) #вивести таблицю профіль 1
#curs = conn.cursor()
#curs.execute('SELECT * FROM profile_1') 
#for row in curs:
#    print(row)
#conn.commit()
#rows = curs.fetchall()
#print(rows)
#curs.close()
#conn.close()
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE profile_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, data_rec TEXT NOT NULL, serial_number INT, data_info TEXT NOT NULL, time_info TEXT NOT NULL, bias INT, all_import_active_energy FLOAT, all_export_active_energy FLOAT,all_import_reactive_energy FLOAT, all_export_reactive_energy FLOAT)''')  #створти базу
#conn.commit() 
#curs.close() 
#conn.close()
#now=str(datetime.datetime.now())
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('INSERT INTO active_energy_registers (data, serial_number, sum_import_active_energy,total_import_active_energy) VALUES (?, ?, ?, ?)',  #записати даннів базу
#             (now, 202498000601, 7.85, 7.85)) #записати даннів базу
#conn.commit()
#curs.close()

#PRAGMA table_info(profile_1) #перегляд структури таблиці, чомусь не працює ...
#SELECT sql FROM sqlite_master WHERE type='table' AND name='profile_1'
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
##curs.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='profile_1'")# Виконуємо запит для отримання структури таблиці
#table_info = curs.fetchall()# Отримуємо та виводимо результат
#for row in table_info:
#    print(row)
#curs.close()   
#conn.close()
# Виконання запиту щодо останнього запису по лічильніку в БД
#number_metr = 202498000621 # Визначення serial_number, для якого потрібно отримати дані
#curs.execute('''                                        
#    SELECT data_info, time_info, data_rec, id
#    FROM profile_1
#    WHERE serial_number = ?
#    ORDER BY data_info DESC, time_info DESC, id DESC
#    LIMIT 1;
#''', (number_metr,))
#result = curs.fetchone()# Отримання результату
#if result:      # Перевірка, чи є результат
#    data_info, time_info, data_rec, record_id = result
#    print(f"Last line for  serial_number {number_metr}:")
#    print(f"Day: {data_info}")
#    print(f"Hour: {time_info}")
#    print(f"Time record: {data_rec}")
#    print(f"ID : {record_id}")
#else:
#    print(f"Data for serial_number {number_metr} no data.")
#    from datetime import datetime 
#    data_info=(f"{datetime.now().year}:{datetime.now().month}:01")#перетворюємо формат дату у строку
#    time_info="00:00:00"
#    print(f'Date start {data_info} hour start {time_info}')
#curs.close()
#conn.close()
#conn.commit() 
#створти базу для 
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE profile_1_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, data_rec TEXT NOT NULL, serial_number INT, data_info TEXT NOT NULL, time_info TEXT NOT NULL, bias INT,status INT, all_import_active_energy FLOAT, all_export_active_energy FLOAT,all_import_reactive_energy FLOAT, all_export_reactive_energy FLOAT, relevant INT)''')  
#curs.close() 
#conn.close()

#conn = sqlite3.connect(db_path)#перегляд структури таблиці
#curs = conn.cursor()
#curs.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='profile_1_2'")# Виконуємо запит для отримання структури таблиці
#table_info = curs.fetchall()# Отримуємо та виводимо результат
#for row in table_info:
#    print(row)
#curs.close() 
#conn.close()
# 
# 
# curs.execute('DELETE FROM  profile_1_2') видалити данні з БД d всі або якісь - ('DELETE FROM  profile_1_2 WHERE serial_number = "126456354"')

conn = sqlite3.connect(db_path) #вивести таблицю по лічильнику профіль 1_2
curs = conn.cursor()
curs.execute ('''
    SELECT *  
    FROM profile_1_2
    WHERE serial_number ="202498000599"
    ORDER BY data_info DESC, time_info DESC, id DESC
    LIMIT 24''') 
for row in curs:
    print(row)
result = curs.fetchone()
print(result)
curs.close()
conn.close()
#перетворти на integer 8 для скалеру
#num=0xFE
#num_integer8=num - 256 if num >127 else num
=======
import sqlite3 
import datetime
import os
db_path='C:\\Users\\admin\\test_01.db'
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE active_energy_registers (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL, serial_number INT, sum_import_active_energy FLOAT, total_import_active_energy FLOAT)''')  #створти базу
#conn.commit() 
#curs.close() 
#conn.close()
#now=str(datetime.datetime.now())
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('INSERT INTO active_energy_registers (data, serial_number, sum_import_active_energy,total_import_active_energy) VALUES (?, ?, ?, ?)',  #записати даннів базу
#             (now, 202498000601, 7.85, 7.85)) #записати даннів базу
#conn.commit() 
#curs.close()
#conn.close()
#вивести таблицю поточні значень
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('SELECT * FROM active_energy_registers')
#for row in curs:
#    print(row)
#conn.commit()
#rows = curs.fetchall()
#print(rows)
#conn = sqlite3.connect(db_path) #вивести таблицю профіль 1
#curs = conn.cursor()
#curs.execute('SELECT * FROM profile_1') 
#for row in curs:
#    print(row)
#conn.commit()
#rows = curs.fetchall()
#print(rows)
#curs.close()
#conn.close()
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE profile_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, data_rec TEXT NOT NULL, serial_number INT, data_info TEXT NOT NULL, time_info TEXT NOT NULL, bias INT, all_import_active_energy FLOAT, all_export_active_energy FLOAT,all_import_reactive_energy FLOAT, all_export_reactive_energy FLOAT)''')  #створти базу
#conn.commit() 
#curs.close() 
#conn.close()
#now=str(datetime.datetime.now())
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
#curs.execute('INSERT INTO active_energy_registers (data, serial_number, sum_import_active_energy,total_import_active_energy) VALUES (?, ?, ?, ?)',  #записати даннів базу
#             (now, 202498000601, 7.85, 7.85)) #записати даннів базу
#conn.commit()
#curs.close()

#PRAGMA table_info(profile_1) #перегляд структури таблиці, чомусь не працює ...
#SELECT sql FROM sqlite_master WHERE type='table' AND name='profile_1'
#conn = sqlite3.connect(db_path)
#curs = conn.cursor()
##curs.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='profile_1'")# Виконуємо запит для отримання структури таблиці
#table_info = curs.fetchall()# Отримуємо та виводимо результат
#for row in table_info:
#    print(row)
#curs.close()   
#conn.close()
# Виконання запиту щодо останнього запису по лічильніку в БД
#number_metr = 202498000621 # Визначення serial_number, для якого потрібно отримати дані
#curs.execute('''                                        
#    SELECT data_info, time_info, data_rec, id
#    FROM profile_1
#    WHERE serial_number = ?
#    ORDER BY data_info DESC, time_info DESC, id DESC
#    LIMIT 1;
#''', (number_metr,))
#result = curs.fetchone()# Отримання результату
#if result:      # Перевірка, чи є результат
#    data_info, time_info, data_rec, record_id = result
#    print(f"Last line for  serial_number {number_metr}:")
#    print(f"Day: {data_info}")
#    print(f"Hour: {time_info}")
#    print(f"Time record: {data_rec}")
#    print(f"ID : {record_id}")
#else:
#    print(f"Data for serial_number {number_metr} no data.")
#    from datetime import datetime 
#    data_info=(f"{datetime.now().year}:{datetime.now().month}:01")#перетворюємо формат дату у строку
#    time_info="00:00:00"
#    print(f'Date start {data_info} hour start {time_info}')
#curs.close()
#conn.close()
#conn.commit() 
#створти базу для 
#conn = sqlite3.connect (db_path)
#curs = conn.cursor() 
#curs.execute('''CREATE TABLE profile_1_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, data_rec TEXT NOT NULL, serial_number INT, data_info TEXT NOT NULL, time_info TEXT NOT NULL, bias INT,status INT, all_import_active_energy FLOAT, all_export_active_energy FLOAT,all_import_reactive_energy FLOAT, all_export_reactive_energy FLOAT, relevant INT)''')  
#curs.close() 
#conn.close()

#conn = sqlite3.connect(db_path)#перегляд структури таблиці
#curs = conn.cursor()
#curs.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='profile_1_2'")# Виконуємо запит для отримання структури таблиці
#table_info = curs.fetchall()# Отримуємо та виводимо результат
#for row in table_info:
#    print(row)
#curs.close() 
#conn.close()
# 
# 
# curs.execute('DELETE FROM  profile_1_2') видалити данні з БД d всі або якісь - ('DELETE FROM  profile_1_2 WHERE serial_number = "126456354"')

conn = sqlite3.connect(db_path) #вивести таблицю по лічильнику профіль 1_2
curs = conn.cursor()
curs.execute ('''
    SELECT *  
    FROM profile_1_2
    WHERE serial_number ="202498000599"
    ORDER BY data_info DESC, time_info DESC, id DESC
    LIMIT 24''') 
for row in curs:
    print(row)
result = curs.fetchone()
print(result)
curs.close()
conn.close()
#перетворти на integer 8 для скалеру
#num=0xFE
#num_integer8=num - 256 if num >127 else num
>>>>>>> fcd6d8ef3d668693cd84ec40c85e0b407b0aa5f5
#print (num)