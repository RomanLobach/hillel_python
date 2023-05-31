# Доопрацюйте гру з заняття наступним чином:
#   @Додайте вибір слова з будь-якого джерела на ваш вибір
#   @Додайте лічильник спроб вгадати слово і вихід з циклу по переповненню лічильника
#   @Додайте більш інформативні повідомлення (список можливих букв для введення, повідомлення про невірне введення, повідомлення про кількість спроб що залишилися і тд)
#   @Опційно. Додайте можливість повторювати гру. Запитати в гравця чи хоче він повторити гру Yes/No і повторювати якщо він введе Yes, завершити якщо введе No

import random

print('\n- Welcome to the game "Guess the Word"! \n- The Player has to unscramble the word by letters (One letter of the English alphabet at a time).\n- Let\'s go to the game and good luck!\n')

# initiate words list
words_list = ['intrepid', 'climber', 'conquere', 'formidable', 'peak', 'amidst', 'treacherous', 'weather', 'condition', 'enthusiastic', 'musicians', 'harmonized', 'melodies', 'captivating', 'audiences', 'with', 'their', 'soulful', 'performances']

restart_condition = True

while restart_condition: 
    # initiate halper variables
    word = words_list[random.randint(0, len(words_list) - 1)]
    guess_result = '?' * len(word)
    guessed_letters = []
    entered_letters = set()
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    attempt_counter = 0
    max_attemts = 20

    #main loop
    while True:
        print('-----\n')

        if not (max_attemts - attempt_counter):
            print('Sorry! The number of attempts is over!')
            break

        print(f'Guess the word: {guess_result}')

        while True:
            print(f'You have {max_attemts - attempt_counter} attemts left!')
            user_letter = input('- Enter a letter of the English alphabet: ').lower()
            attempt_counter += 1

            if len(user_letter) != 1:
                print('Incorrect number of characters. There must be entered one letter at a time')
                continue
            elif user_letter not in available_letters:
                print('Eou entered an invalid character. Enter a letter of the English alphabet, please!')
                continue
            elif user_letter in entered_letters:
                print('You have already entered this letter. Try another one please!')
                continue

            entered_letters.add(user_letter)
            break

        if user_letter in word:
            guessed_letters.append(user_letter)
            guess_result = ''.join(['?' if char not in guessed_letters else char for char in word])

            if guess_result == word:
                print('Oh, congratulations, Champion! Champagne is on the way :) !')
                break

        else:
            print('Sorry! Didn\'t guess. Try one more time.') if max_attemts - attempt_counter else print('Sorry! Didn\'t guess.')

    #restart loop
    while True:
        user_input_condition = input('Do you want to repeat the game? yes/no ->').strip().lower()
        print(user_input_condition)
        if user_input_condition == 'yes':
            restart_condition = True
            break
        elif user_input_condition == 'no':
            restart_condition = False
            break
        else:
            print('Enter exactly \'yes\' or \'no\', please.')
            continue
