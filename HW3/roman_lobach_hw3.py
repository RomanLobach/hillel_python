# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
print('--- task #1 ---')

while True:
    user_input_phrase = input('Input Your phrase, please --> ').strip()
    if len(user_input_phrase):
        break

user_input_phrase_length = len(user_input_phrase)

while True:
    user_input_number = input(f'Input number in range of 1 and {user_input_phrase_length}, please :) --> ').strip()
    if user_input_number.isdigit() and int(user_input_number) <= user_input_phrase_length and int(user_input_number) > 0:
        break

user_number = int(user_input_number)
symbol = user_input_phrase[user_number - 1]

print(f"The {user_number} symbol in '{user_input_phrase}' is '{symbol}'")

# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
print('--- task #2 ---')

user_input_phrase = input('Input Your phrase: ').strip()

while not user_input_phrase:
    print("Invalid input. Please enter some words!")
    # тут має бути більше перевірок, застосовуючи регулярку, щоб виключити різні аказії. але їх ми ще не вчили :)
    # тому залишаю перевірку лише на ненульову довжину інпуту
    user_input_phrase = input('Input Your phrase: ').strip()

user_phrase_list = user_input_phrase.split()
print(f'Yor phrase has {len(user_phrase_list)} words.')

# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
print('--- task #3 ---')

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 2.1, 'Lorem Ipsum']
lst2 = []

for elem in lst1:
    elem_type = type(elem)
    if elem_type == int or elem_type == float:
        lst2.append(elem)

print(f'New list is: {lst2}')