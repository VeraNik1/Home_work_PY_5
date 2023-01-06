def rle_encoding(File_name):
    with open(File_name, 'r', encoding='UTF-8') as file, \
    open(File_name[:-4]+'_rle_enc.txt','w+', encoding='UTF-8') as out:
        for item in file.readlines():
            temp = item.rstrip()
            res = ''
            for i in range(1, len(temp)):
                count = 1
                if temp[i - 1].isalpha():
                    while temp[i - 1] == temp[i]:
                        count += 1
                    res += str(count) + temp[i-1]
                else:
                    res += temp[i-1]
            print(res, file=out, end='\n')

rle_encoding("file_1.txt")