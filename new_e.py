


import re
import os

# Задание 1
def opens_file():
    some_f = input('Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')
    while True:
        try:
            f = open(some_f, 'r')
        except FileNotFoundError:
            some_f = input('Такого файла нет. Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')
        else:
            break
    
    return some_f

def reads_file(path):
    f = open(path, 'r', encoding = 'UTF-8')
    string = f.read()
    f.close()
    return string


def find_name1(string):
    res = re.findall('([А-ЯЁ]\. [А-ЯЁ][а-яё]+(\.|,|!|\?|\:|\;|_|-| |\)|]|\n))', string)
    for elem in res:
        n_el = elem[0].strip('.,!?-)\n ')
        #print(n_el)

#Задание 2
names = []
def find_name2(string):
    res = re.findall('(([А-ЯЁ]\. ?){1,2} [А-ЯЁ][а-яё]+(\.|,|!|\?|\:|\;|_|-| |\)|]|\n))', string)
    for elem in res:
        n_el = elem[0].strip('.,!?-)\n ')
        names.append(n_el)#print(n_el)
    return names
def find_name3(string):
    res = re.findall('([А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+(\.|,|!|\?|\:|\;|_|-| |\)|]|\n))', string)
    for elem in res:
        n_el = elem[0].strip('.,!?-)\n ')
        names.append(n_el)#print(n_el)
    return names

def prints_names(n_1, n_2):
    for name in names:
        print(el)

#Задание 3
#def sentences(arr):
 #   for name in arr:
  #      res = re.findall( name, string)  


def makes_tuples():
    arr = []
    for name in names:
        a = tuple(name.split(' '))
        arr.append(a)
    return arr
        #print(a)
def makes_dicts(arr):
    d = {}
    for el in arr:
        fin = el[len(el) - 1]
        if len(el) > 2:
            beg = el[0] + el[1]
        else:
            beg = el[0]
        d[fin] = beg
    return d
    #print(d)

def makes_folders(arr):
    for el in arr:
        surn = el[len(el) - 1]
        try:
            os.makedirs(surn)
        except FileExistsError:
            continue

def m_file(d):
    direct = ''
    for key, val in d:


    

def main():
    print('Задание 1')
    print(findname1(reads_file(opens_file)))
    prints_names(find_name2(reads_file(opens_file())), find_name3(reads_file(opens_file())))
    find_name2(reads_file(opens_file()))
    find_name3(reads_file(opens_file()))
    makes_folders(makes_tuples())
if __name__ == '__main__':
    main()
