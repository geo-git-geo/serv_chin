dec_number1=33550399  # число у десятковому форматі
dec_number_d=33550399  # число у десятковому форматі
#hex_bytes = dec_number1.to_bytes(2,'big') #тре вказати кількість байтів
#print(hex_bytes)
# Перетворюємо байти у число (big-endian)
#number = int.from_bytes(hex_bytes, byteorder='big')
#print(number)
shedule_d=bin(dec_number_d) #перетворення у двійкову
print(shedule_d)
shedule=bin(dec_number1) #перетворення у двійкову
print(shedule)