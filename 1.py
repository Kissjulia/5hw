# Напишите программу, удаляющую из тек
text = str(input('Введите текст'))
def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = del_words(text)
print(text)