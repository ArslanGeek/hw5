from random import choice
from decouple import config


def start_game():
    numbers = []

    for i in range(1, 31):
        numbers.append(i)

    print('Welcome to the Casino!!')
    play = input('Do you want to play? (yes/no): ').lower()
    if play == 'yes':
        my_money = config(f'MY_MONEY', cast=int)
        while True:
            i = choice(numbers)
            print(f'Your cash is {my_money}$')
            num = int(input('\nEnter your number: '))
            bet = int(input('How much money do you want to bet: '))
            if int(bet) > my_money:
                print(f'You dont have enough money')
                print(f'Please, try again')
                start_game()

            if num == i:
                cash = bet * 2
                my_money += int(cash)
                print(f'\nThe number was {i}')
                print(f'You won {cash}$')
            elif num != i:
                my_money -= int(bet)
                print(f'\nThe number was {i}')
                print(f'You lose {bet}$')
                print(f'Now your cash is {my_money}$')

            if my_money <= 0:
                print(f'\nYour cash is {my_money}')
                print(f"You cannot continue the game")
                break
            restart = input('\nDo you want to play again? (yes/no): ').lower()
            if restart == 'no':
                print('---Game is finished---')
                break
    else:
        print(f'Thank you for coming! Good Bye!')


if __name__ == '__main__':
    start_game()
