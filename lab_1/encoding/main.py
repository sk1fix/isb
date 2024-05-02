from functions import read_key, reading_files, write_to_file
import paths


def encryption(path: str) -> None:
    key = read_key(paths.KEY_ENCODING)
    file=reading_files(path)
    for line in file:
        temp=''
        for i in line:
            if i in key:
                temp+=key[i]
            else:
                temp+=i
        write_to_file(paths.DECODING_RESULT)


if __name__ == "__main__":
    encryption(paths.BEGINING_DECODING_TXT)
