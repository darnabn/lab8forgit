import functools

# Создаем список из нескольких слов
words = ["hello", "world", "python", "programming"]

# Фильтруем слова, которые содержат букву "o"
filtered_words = filter(lambda word: 'o' in word, words)

# Создаем множество из ASCII кодов букв, встречающихся в отфильтрованных словах
letters_set = set()
for word in filtered_words:
    for letter in word:
        letters_set.add(ord(letter))

# Создаем словарь, где ключами являются символы, а значениями - их ASCII коды
char_dict = {chr(code): code for code in letters_set}

# Создаем список из четных ASCII кодов символов, содержащихся в char_dict
even_codes = filter(lambda code: code % 2 == 0, char_dict.values())
even_chars = [chr(code) for code in even_codes]

# Создаем генератор из пар символ-код, где символы - это буквы, содержащиеся в filtered_words
char_code_pairs = zip("".join(filtered_words), map(ord, "".join(filtered_words)))

# Функция, которая складывает ASCII коды двух символов
def sum_ascii_codes(a, b):
    return a + b

# Складываем ASCII коды всех символов, содержащихся в filtered_words
letters_sum = functools.reduce(sum_ascii_codes, map(ord, "".join(filtered_words)), 0)

# Проверяем, что все символы в even_chars имеют четные ASCII коды
all_even = all(code % 2 == 0 for code in map(ord, even_chars))

# Получаем следующий символ после последнего символа в char_dict
next_char = chr(next(iter(char_dict.values()), 0) + len(char_dict))


print(filtered_words)
print(char_dict)
print(even_chars)
print(list(char_code_pairs))
print(letters_sum)
print(all_even)
print(next_char)
