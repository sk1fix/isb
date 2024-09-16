import json


def read_json(path: str) -> dict:
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
