import json
import paths


def reading_files(path: str) -> str:
    """function that can read data from .txt file

    Args:
        path (str): path to file

    Returns:
        str: what the file contains
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('No such file or directory')


def write_to_file(path: str, text: str) -> None:
    """function that can write data to .txt file

    Args:
        path (str): path to file
        text (str): what we need to write in file
    """
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(text)
    except IOError:
        print('All bad')


def read_key(path: str) -> dict:
    '''
        The function reads the key from the json file
    Args:
        path (str): path to file
    '''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('No such file or directory')


def frequency_analysis(read_path: str, write_path: str) -> None:
    """function of calculation frequency in text

    Args:
        read_path (str): file with original text

    """
    key = {}
    k = 0
    a = []
    read_file = reading_files(read_path)

    for line in read_file:
        temp = ''
        for i in line:
            if i in key:
                key[i] += 1
            else:
                key[i] = 0
            k += 1
    for i in key:
        a.append([str(i), key[i]/k])
    sorted_data = sorted(a, key=lambda x: x[1], reverse=True)
    for i in sorted_data:
        write_to_file(write_path, f"{i[0]} : {str(i[1])}\n")


def encryption(path: str) -> None:
    """function that encrypts text

    Args:
        path (str): file with original text

    """
    key = read_key(paths.KEY_ENCODING)
    file = reading_files(path)
    for line in file:
        temp = ''
        for i in line:
            if i in key:
                temp += key[i]
            else:
                temp += i
        write_to_file(paths.DECODING_RESULT, temp)


def decoding(path: str) -> None:
    """function that decrypts text

    Args:
        path (str): file with original text

    """
    key = read_key(paths.KEY_DECODING)
    file = reading_files(path)
    for line in file:
        temp = ''
        for i in line:
            if i in key:
                temp += key[i]
            else:
                temp += i
        write_to_file(paths.ENCODING_RESULT, temp)


if __name__ == "__main__":
    encryption(paths.BEGINING_DECODING_TXT)
    frequency_analysis(paths.BEGINING_ENCODING_TXT, paths.FREQUENCY_RESULT)
    decoding(paths.BEGINING_ENCODING_TXT)
