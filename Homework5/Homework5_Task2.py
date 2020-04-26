'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

char_list = []
try:
    with open("Input_task2.txt") as in_f:
        for line in in_f:
            char_count = 0
            for char in line:
                char_count += 1
            char_list.append(char_count)
except IOError:
    print('File not found')

print('Number of lines: ', len(char_list))
for i, el in enumerate(char_list):
    print('{1} chars in line №{0}'.format(i+1, el))
