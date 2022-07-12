from random import randint

print('Добро пожаловать в Игру: "Угадай число или УМРИ"')
print('У вас будет всего 6 попыток, что бы остаться в Ж И В Ы Х!')


def is_val(a: 1, n):
    if a.isdigit():
        return 1 <= int(a) <= n
    return False


def game():
    start = input("Вы уверены, что хотите играть? (д = да, н = нет) >>  ")
    if start == 'н':
        print('Сегодня на одного человека останется больше людей. Прощай!')
        return False

    if start == 'д':
        print('Начнем!')
        n = int(input('Введите крайнюю границу, до какого числа будем угадывать цифры >> '))
        guess_num, our_num, count = randint(1, n), 0, 0
        print(f'Угадайте число от 1 до {n}')

        while True:
            inputted = input('Ваш выбор >> ')
            count += 1

            if is_val(inputted, n):
                our_num = int(inputted)
            else:
                print('А может быть введете целое число от 1 до загаданного вами?')
                continue

            if guess_num == our_num:
                print('Вы угадали, поздравляем!')
                again = input('Хотите сыграть еще раз? (д = да, н = нет): ')
                if again == 'д':
                    return game()
                else:
                    break
            elif count == 6:
                print('УПС... Количество попыток превышено! Умри человечешка!\n'
                      'GAME OVER')
                break
            else:
                print(f'Ваше число {"больше" if guess_num < our_num else "меньше"} загаданного, попробуйте еще разок')

        print(f'Спасибо, что играли в числовую угадайку. Ваше количество попыток: {count}')


game()

