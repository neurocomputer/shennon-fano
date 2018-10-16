import shennonfano as sf

word = 'mississippi'

code = sf.get_code(word)

print(code)

coded_message = sf.code_message(word)

print(coded_message)

decoded_message = sf.decode_message(coded_message)

print(decoded_message)