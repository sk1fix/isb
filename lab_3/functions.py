import json


class Func:
    """
    A class for working with files, reading data from them and writing
    """
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

    def write_bytes_text(path: str, bytes_text: bytes) -> None:
        """function that can write binary data to file

        Args:
            path (str): path to file
            text (str): what we need to write in file
        """
        try:
            with open(path, "wb") as file:
                file.write(bytes_text)
        except FileNotFoundError:
            print("The file was not found")

    def read_txt(path: str) -> dict:
        '''
            The function reads the text from file
        Args:
            path (str): path to file
        '''
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
