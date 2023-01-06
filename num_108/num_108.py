# **Задача 108** Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).

from rle import rle_encoding as enc, rle_decodoing as dec
enc('num_108\\file_1.txt')
dec('num_108\\file_1_rle_enc.txt')
import os
inputstats = os.stat('num_108\\file_1.txt')
outstats = os.stat('num_108\\file_1_rle_enc.txt')
inputsize = inputstats.st_size
outputsize = outstats.st_size
print('Степень сжатия', round(outputsize / inputsize, 3)) 