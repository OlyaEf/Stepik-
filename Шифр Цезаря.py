action = input('Выберите действие:\nШифрование(1) или Дешифрование(2) >>  ')
step = int(input('Шаг шифровки >>  '))
text = input('Введите текст >>  ')


def encript(text, step):
    alphabet_ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_ru_upper = alphabet_ru_lower.upper()

    alphabet_en_lower = 'abcdefghigklmnopqrstuvwxyz'
    alphabet_en_upper = alphabet_en_lower.upper()

    ord_ru = ord('а')
    ord_Ru = ord('А')

    ord_en = ord('a')
    ord_En = ord('A')

    new_text = ''

    for i in text:
        if i in alphabet_ru_lower:
            new_text += chr(((ord(i) - ord_ru + step) % 32) + ord_ru)
        elif i in alphabet_en_lower:
            new_text += chr(((ord(i) - ord_en + step) % 26) + ord_en)
        elif i in alphabet_ru_upper:
            new_text += chr(((ord(i) - ord_Ru + step) % 32) + ord_Ru)
        elif i in alphabet_en_upper:
            new_text += chr(((ord(i) - ord_En + step) % 26) + ord_En)
        else:
            new_text += i

    return new_text


def decript(text, step):
    return encript(text, -step)


if action == '1':
    print(encript(text, step))
elif action == '2':
    print(decript(text, step))

