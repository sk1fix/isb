import json


def reading_files(path: str) -> str:
    '''
        The function reads the text from the file
    '''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('No such file or directory')


def write_to_file(path: str, text: str) -> None:
    '''
        The function writes text to a file
    '''
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(text)
    except IOError:
        print('All bad')


def read_key(path: str) -> dict:
    '''
        The function reads the key from the json file
    '''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('No such file or directory')


def frequency_analysis(read_path: str, write_path: str) -> None:
    key = {}
    k = 0
    a = []
    read_file=reading_files(read_path)
    
    for line in read_file:
        temp = ''
        for i in line:
            try:
                key[i] += 1
            except:
                key[i] = 0
            k += 1
    for i in key:
        a.append([str(i), key[i]/k])
    sorted_data = sorted(a, key=lambda x: x[1], reverse=True)
    for i in sorted_data:
        write_to_file(write_path,f"{i[0]} : {str(i[1])}\n")
    

