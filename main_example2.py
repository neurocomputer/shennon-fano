from shennonfano import *

#сообщение для кодирования
word = 'mississippi'

#генерируем код с помощью модуля shennonfano
get_code(word)

#выводим на экран код
print(code)

#кодируем сообщение
coded_message = code_message(word)

#выводим на экран кодированное сообщение
print(coded_message)

#декодируем сообщение
decoded_message = decode_message(coded_message)

#выводим на экран декодированное сообщение
print(decoded_message)
