# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.
# ------------------------

def float_converter(arg):
    res = 0

    if isinstance(arg, float):
        res = arg
        return res

    try:
        res = float(arg)
    except Exception:
        print('Exception in float_converter! Somthing wrong with input data!')

    return res

print(float_converter(10))
print(float_converter(-10))
print(float_converter(10.10))
print(float_converter(-10.10))
print(float_converter('10'))
print(float_converter('-10'))
print(float_converter('10.10'))
print(float_converter('10'))
print(float_converter(''))
print(float_converter('asfasd10'))

# Напишіть функцію, що приймає два аргументи. Функція повинна
#   a. якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#   b. якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
#   c. у будь-якому іншому випадку повернути кортеж з цих аргументів
# ------------------------

def wierd_functional(arg1, arg2):
    res = None
    condition_for_multiply = (isinstance(arg1, int) or isinstance(arg1, float)) and isinstance(arg2, int) or isinstance(arg2, float)
    condition_for_concut =  isinstance(arg1, str) and isinstance(arg2, str)

    if condition_for_multiply:
        res = arg1 * arg2

    elif condition_for_concut:
        res = arg1 + arg2

    else:
        res = (arg1, arg2)

    return res

print(wierd_functional(2, 2))
print(wierd_functional(2.2, 2))
print(wierd_functional(2, 2.2))
print(wierd_functional(2.2, 2.2))
print(wierd_functional('hello ', 'world'))
print(wierd_functional(2, '2'))
print(wierd_functional('2', 2))
print(wierd_functional('2.2', 2))
print(wierd_functional(2, '2.2'))
print(wierd_functional('abc', 'efg'))
print(wierd_functional([2, 2.2], {'a': 1, 'b': 2}))

# Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#   @ Попросіть користувача ввести свій вік.
#       - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
#       - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
#       - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
#       - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
#       - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# 
#   @Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).
# 
#   Наприклад:
#       "Тобі ж 5 років! Де твої батьки?"
#       "Вам 81 рік? Покажіть пенсійне посвідчення!"
#       "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"
# ------------------------
# initial helper functions

# 
# config_age_word_handler helps to configure word, that comes after age in message
# 
def config_age_word_handler(age):
    age_word = ''
    last_number = age % 10

    if 5 <= age < 20:
        age_word = 'років'
    elif last_number == 1:
        age_word = 'рік'
    elif last_number in (2, 3, 4):
        age_word = 'роки'
    elif last_number in (0, 5, 6, 7, 8, 9):
        age_word = 'років'

    return age_word

# 
# config_message_handler helps to configure message for user
# 
def config_message_handler(age, age_word):
    message = 'Шось в мене пішло не так, вибачте!'

    if age <= 0:
        message = 'Вік не може бути меншим, або рівним нулю!'
    elif '7' in str(age) and age <= 7:
        message = f'Вам {age} {age_word}, вам пощастить! Але все одно: де твої батьки?!'
    elif '7' in str(age) and age > 7:
        message = f'Вам {age} {age_word}, вам пощастить!'
    elif age < 7:
        message = f'Тобі ж {age} {age_word}! Де твої батьки?'
    elif age < 16:
        message = f'Тобі лише {age} {age_word}, а це є фільм для дорослих!'
    elif age > 65:
        message = f'Вам {age} {age_word}? Покажіть пенсійне посвідчення!'
    else:
        message = f'Незважаючи на те, що вам {age} {age_word}, білетів всеодно нема!'

    return message

# 
# cashier_logic function with all main logic
# 
def cashier_logic(input_age):
    #main if
    if not input_age.isdigit():
        message = 'Введено не тільки цифри!'

    else:
        age = int(input_age)

        age_word = config_age_word_handler(age)
        message = config_message_handler(age, age_word)

    return message

# 
# main_game function with loopback
# 
def main_game():
    restart_condition = True

    print('-----\nВітаємо у цікавезній грі Кассир!')

    while restart_condition:

        # initiate user input
        user_input = input('Введіть ваш вік, будь ласка: ')

        # main logic
        print(cashier_logic(user_input))

        # restart loop
        while True:
            user_input_condition = input('Do you want to repeat the game? yes/no(y/n) ->').strip().lower()
            print(user_input_condition)
            if user_input_condition == 'yes' or user_input_condition == 'y':
                restart_condition = True
                break
            elif user_input_condition == 'no' or user_input_condition == 'n':
                restart_condition = False
                break
            else:
                print('Enter exactly \'yes\', (\'y\') or \'no\', (\'n\')< please.')
                continue

# starting game:
main_game()