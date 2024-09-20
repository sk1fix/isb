import logging

from typing import Union

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class AsymerticEncryption:
    """
    Class for asymmetric encryption
    """
    private_key = None
    public_key = None
    public_key_path = None
    private_key_path = None
    
    @staticmethod
    def generate_keys(self):
        """
        Generates keys for asymmetric encrytpion
        :param length: length of key
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()

    @staticmethod
    def encrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Encrypts a data using asymmetric algorithm
        :param key: public key in bytes for asymmetric encrytpion
        :param data: data for asymmetric encryption
        :return: encoded data, None if error
        """

        return key.encrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    @staticmethod
    def decrypt_data(key: bytes, data: bytes) -> Union[bytes, None]:
        """
        Decrypts a data using asymmetric algorithm
        :param key: private key in bytes for decrypting
        :param data: encrypted data
        :return: decrypted data, None if error
        """

        return key.decrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
