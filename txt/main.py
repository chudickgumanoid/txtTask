from os import path

# список для вывода
filesName = ['Библия.txt', 'Божественная комедия.txt', 'Путь лидера.txt']
print("Название файла: ", filesName[0])


# вывод расширения файла
full_name = path.basename(r'Библия.txt')
ex = path.splitext(full_name)[1]
print('Расширение данного файла', ex)

# подсчет строк в файле
with open('Библия.txt', 'r', encoding='utf-8') as file:
    line_count = 0
    for line in file:
        line_count += 1

print("Количество строк в файле:", line_count)

# подсчет слов в файле
with open('Библия.txt', 'r', encoding='utf-8') as file:
    words_count = 0
    for word in file.read().split():
        words_count += 1
print('Количество слов в файле:', words_count)


# считает повторяющееся слово
count = 0
wordRep = ""
maxCount = 0
words = []
with open('Библия.txt', 'r', encoding='utf-8') as file:

# Получает каждую строку до конца файла
    for line in file:
        # Разбиваем каждую строку на слова
        string = line.lower().split(" ")
        for s in string:
            words.append(s)

    # Определение наиболее часто повторяющегося слова в файле
    for i in range(0, len(words)):
        count = 1
        # Подсчет каждого слова в файле и сохрание его в переменной count
        for j in range(i + 1, len(words)):
            if (words[i] == words[j]):
                count = count + 1

        # Если соблюдается условие то сохраняем значение count в maxCount, и слово
        if count > maxCount:
            maxCount = count
            wordRep = words[i]

print("Самое встречающееся слово: " + wordRep)



# действия над файлом Божественная комедия
# подсчет строк в файле
print('\n', "Название файла: ", filesName[1])
print('Расширение данного файла', ex)
with open('Божественная комедия.txt', 'r', encoding='utf-8') as file:
    line_count = 0
    for line in file:
        line_count += 1

print("Количество строк в файле:", line_count)

# подсчет слов в файле
with open('Божественная комедия.txt', 'r', encoding='utf-8') as file:
    words_count = 0
    for word in file.read().split():
        words_count += 1
print('Количество слов в файле:', words_count)


# действия над файлом Путь лидера
# подсчет строк в файле
print('\n',"Название файла: ", filesName[2])
print('Расширение данного файла', ex)
with open('Путь лидера.txt', 'r', encoding='utf-8') as file:
    line_count = 0
    for line in file:
        line_count += 1

print("Количество строк в файле:", line_count)


# подсчет слов в файле
with open('Путь лидера.txt', 'r', encoding='utf-8') as file:
    words_count = 0
    for word in file.read().split():
        words_count += 1
print('Количество слов в файле :', words_count)



# обозначение переменных для вывода
title = 'Название: '
extension = 'Расширение файла: '
lineSum = 'Количество строк в файле: '
wordSum = 'Количество слов: '
meet = 'Самое встречающееся слово: '
firstOn = 'Его место в тексте'

# вывод в отдельный файл
f = open('output.txt', 'w', encoding='utf-8')
f.write(title + filesName[0] + '\n')
f.write(extension + ex + '\n')
f.write(lineSum + str(line_count) + '\n')
f.write(wordSum + str(words_count) + '\n')
f.write(meet + wordRep + '\n')
with open('Библия.txt', 'r', encoding='utf-8') as file:
    f.write('\n' + file.read() + "\n")

# вывод для второго файла
f.write(title + filesName[1] + '\n')
f.write(extension + ex + '\n')
f.write(lineSum + str(line_count) + '\n')
f.write(wordSum + str(words_count) + '\n')
with open('Божественная комедия.txt', 'r', encoding='utf-8') as file:
    f.write('\n' + file.read() + "\n")

# вывод для третьего файла
f.write('\n' + '\n' + title + filesName[2] + '\n')
f.write(extension + ex + '\n')
f.write(lineSum + str(line_count) + '\n')
f.write(wordSum + str(words_count) + '\n')
with open('Путь лидера.txt', 'r', encoding='utf-8') as file:
    f.write('\n' + file.read() + "\n")
