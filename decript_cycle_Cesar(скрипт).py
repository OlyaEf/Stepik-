text = input('Введите текст для дешифровки >>  ')
alph = 'abcdefghijklmnopqrstuvwxyz'

for k in range(26):
    x = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            x += text[i]
        else:
            if text[i].isupper():
                x += (alph[alph.find(text[i].lower())-k]).upper()
            else:
                x += alph[alph.find(text[i].lower())-k]
    print(x)
