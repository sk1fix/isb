def frequency_analysis(path):
    key={}
    k=0
    a=[]
    with open('D:/Ycheba/isb/lab_1/decoding/decod.txt','w+',encoding='UTF-8') as wr:
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                for line in file:
                    temp = ''
                    line = line.strip()
                    for i in line:
                        try:
                            key[i]+=1
                        except:
                            key[i]=0
                        k+=1
                for i in key:
                    a.append([str(i), key[i]/k])
                sorted_data = sorted(a, key=lambda x: x[1], reverse=True)
                for i in sorted_data:
                    wr.write(i[0] + ' : ' + str(i[1]) + '\n')
        except:
            print('No such file or directory')

def get_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None
    
def decoding(path) -> None:
    key = {' ': '2', 'е': 'К', 'о': 'Ь', 'и': 't', 'н': 'Ы', 'в': 'r', 'а': 'Д', 'с': '>', 'т': 'О', 'м': '<', 'д': 'Б', 'к': 'Й', 'п': 'Я',
       'я': '1', 'л': 'Ч', 'р': ' ', 'з': 'М', 'у': '0', 'ю': 'Х', 'г': 'А', 'ч': 'a', 'ж': 'Л', 'ы': '8', 'б': 'Е', 'щ': 'c', 'х': '3',
       'ь': ',', 'ф': '.', 'ш': 'b', 'ц': '9', 'э': 'Ф', 'й': '?'}

    with open(path, 'r', encoding='UTF-8') as write_f:
        with open('D:/Ycheba/isb/lab_1/decoding/decoded.txt', 'w+', encoding='UTF-8') as file:
            for line in write_f:
                temp = ''
                line = line.strip()
                for i in line:
                    if get_key_by_value(key, i):
                        temp += get_key_by_value(key, i)
                    else:
                        temp += str(i)
                file.write(temp + '\n')


def main():
    frequency_analysis('D:/Ycheba/isb/lab_1/decoding/code1.txt')
    decoding('D:/Ycheba/isb/lab_1/decoding/code1.txt')


if __name__ == "__main__":
    main()