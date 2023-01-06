def rle_encoding(File_name):
    with open(File_name, 'r', encoding='UTF-8') as file, \
    open(File_name[:-4]+'_rle_enc.txt','w', encoding='UTF-8') as out:
        for item in file.readlines():
            temp = item.rstrip()
            res = ''
            count = 1
            for i in range(1, len(temp)):
                if temp[i] == temp[i - 1]:
                    count += 1
                else:
                    res += str(count) + temp[i - 1]
                    count = 1
                if i == len(temp) - 1:
                    res += str(count) + temp[i - 1]               
            print(res, file=out)

def rle_decodoing(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f, \
    open(file_name[:-4]+'_rle_dec.txt','w', encoding='UTF-8') as out:
        for item in f.readlines():
            temp = item.rstrip()
            res = ''
            count = ''
            for i in range(1, len(temp) + 1):
                if temp[i - 1].isdigit() and temp[i].isalpha():
                    count += temp[i - 1]
                    res += temp[i]*int(count)
                    count = ''
                elif temp[i - 1].isdigit() and temp[i].isdigit():
                    count += temp[i - 1]
               
            print(res, file=out)
