# Напишіть гру 'Rock paper scissors' https://en.wikipedia.org/wiki/Rock_paper_scissors
# Грають гравець і компʼютер. Вdід даних гравцем - через input()
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду (DRY, KISS, YAGNI).

import random


def get_user_choice():
    '''
    Function initiate players choise from console input.

    Returns:
        int: The return value. 1 corresponds to Rock, 2 corresponds to Paper, 3 correspondes to Scissors.
    '''
    while True:
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')

        user_choice = input('Enter your choice (1-3): ')

        if user_choice in ['1', '2', '3']:
            return int(user_choice)

        else:
            print('\nInvalid choice!\nPlease enter a valid option (1-3).')


def get_computer_choice():
    '''
    Function initiate computers choise useing random int in range 1-3.

    Returns:
        int: The return value. 1 corresponds to Rock, 2 corresponds to Paper, 3 correspondes to Scissors.
    '''
    return random.randint(1, 3)


def converter_from_int_to_game_unit(game_int):
    '''
    Converts the numerical selection of the players into the corresponding text equivalent.
    '1' converts into 'Rock', '2' converts into 'Paper', '3' converts into 'Scissors'.

    Args:
        game_int (int): int selection of one of the players.
    Returns:
        str: Prepared text message - the result of convertation.
    '''
    if game_int == 1:
        return 'Rock'
    elif game_int == 2:
        return 'Paper'
    else:
        return 'Scissors'


def get_winner(user_choice, computer_choice):
    '''
    Function calculates the result of the game.

    Args:
        user_choice (int): user choise.
        computer_choice (int): computer choise.

    Returns:
        str: The text of the message with the results of the game.
    '''
    if user_choice == computer_choice:
        return 'It\'s a draw!'

    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return 'Player wins!'

    else:
        return 'Computer wins!'


def get_exit_game_condition():
    '''
    Function determines the condition for exiting the game at the player's request.

    Returns:
        bool: Value answers the question "Do you want to exit the game?".
    '''
    while True:
        play_again = input('\nDo you want to play again? (y/n): ').lower()

        if play_again == 'n' or play_again == 'no':
            return True #exit game?

        elif play_again == 'y' or play_again == 'yes':
            return False #exit game?

        else: 
            print('\nYou should choose between "y", "yes", "n" and "no"!')


def game():
    '''
    Function contains the main logic of the game. 
    There is interaction with the user through messages in the console, as well as receiving parameters from the user.
    The results are calculated by excluding pre-declared functions.
    The function takes no arguments and returns nothing.
    '''

    hello_message = '\nHello and welcome to the interesting game "Rock Scissors Paper".\nYou will play with the computer.\nIn each round, you and the computer take turns choosing between rock, scissors, or paper.\nRock beats scissors, scissors beat paper, and paper beats rock.\nMake your choice and good luck!\n'
    print(hello_message)

    while True:
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f'\nPlayer chose: {converter_from_int_to_game_unit(player_choice)}')
        print(f'Computer chose: {converter_from_int_to_game_unit(computer_choice)}')

        result_message = get_winner(player_choice, computer_choice)
        print(result_message)

        restart_game_condition = get_exit_game_condition()

        if restart_game_condition:
            break

    print('\nThank you for playing!')


game()