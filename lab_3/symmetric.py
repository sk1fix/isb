import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryption:
    ENCODING = 'UTF-8'

    @staticmethod
    def generate_key(length: int) -> bytes:
        """
        Generates a symmetric key.
        :param length: length of key (128, 192, 256 bits)
        :return: generated key
        """
        if length not in [128, 192, 256]:
            raise ValueError(
                "Invalid key length: must be 128, 192, or 256 bits.")
        return os.urandom(length // 8)

    @staticmethod
    def encrypt_data(key: bytes, data: str) -> bytes:
        """
        Encrypts data using AES symmetric encryption.
        :param key: symmetric key
        :param data: data to encrypt
        :return: encrypted data
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        data_bytes = data.encode(SymmetricEncryption.ENCODING)
        padded_data = padder.update(data_bytes) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    @staticmethod
    def decrypt_data(key: bytes, encrypted_data: bytes) -> str:
        """
        Decrypts data that was encrypted with AES symmetric encryption.
        :param key: symmetric key
        :param encrypted_data: encrypted data
        :return: decrypted data as a string
        """
        iv = encrypted_data[:16]
        actual_ciphertext = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_padded_data = decryptor.update(
            actual_ciphertext) + decryptor.finalize()
        plaintext_bytes = unpadder.update(
            decrypted_padded_data) + unpadder.finalize()

        return plaintext_bytes.decode(SymmetricEncryption.ENCODING)
