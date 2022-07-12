import random


def valid(a):
    if a.lower() == 'д':
        return True
    elif a.lower() == 'н':
        return False
    else:
        a = input('Ответ не правильный повторите д = да, н = нет >>  ')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

print('Укажите характеристики паролей:')
password_need = int(input('Сколько нужно паролей? >>  '))
length_need = int(input('Какая будет длина пароля? >>  '))
digits_need = valid(input('Включать ли цифры 0123456789? (д = да, н = нет) >>  '))
uppercase_need = valid(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д = да, н = нет) >>  '))
lowercase_need = valid(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д = да, н = нет) >>  '))
punctuation_need = valid(input('Включать ли символы !#$%&*+-=?@^_? (д = да, н = нет) >>  '))
symbol_need = valid(input('Исключать ли неоднозначные символы il1Lo0O? (д = да, н = нет) >>  '))

if digits_need == 'д':
    chars += digits
if uppercase_need == 'д':
    chars += uppercase_letters
if lowercase_need == 'д':
    chars += lowercase_letters
if punctuation_need == 'д':
    chars += punctuation
if symbol_need == 'д':
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')


def generate_password(chars, length_need):
    password = random.sample(chars, length_need)
    print(*password, sep='')


for _ in range(0, password_need):
    generate_password(chars, length_need)
