text = input('Введите текст для дешифровки >>  ').split()
alphabet_en_lower = 'abcdefghigklmnopqrstuvwxyz'
alphabet_en_upper = alphabet_en_lower.upper()
ord_en = ord('a')
ord_En = ord('A')
new_text = ''

for i in text:
    step = 0
    for j in i:
        if j.isalpha() == True:
            step += 1
    for j in i:
        if j in alphabet_en_lower:
            new_text += chr(((ord(j) - ord_en + step) % 26) + ord_en)
        elif j in alphabet_en_upper:
            new_text += chr(((ord(j) - ord_En + step) % 26) + ord_En)
        else:
            new_text += j
    new_text += ' '

print(new_text)


