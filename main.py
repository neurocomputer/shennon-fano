import shennonfano as sf

#выбираем текст для кодирования
f = open('sample.txt', 'r')
message = f.read()

#генерируем код с помощью модуля shennonfano
code = sf.get_code(message)

#выводим на экран код
print(code)

#кодируем сообщение
coded_message = sf.code_message(message)

#выводим на экран кодированное сообщение
print(coded_message)

#выводим на экран размер сообщения в байтах
print(len(coded_message)/8)

#декодируем сообщение
decoded_message = sf.decode_message(coded_message)

#выводим на экран декодированное сообщение
print(decoded_message)

#сравниваем длину до кодирования и после декодирования
print('Длина исходная:',len(message),'Длина полученная:',len(decoded_message))
