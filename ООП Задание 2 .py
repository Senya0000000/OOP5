def reverse(word): # Определяем функцию reverse, которая будет инвертировать слова в сообщении
    punctuation_marks = '.,?- :;!"' # Определяем строку с знаками препинания
    word_rev=''# Переменная для хранения инвертированного слова
    res=''#переменная для хранения результата
    for sym in word:# Проходим по каждому символу в слове
        if sym not in punctuation_marks: # Если символ не является знаком препинания, добавляем его к инвертированному слову
            word_rev += sym
        else:
            word_rev = word_rev[::-1] # Если символ является знаком препинания, инвертируем инвертированное слово
            res+=word_rev+sym# Добавляем инвертированное слово и знак препинания к результату
            word_rev = '' # Сбрасываем инвертированное слово для следующего символа знака препинания
    word_rev = word_rev [::-1]# Инвертируем последнее слово и добавляем его к результату
    res += word_rev
    return res# Возвращаем инвертированное слово
message=input('Сообщение: ').split()# ввод от пользователя и разбивка его на слова
reverse_mes = ''
for word in message:# Проходим по каждому слову в сообщении и инвертируем его
    reverse_mes += ' ' + reverse(word)
print('Новое сообщение: ', reverse_mes)# Выводим инвертированное сообщение