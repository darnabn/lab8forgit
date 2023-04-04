#1 тапсырма Сұңқар
# 10 кірістірілген функцияны алып,
# бір бірімен үйлестіріп бағдарлама жазамыз.
# Барлық функциялар өзарабайланысты болуы керек,
# жəне бағдарламаның логикалық басы мен соңы болуы қажет.
import random

# Әртүрлі санды генерация жасайтын функция
def generate_random_number(start, end):
    return random.randint(start, end)

# Сөзді қабылдап оның ұзындығын шығарып береді
def get_string_length(text):
    return len(text)

# Екі санның қосындысын табатын функция
def add_numbers(num1, num2):
    return num1 + num2

# Списокты қабылдап оны реттейтін функция
def sort_list(lst):
    return sorted(lst)

# Екі сөзді қосатын функция
def concatenate_strings(str1, str2):
    return str1 + str2

# Санның квадраты
def get_square(num):
    return num**2

# Тізімнің орташа санын тауып береді
def get_average(lst):
    return sum(lst) / len(lst)

# Сөзді үлкен әріптермен жазып береді
def convert_to_uppercase(text):
    return text.upper()

# Факториалды тауып беретін функ
def get_factorial(num):
    if num == 0:
        return 1
    else:
        return num * get_factorial(num-1)

# Тізімнің ұзындығы
def get_list_length(lst):
    return len(lst)

random_num = generate_random_number(1, 10)
print("Кездейсоқ сан: ", random_num)


text = "SAAAAAATBAYEEEV!"
text_length = get_string_length(text)
print("Мына сөздің ->'", text, "' ұзындығы ", text_length)

sum_of_numbers = add_numbers(3, 4)
print("Sum = ", sum_of_numbers)

lst = [4, 2, 7, 1, 9]
sorted_list = sort_list(lst)
print("Тізім: ", sorted_list)

str1 = "Hello, "
str2 = "world!"
concatenated_string = concatenate_strings(str1, str2)
print("Қосылған строка: ", concatenated_string)

num = 5
square = get_square(num)
print("Осы санның ", num, " квадраты ", square)


lst = [4, 2, 7, 1, 9]
get_average = get_average(lst)
print("ортасы", get_average)

text = "Janny have a good taste"
convert_to_uppercase = convert_to_uppercase(text)
print(convert_to_uppercase)

num = 3
get_factorial = get_factorial(num)
print(get_factorial)

lst = [4,4,4,8,9,7,5,6]
get_list_length = get_list_length(lst)
print(get_list_length)