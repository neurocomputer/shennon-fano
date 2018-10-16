import shennonfano as sf

f = open('sample.txt', 'r')

message = f.read()
print(len(message))

code = sf.get_code(message)

print(code)

coded_message = sf.code_message(message)

print(coded_message)

print(len(coded_message)/8)

decoded_message = sf.decode_message(coded_message)

print(decoded_message)

print('Длина исходная:',len(message),'Длина полученная:',len(decoded_message))
