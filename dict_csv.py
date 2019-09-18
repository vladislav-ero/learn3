"""
Домашнее задание №2
Работа csv
* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv
"""
import csv

def main():
    people_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]
    with open('people.csv','w', encoding='UTF-8') as c:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(c, fields, delimiter=';')
        writer.writeheader()
        for person in people_list:
            writer.writerow(person)



if __name__ == "__main__":
    main()