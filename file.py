"""
Домашнее задание №2
Работа с файлами
* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        length = 0
        ammount_of_words = 0
        for line in f:
            line = line.replace('.', '!')
            length += len(line)
            ammount_of_words += len(line.split())
            with open('referat2.txt', 'a', encoding='utf-8') as f2:
                f2.write(line)
                pass
        print(f"\nLength of the string is {length} symbols.")
        print(f"There are {ammount_of_words} words in this text.")
        

if __name__ == "__main__":
    main()