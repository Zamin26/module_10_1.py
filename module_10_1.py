import time
from time import sleep
from threading import Thread # для запуска потоков


time_start = time.time()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)  # пауза с прерыванием после записи каждого слова на 0.1 секунду
        print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = time.time() # окончательное время
print(f'Работа потоков {time_end - time_start}') # затраченное время
print()

time_start = time.time() # начальное время

# активация потоков
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

# запуск потоков
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# остановка между потоками
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end = time.time() # окончательное время
print(f'Работа потоков {time_end - time_start}')