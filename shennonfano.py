'''
Модуль содержит функции кодирования по алгоритму Шеннона-Фано
'''

print('Модуль кодирования по алгоритму Шеннона-Фано подключен...')
global code
code = {} # переменная с кодом
print('создана глобальная переменная с именем code!')

def list_word(input_word):
    '''
    Функция разбиения сообщения по символам
    '''
    
    print('разбиваем сообщение по буквам...')
    letters = []
    for letter in input_word:
        letters.append(letter)
    print('длина сообщения:', len(input_word))
    
    return letters
    
def count_word(word_letters):
    '''
    Функция подсчета частоты встречаемости символов
    '''
    
    all_letters = len(word_letters)
    print('считаем частоту встречаемости символов...')
    count_letter = {}
    for letter in word_letters:
        if letter not in count_letter:
            count_letter[letter] = word_letters.count(letter) / all_letters
    
    return count_letter
    
def sort_dict(letters_dict):
    '''
    Функция сортировки символов по частоте встречаемости
    '''
    
    print('сортируем символы по частоте встречаемости...')
    sorted_letters = sorted(letters_dict.items(), key=lambda tup: tup[1], reverse = True)
    
    return sorted_letters

def find_meadle(alphabet_part):
    '''
    Функция поиска середины суммы вероятностей
    '''
    print('рассматриваем символы %s...' % [letter_tup[0] for letter_tup in alphabet_part])
    
    #подсчитываем сумму
    sum_prob = sum([alphabet_part[i][1] for i,item in enumerate(alphabet_part)])
    print('сумма их вероятностей равна', sum_prob)
    
    #в цикле по алфавиту ищем середину суммы вероятностей
    prob = 0
    for meadle,letter_tup in enumerate(alphabet_part):
        prob += letter_tup[1]
        if prob > sum_prob / 2 and meadle > 0:
            print('в левую половину вошли элементы %s с суммой вероятностей %f' %
            ([alphabet_part[i][0] for i in range(meadle)], prob - letter_tup[1]))
            print('в правую половину вошли элементы %s с суммой вероятностей %f' %
            ([alphabet_part[i][0] for i in range(meadle,len(alphabet_part))], sum_prob - prob + letter_tup[1]))
            return meadle

def graph(alphabet,location):
    '''
    Функция построения графа кодирования
    '''
    
    letters_amount = len(alphabet)
    if letters_amount == 1: # если дошли до конечной вершины, то дальше не идм
        print('дошли до %s, его код %s' % (alphabet[0][0],code[alphabet[0][0]]))
        return
    else: # иначе делаем следующее
        
        # находим номер элемента середины суммы вероятностей
        counter = find_meadle(alphabet)
        
        # дописываем кодовую последовательность
        for i in range(counter): # элементам слева 0
            code[alphabet[i][0]] += '0'
        
        for i in range(counter,letters_amount): # элементам справа 1
            code[alphabet[i][0]] += '1'
        
        # разветвление на обход в лево и вправо
        for i in range(2):
            if i == 0: # идем по левой ветке
                graph(alphabet[0:counter],counter)
            else: # идем по правой ветке
                graph(alphabet[counter:letters_amount],counter)

def get_code(message):
    '''
    Функция получения кода по алгоритму Шеннона-Фано
    '''
    
    # формируем пары символ-вероятность
    letters_tup = sort_dict(count_word(list_word(message)))
    
    # подготавливаем места для кодовых последовательностей
    for item in letters_tup:
        code[item[0]] = ''
    
    # генерируем кодовые последовательности
    graph(letters_tup,'all')
    print('код сгенерирован успешно!')
    
    return code
    
def code_message(message):
    '''
    Функция кодирования сообщения в соответствии с полученным кодом
    '''
    coded_message = []
    for letter in message:
        coded_message.append(code[letter])
        
    coded_message = ''.join(coded_message)
    
    return coded_message
    
def decode_message(message):
    '''
    Функция декодирования сообщения в соответствии с полученным кодом
    '''
    decoded_message = []
    decode = {value: key for key, value in code.items()}
    
    letter_buffer = ''
    for letter in message:
        letter_buffer += letter
        try: 
            decoded_message.append(decode[letter_buffer])
            letter_buffer = ''
        except KeyError:
            pass
        
    decoded_message = ''.join(decoded_message)
    
    return decoded_message