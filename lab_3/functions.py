import json


class Func:
    @staticmethod
    def read_json(file_path: str) -> dict:
        """
        Reads JSON data from a file.
        :param file_path: path to the JSON file
        :return: dictionary with data
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path: str, data: dict) -> None:
        """
        Writes JSON data to a file.
        :param file_path: path to the JSON file
        :param data: dictionary with data to write
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        """
        Reads data from a file as bytes.
        :param file_path: path to the file
        :return: file data as bytes
        """
        with open(file_path, 'rb') as file:
            return file.read()

    @staticmethod
    def write_bytes(file_path: str, data: bytes) -> None:
        """
        Writes data to a file as bytes.
        :param file_path: path to the file
        :param data: bytes to write
        """
        with open(file_path, 'wb') as file:
            file.write(data)
