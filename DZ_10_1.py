import time
from time import sleep
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №  {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    return f'Завершилась запись в файл {file_name}'

time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
print(f'1.Работа без потоков: {time_end - time_start}')

th_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

time_start = time.time()
th_1.start()
th_2.start()
th_3.start()
th_4.start()

th_1.join()
th_2.join()
th_3.join()
th_4.join()
time_end = time.time()
print(f'2.Работа потоков: {time_end - time_start}')

