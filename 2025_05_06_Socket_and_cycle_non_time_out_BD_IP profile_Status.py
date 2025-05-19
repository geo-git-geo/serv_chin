#https://www.youtube.com/watch?v=f5ic6D30_mQ
import socket
import datetime
import sqlite3
import time



try: # ця обробка для можливості зупинки програми через клавітуру
    #створення серверного сокету
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #server.settimeout(5)  # Таймаут для всіх операцій 
    #створитт сокет сервера (без цієї строки з адресу був би сокет кліенту)
    p=4062 #номер порту
    server.bind(('0.0.0.0',p))
    #варіант 2 по замовчуванню працює з (socket.AF_INET,socket.SOCK_STREAM)
    #server=socket.create_server(('127.0.0.1',4061))
    #команда на прослуховування у дужках кільківсть вхідних запитів які будуть прослуховуватися сисстемою та поставлені в режим очикування    

    server.listen(5)
    while True: 
             #дату та час для виведення у повідомлення 
            now = datetime.datetime.now()
            print(now,'start listening port', p ,', please wait connect...')
            #accept для прийнятт запитів та розділяти іх на кліента та  адресу з якоі прийшов запит
            client_socket, adress=server.accept()
            #із обєкту кліента отримуємо зміст запиту recv(1024) - розмір пакету у байтах, та декодувати
            #data=client_socket.recv(1024).decode('utf-8')3
            now = datetime.datetime.now()
            print(f'{now} ping')
            try:
                client_socket.settimeout(5)# Обмежуємо час очікування даних після підключення  
                data=client_socket.recv(1024)
                now = datetime.datetime.now()
                print(now,data)
            except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                now = datetime.datetime.now()
                print(f'{now}\t {e}\t meter is offline 0')
                #client_socket.shutdown(socket.SHUT_WR)
                continue #починаємо цикл зпочатку
            index=data.find(b'\x0c')
            hex_bytes=data[index+1:index+13]
            try:
                number_metr=int(hex_bytes)
            except  ValueError as e:
                now = datetime.datetime.now()
                print(now, "error number Value",e,"comand shutdown")
                try:
                    client_socket.shutdown(socket.SHUT_WR)
                except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                    now = datetime.datetime.now()
                    print(f'{now}\t {e}')
                now = datetime.datetime.now()
                print(f'{now}\t meter is offline')
                continue #починаємо цикл зпочатку
            now = datetime.datetime.now()
            print(f"{now} number metr : {number_metr}")
            #створюємо повідомлення
            content_0=b'\x00\x01\x00\x01\x00\x66\x00\x00'
            content_1=b'\x00\x01\x00\x66\x00\x01\x00\x00'
            content_start=b'\x00\x01\x00\x11\x00\x01\x00\x38\x60\x36\xA1\x09\x06\x07\x60\x85\x74\x05\x08\x01\x01\x8A\x02\x07\x80\x8B\x07\x60\x85\x74\x05\x08\x02\x01\xAC\x0A\x80\x08\x31\x32\x33\x34\x35\x36\x37\x38\xBE\x10\x04\x0E\x01\x00\x00\x00\x06\x5F\x1F\x04\x00\x00\x7E\x1F\x04\xB0'
            content_TIAE=b'\x00\x01\x00\x11\x00\x01\x00\x0D\xC0\x01\x81\x00\x03\x01\x00\x01\x08\x00\xFF\x02\x00'
            content_TASAE=b'\x00\x01\x00\x11\x00\x01\x00\x0D\xC0\x01\x81\x00\x03\x01\x00\x0F\x08\x00\xFF\x02\x00'
            content_end_1=b'\x00\x01\x00\x11\x00\x01\x00\x17\x62\x15\x80\x01\x00\xBE\x10\x04\x0E\x01\x00\x00\x00\x06\x5F\x1F\x04\x00\x00\x7E\x1F\x04\xB0'
            content_end_2=b'\x01\x00\x11\x00\x17\x63\x15\x80\x01\x00\xBE\x10\x04\x0E\x08\x00\x06\x5F\x1F\x04\x00\x00\x1A\x1D\x00\xF6\x00\x07'
            content_scaler_profile_1=b'\x00\x01\x00\x11\x00\x01\x00\x0D\xC0\x01\x81\x00\x07\x01\x00\x63\x01\x00\xFF\x03\x00'
            content_ask_profile_1=b'\x00\x01\x00\x11\x00\x01\x00\x40\xC0\x01\x81\x00\x07\x01\x00\x63\x01\x00\xFF\x02\x01\x01\x02\x04\x02\x04\x12\x00\x08\x09\x06\x00\x00\x01\x00\x00\xFF\x0F\x02\x12\x00\x00\x09\x0C\x07\xE9\x03\x18\x01\x00\x00\x00\x00\x00\x00\xFF\x09\x0C\x07\xE9\x03\x18\x01\x0F\x00\x00\x00\x80\x00\xFF\x01\x00'
            content_ask_profile_1_next=b'\x00\x01\x00\x11\x00\x01\x00\x07\xC0\x02\x81\x00\x00'
            content_ask_profile_1_period_block_start=b'\x00\x01\x00\x11\x00\x01\x00\x40\xC0\x01\x81\x00\x07\x01\x00\x63\x01\x00\xFF\x02\x01\x01\x02\x04\x02\x04\x12\x00\x08\x09\x06\x00\x00\x01\x00\x00\xFF\x0F\x02\x12\x00\x00\x09\x0C'
            content_ask_profile_1_period_block_continue=b'\xFF\x09\x0C'
            content_ask_profile_1_period_block_end=b'\xFF\x01\x00'
            content_answer_first_ask=b'\x00\x01\x00\x01\x00\x11\x00+a)\xa1\t\x06\x07`\x85t\x05\x08\x01\x01\xa2\x03\x02\x01\x00\xa3\x05\xa1\x03\x02\x01\x00\xbe\x10\x04\x0e\x08\x00\x06_\x1f\x04\x00\x00\x1a\x1d\x00\xf3\x00\x07'
            conn = sqlite3.connect('test_01.db')
            try:
                client_socket.settimeout(30)# Обмежуємо час очікування даних після підключення     
                data_1=client_socket.recv(1024)
            except  (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                client_socket.shutdown(socket.SHUT_WR)
                now = datetime.datetime.now()
                print(now, e, "time out 1 meter is offline")                
                continue #починаємо цикл зпочатку                             
            if data_1==content_0:                
                now = datetime.datetime.now()
                print( now, "reseived start message : ", data_1)
            else:
                try:
                    client_socket.shutdown(socket.SHUT_WR)
                    now = datetime.datetime.now()
                    print(f'{now}\t error data, meter is offline')
                except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                    client_socket.shutdown(socket.SHUT_WR)
                    now = datetime.datetime.now()
                    print(now, e, "time out 1 meter is offline")                
                continue #починаємо цикл зпочатку             
            
            ip, port = adress  # Отримуємо IP і порт клієнта
            now=datetime.datetime.now()
            print(f'{now}\t IP={ip}\t PORT={port}\t {number_metr}')
            #обмін  
            count_cicle=0
            #Додав перевірку відповіді на стартове повідомлення, чомусь іноді приходить інше
            while count_cicle<5:
                try:
                    client_socket.send(content_1)
                    time.sleep(6) #пауза між відправкою пакетів
                    client_socket.send(content_start)                                   
                    client_socket.settimeout(10)# Обмежуємо час очікування даних після підключення    
                    data_2=client_socket.recv(1024)
                except  (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error,OSError) as e:
                    now = datetime.datetime.now()
                    print(now, e, " 2"," - ", count_cicle)
                    count_cicle+=1
                    continue                       
                now = datetime.datetime.now()
                print(now, "reseived answer start", data_2)
                if data_2==content_answer_first_ask:
                    count_cicle=6
                else:
                    now = datetime.datetime.now()
                    print(f"{now} {number_metr} reseived data error, send data start again")
                    count_cicle+=1
            if count_cicle>5:
                count_cicle=0
            else:
                client_socket.shutdown(socket.SHUT_WR)
                now = datetime.datetime.now()
                print( f"{now}  start answer error {number_metr} is offline")
                continue
            while count_cicle <=5:
                try:                
                    client_socket.send(content_TIAE)
                    now = datetime.datetime.now()
                    print(now,'requested import active energy')
                    client_socket.settimeout(10)# Обмежуємо час очікування даних після підключення            
                    data_energy_TIAE=client_socket.recv(1024)
                except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                    now = datetime.datetime.now()
                    print(now, e)
                    count_cicle+=1
                    continue #починаємо цикл зпочатку
                now = datetime.datetime.now()                  
                print(now,data_energy_TIAE)                  
                temp_data=data_energy_TIAE
                temp_text=" Import activ energy: "              
                if len(temp_data)==17:
                    #print("index")
                    index=temp_data.find(b'\x06')
                    #now = datetime.datetime.now()
                    #print(now,"find HEX")
                    #hex_bytes = data_energy_TIAE[index + 1 : index + 5]
                    #print("value")
                    #value_data_energy_TIAE = int.from_bytes(hex_bytes, byteorder='big')*0.01
                    if index != -1 and index + 4 < len(temp_data):  
                        # Отримуємо наступні 4 байти після 0x06
                        hex_bytes = temp_data[index + 1 : index + 5]
                        # Перетворюємо байти у число (big-endian)
                        sum_import_active_energy = round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                        now = datetime.datetime.now()
                        print(f"{now}{temp_text}{sum_import_active_energy}")  # Виведе:
                        count_cicle=6
                    else:
                        if count_cicle==5:
                            now = datetime.datetime.now()
                            print(now,temp_text,"eror data")
                            count_cicle+=1
                        else:
                            count_cicle+=1
                else:
                    if count_cicle==5:
                        now = datetime.datetime.now()
                        print(now,temp_text,"eror data")
                        count_cicle+=1
                    else:
                        count_cicle+=1  
            count_cicle=0
            while count_cicle <=5:
                try:
                    now = datetime.datetime.now()
                    print(now,'request sum active energy')
                    client_socket.send(content_TASAE)
                    now = datetime.datetime.now()
                    print(now," resieving sum active energy")          
                    client_socket.settimeout(10)# Обмежуємо час очікування даних після підключення
                    data_energy_TASAE=client_socket.recv(1024)
                except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                    now = datetime.datetime.now()
                    print(now, e)
                    count_cicle+=1
                    continue #починаємо цикл зпочатку
                now = datetime.datetime.now()
                print(now,data_energy_TASAE)
                #hex_bytes = data_energy_TASAE[index + 1 : index + 5]
                #value_data_energy_TASAE= int.from_bytes(hex_bytes, byteorder='big')*0.01
                temp_data=data_energy_TASAE
                temp_text=" sum activ energy :"
                if len(temp_data)==17:
                    index=temp_data.find(b'\x06')
                    if index != -1 and index + 4 < len(temp_data):
                        #now = datetime.datetime.now()
                        #print(now,"find HEX")                          
                        # Отримуємо наступні 4 байти після 0x06
                        hex_bytes = temp_data[index + 1 : index + 5]
                        # Перетворюємо байти у число (big-endian)
                        total_import_active_energy = round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                        now = datetime.datetime.now()
                        print(f"{now} {temp_text} {total_import_active_energy}")  # Виведе: 
                        count_cicle=6
                    else:
                        if count_cicle==5:
                            now = datetime.datetime.now()
                            print(now,temp_text," eror data")
                            count_cicle+=1
                        else:
                            count_cicle+=1
                else:
                    if count_cicle==5:
                        now = datetime.datetime.now()
                        print(now,temp_text,"eror data")
                        count_cicle+=1
                    else:
                        count_cicle+=1
            conn = sqlite3.connect('test_01.db')
            curs = conn.cursor()
            now=str(datetime.datetime.now())
            try:
                curs.execute('INSERT INTO active_energy_registers (data, serial_number, sum_import_active_energy,total_import_active_energy) VALUES (?, ?, ?, ?)', 
             (now, number_metr, sum_import_active_energy,total_import_active_energy))
                print(now,"write data")
            except NameError or TypeError:
                print(now,"eror record")
            conn.commit()
            curs.close()
            conn.close()
            conn = sqlite3.connect('test_01.db')
            curs = conn.cursor()
            # Виконання запиту пошуку останього даних                     
            curs.execute('''                                        
                SELECT data_info, time_info, data_rec, id
                FROM profile_1_2
                WHERE serial_number = ?
                ORDER BY data_info DESC, time_info DESC, id DESC
                LIMIT 1;
            ''', (number_metr,))
            result = curs.fetchone()# Отримання результату
            if result:      # Перевірка, чи є результат
                data_info, time_info, data_rec, record_id = result
                print(f"Last line for  serial_number {number_metr}:")
                print(f"Day: {data_info}")
                print(f"Hour: {time_info}")
                print(f"Time record: {data_rec}")
                print(f"ID : {record_id}")
            else:
                print(f"Data for serial_number {number_metr} no data.")
                from datetime import datetime 
                #data_info=(f"{datetime.now().year}:{datetime.now().month}:01") #перетворюємо формат дату у строку
                data_info=(f"{datetime.now().year}:02:01")
                time_info="00:00:00"
                print(f'Date start {data_info} hour start {time_info}')
            curs.close()
            conn.close()
            from datetime import datetime
            date_temp = datetime.strptime(data_info, "%Y:%m:%d")    # Перетворюємо у формат datetime
            time_temp = datetime.strptime(time_info, "%H:%M:%S")
            
            year_start=date_temp.year
            month_start=date_temp.month
            day_start=date_temp.day
            period_day_start=datetime(year_start,month_start,day_start)
            week_day_start=period_day_start.weekday()+1
            hour_start=time_temp.hour
            minute_start=time_temp.minute
            secunde_start=10
            beas_start=0
            status_start=0
            period_start_time=datetime(year_start,month_start,day_start,hour_start,minute_start,secunde_start)
            period_start=year_start.to_bytes(2,'big')+month_start.to_bytes(1,'big')+day_start.to_bytes(1,'big')+week_day_start.to_bytes(1,'big')+hour_start.to_bytes(1,'big')+minute_start.to_bytes(1,'big')+secunde_start.to_bytes(1,'big')+beas_start.to_bytes(2,'big')+status_start.to_bytes(1,'big')
            year_end=datetime.now().year
            month_end=datetime.now().month
            day_end=datetime.now().day
            period_day_end=datetime(year_end,month_end,day_end)
            week_day_end=period_day_end.weekday()+1
            hour_end=datetime.now().hour
            minute_end=00
            secunde_end=0
            beas_end=0
            status_end=0
            period_end_time=datetime(year_end,month_end,day_end,hour_end,minute_end,secunde_end)
            print('period_end_time :', period_end_time)
            period_end=year_end.to_bytes(2,'big')+month_end.to_bytes(1,'big')+day_end.to_bytes(1,'big')+week_day_end.to_bytes(1,'big')+hour_end.to_bytes(1,'big')+minute_end.to_bytes(1,'big')+secunde_end.to_bytes(1,'big')+beas_end.to_bytes(2,'big')+status_end.to_bytes(1,'big')
            content_ask_profile_1=content_ask_profile_1_period_block_start+period_start+content_ask_profile_1_period_block_continue+period_end+content_ask_profile_1_period_block_end
            for_count=year_end.to_bytes(2,'big')+month_end.to_bytes(1,'big')+day_end.to_bytes(1,'big')+week_day_end.to_bytes(1,'big')+hour_end.to_bytes(1,'big')+minute_end.to_bytes(1,'big')
            content_profile_1_temp=content_ask_profile_1
            count_block_profile_1=1
            import datetime   
            if period_start_time<period_end_time:
                try:                
                        client_socket.send(content_scaler_profile_1)
                        now = datetime.datetime.now()
                        print(now, "send ask scaller profile and waiting answer")
                        client_socket.settimeout(10)# Обмежуємо час очікування даних після підключення          
                        data_scaler_profile_1=client_socket.recv(1024)
                        now = datetime.datetime.now()
                        print(data_scaler_profile_1)
                except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error, OSError) as e:
                        now = datetime.datetime.now()
                        print(now, e, 'error answer scaller')
            else:
                now = datetime.datetime.now()
                print(f'start:{period_start_time}\t and:{period_end_time} ')
                print(now, "no new data or error date")
            while True: 
                if period_start_time<period_end_time:
                    print(f'start:{period_start_time}\t and:{period_end_time} ')                    
                    now = datetime.datetime.now()
                    print(now, "start request profile")
                else :
                    break
                count_cicle=0 
                while count_cicle<6:
                    try:
                        print('content_profile_1_temp :', content_profile_1_temp)
                        client_socket.send(content_profile_1_temp)
                        now = datetime.datetime.now()
                        print(now, "send ask profile and waiting answer")
                        client_socket.settimeout(15)# Обмежуємо час очікування даних після підключення          
                        data_profile_1=client_socket.recv(1024)
                        print('data_profile_1 :', data_profile_1)
                        break
                    except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                        now = datetime.datetime.now()
                        print(now, e)
                        count_cicle+=1
                        continue                 
                if count_cicle==6: 
                    break
                    now = datetime.datetime.now()
                    print (f'{now}\t error data proffile')
                else:
                    count_cicle=0                
                number_line=data_profile_1.count(b'\x02\x05\x19')
                print('number of date: ', number_line)
                index=data_profile_1.find(b'\x02\x05\x19')
                print('first date', index)
                count=0
                corr=0
                while count<number_line:
                    hex_bytes = data_profile_1[index + 3 +corr: index + 5+corr]
                    year_1=int.from_bytes(hex_bytes, byteorder='big')
                    #print("year ",year_1)
                    hex_bytes = data_profile_1[index + 5+corr:index + 6+corr]
                    mounth_1=int.from_bytes(hex_bytes, byteorder='big')
                    #print("mohth ",mounth_1)
                    hex_bytes= data_profile_1[index + 6+corr: index + 7+corr]
                    day_1=int.from_bytes(hex_bytes, byteorder='big')
                    hex_bytes= data_profile_1[index + 8+corr: index + 9+corr]
                    hour_1=int.from_bytes(hex_bytes, byteorder='big')
                    hex_bytes= data_profile_1[index + 9+corr: index + 10+corr]
                    minute_1=int.from_bytes(hex_bytes, byteorder='big')
                    hex_bytes= data_profile_1[index + 10+corr: index + 11+corr]
                    secunde_1=int.from_bytes(hex_bytes, byteorder='big')
                    hex_bytes= data_profile_1[index + 12+corr: index + 14+corr]
                    bias_1=int.from_bytes(hex_bytes, byteorder='big')
                    #print("bias" ,bias_1)
                    hex_bytes= data_profile_1[index + 14+corr: index + 15+corr]
                    status_1=int.from_bytes(hex_bytes, byteorder='big')
                    print(status_1)
                    hex_bytes= data_profile_1[index + 16+corr: index + 20+corr]
                    all_import_active_energy_1=round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                    #print("all_import_active_energy_1" ,all_import_active_energy_1)
                    hex_bytes= data_profile_1[index + 21+corr: index + 25+corr]
                    all_export_active_energy_1=round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                    #print(" all_export_active_energy_1" , all_export_active_energy_1)
                    hex_bytes= data_profile_1[index + 26+corr: index + 30+corr]
                    all_import_reactive_energy_1=round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                    #print("all_import_reactive_energy_1" ,all_import_reactive_energy_1)
                    hex_bytes= data_profile_1[index + 31+corr: index + 35+corr]
                    all_export_reactive_energy_1=round(int.from_bytes(hex_bytes, byteorder='big')*0.01,2)
                    #print("all_export_reactive_energy_1" ,all_export_reactive_energy_1)    
                    print(f'{year_1}:{mounth_1}:{day_1}\t {hour_1}:{minute_1:02d}:{secunde_1:02d}\t {bias_1}\t {status_1}t {number_metr} \t all_import_active_energy : {all_import_active_energy_1}\t all_export_active_energy : {all_export_active_energy_1}\t all_import_reactive_energy : {all_import_reactive_energy_1}\t all_export_reactive_energy : {all_export_reactive_energy_1}')
                    data_info=f"{year_1}:{mounth_1:02d}:{day_1:02d}"
                    time_info=f"{hour_1:02d}:{minute_1:02d}:{secunde_1:02d}"
                    conn = sqlite3.connect('test_01.db')
                    curs = conn.cursor()
                    now=str(datetime.datetime.now())
                    try:
                        curs.execute('INSERT INTO profile_1_2 (data_rec, serial_number, data_info, time_info, bias, status, all_import_active_energy, all_export_active_energy, all_import_reactive_energy, all_export_reactive_energy, relevant) VALUES (?, ?, ?, ?,?, ?, ?, ?, ?, ?,?)', 
                        (now, number_metr, data_info, time_info,bias_1,status_1,all_import_active_energy_1,all_export_active_energy_1,all_import_reactive_energy_1,all_export_reactive_energy_1,1))
                        print(now,"write data profile")
                    except NameError or TypeError:
                        print(now,"eror record profile")
                    conn.commit()
                    curs.close()
                    conn.close()
                    corr+=35
                    count+=1
                time_end_res=data_profile_1.count(for_count) # кількість кінцевих дат у блоці відповіді
                if time_end_res==1 or len(data_profile_1)<52 or count_block_profile_1>960:
                    break
                else:                     
                    content_profile_1_temp=content_ask_profile_1_next+count_block_profile_1.to_bytes(2,'big')
                    count_block_profile_1+=1
                    continue
            now = datetime.datetime.now
            print(now,"send end message_1")
            try:
                client_socket.send(content_end_1)
                import datetime
                now = datetime.datetime.now()
                print(now, "waiting answer")
                client_socket.settimeout(10)# Обмежуємо час очікування даних після підключення          
                data_end_1=client_socket.recv(1024)
                now = datetime.datetime.now()
                print(now, "answer ok - ", data_end_1)
            except (socket.timeout, ConnectionResetError, BrokenPipeError,socket.error) as e:
                now = datetime.datetime.now()
                print(now, e)
            print(now, "comand shutdown")
            client_socket.shutdown(socket.SHUT_WR)
            now = datetime.datetime.now()
            print(f'{now}\t {number_metr}  is offline')
except KeyboardInterrupt:
    server.close()
    print('server clossed')
    

