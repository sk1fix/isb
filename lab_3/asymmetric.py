from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class AsymerticEncryption:
    """
    Class for asymmetric encryption
    """

    @staticmethod
    def generate_keys() -> tuple:
        """
        Generates RSA key pair.
        :return: tuple (private_key, public_key)
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048)
        return private_key, private_key.public_key()

    @staticmethod
    def encrypt_data(public_key, data: bytes) -> bytes:
        """
        Encrypts data using the public key.
        :param public_key: public RSA key for encryption
        :param data: data to encrypt
        :return: encrypted data
        """
        return public_key.encrypt(
            data,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(), label=None)
        )

    @staticmethod
    def decrypt_data(private_key, encrypted_data: bytes) -> bytes:
        """
        Decrypts data using the private key.
        :param private_key: private RSA key for decryption
        :param encrypted_data: encrypted data
        :return: decrypted data
        """
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(), label=None)
        )
