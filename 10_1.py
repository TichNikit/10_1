from threading import Thread
from time import sleep

def wite_words(word_count, file_name, word):
    with open(file_name, 'w', encoding='UTF-8') as fi:
        for item in range(1, word_count+1):
            fi.write(f'Слово {word} №{item}')
            fi.write('\n')
            sleep(0.1)

wite_words(10, 'example1.txt', '"Word 1"')
wite_words(30, 'example2.txt', '"Word 2"')
wite_words(200, 'example3.txt', '"Word 3"')
wite_words(100, 'example4.txt', '"Word 4"')

file_one = Thread(target=wite_words(10, 'example5.txt', '"Word 5"'))
file_two = Thread(target=wite_words(30, 'example6.txt','"Word 6"'))
file_three = Thread(target=wite_words(200, 'example7.txt', '"Word 7"'))
file_four = Thread(target=wite_words(100, 'example8.txt', '"Word 8"'))

file_one.start()
file_two.start()
file_three.start()
file_four.start()

file_one.join()
file_two.join()
file_three.join()
file_four.join()
