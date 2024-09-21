import argparse

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from asymmetric import AsymerticEncryption
from symmetric import SymmetricEncryption
from functions import Func
import path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encrypt/decrypt text using AsymerticEncryption and SymmetricEncryption algorithms.")
    parser.add_argument("variants", choices=["key_gen", "encryption", "decryption"],
                        help="Operation mode: key_gen, encryption, decryption.")
    args = parser.parse_args()

    settings = Func.read_json(path.PATH)

    def key_gen() -> None:
        """
        Generates AsymerticEncryption key pair and SymmetricEncryption symmetric key, and saves them to designated Funcs.
        """
        symmetric_key = SymmetricEncryption.generate_key(192)
        private_key, public_key = AsymerticEncryption.generate_keys()

        Func.write_bytes(settings["private_key"], private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
        Func.write_bytes(settings["public_key"], public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
        Func.write_bytes(settings["symmetric_key"], AsymerticEncryption.encrypt_data(
            public_key, symmetric_key))

        print("Keys were generated")

    def encryption():
        """
        Encrypts text using AsymerticEncryption and SymmetricEncryption algorithms.
        """
        initial_text = Func.read_bytes(settings["initial_file"])
        symmetric_key_encrypted = Func.read_bytes(settings["symmetric_key"])
        private_key = serialization.load_pem_private_key(
            Func.read_bytes(settings["private_key"]),
            password=None
        )

        symmetric_key = AsymerticEncryption.decrypt_data(
            private_key, symmetric_key_encrypted)
        encrypted_text = SymmetricEncryption.encrypt_data(
            symmetric_key, initial_text.decode('utf-8'))
        Func.write_bytes(settings["encrypted_file"], encrypted_text)

        print("Text encrypted")

    def decryption() -> None:
        """
        Decrypts encrypted text using AsymerticEncryption and SymmetricEncryption algorithms.
        """
        encrypted_text = Func.read_bytes(settings["encrypted_file"])
        symmetric_key_encrypted = Func.read_bytes(settings["symmetric_key"])
        private_key = serialization.load_pem_private_key(
            Func.read_bytes(settings["private_key"]),
            password=None
        )

        symmetric_key = AsymerticEncryption.decrypt_data(
            private_key, symmetric_key_encrypted)
        decrypted_text = SymmetricEncryption.decrypt_data(
            symmetric_key, encrypted_text)
        Func.write_bytes(settings["decrypted_file"],
                         decrypted_text.encode('utf-8'))

        print("Text decrypted")

    match args.variants:
        case "key_gen":
            key_gen()
        case "encryption":
            encryption()
        case "decryption":
            decryption()
        case _:
            print("Unknown mode")


if __name__ == "__main__":
    main()
