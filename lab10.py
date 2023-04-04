import functools

# Тізім құрастырамыз
words = ["hello", "world", "python", "programming"]

# Фильтр о сөзі барларды
filtered_words = filter(lambda word: 'o' in word, words)

#Шыққан сөздерден ASCII кодқа аударамыз
letters_set = set()
for word in filtered_words:
    for letter in word:
        letters_set.add(ord(letter))

# Сөздік жасаймыз ішіндегі кілттердің мәні сан бірақ ASCII кодта жазылып шығады
char_dict = {chr(code): code for code in letters_set}

# Тізім
even_codes = filter(lambda code: code % 2 == 0, char_dict.values())
even_chars = [chr(code) for code in even_codes]

# Генератор символ-кодты жасаймыз, оның ішінде символдар - әріптер filtered_words-тың ішіндегі

char_code_pairs = zip("".join(even_chars), map(ord, "".join(even_chars)))

# Екі ASCII кодты қосатың функция
def sum_ascii_codes(a, b):
    return a + b

# Барлық символдың кодтарын қосамыз
letters_sum = functools.reduce(sum_ascii_codes, map(ord, "".join(even_chars)), 0)

# even_chars-тың ASCII кодын тексереміз оның барлық символдары жұп екенін
all_even = all(code % 2 == 0 for code in map(ord, even_chars))

# о әріпінен кейінгі әріпті шығарып береді
next_char = chr(next(iter(char_dict.values()), 0) + len(char_dict))


print(filtered_words)
print(char_dict)
print(even_chars)
print(list(char_code_pairs))
print(letters_sum)
print(all_even)
print(next_char)
