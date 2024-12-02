from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from cryptography.hazmat.primitives import serialization





def encrypt_file(input_file, public_key_path):
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes


    #load the public key

    with open(public_key_path, "r") as pub_file:
        public_key = serialization.load_pem_public_key(pub_file.read())
    
    # Read the file and encrypt
    with open(input_file, "rb") as file:
        plaintext = file.read()
    
    encrypted = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Save encrypted file
    with open(f"{input_file}.enc", "wb") as enc_file:
        enc_file.write(encrypted)

def decrypt_file(encrypted_file, private_key_path):
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes
    
    # Load private key
    with open(private_key_path, "rb") as priv_file:
        private_key = serialization.load_pem_private_key(
            priv_file.read(),
            password=None,
        )
    
    # Read encrypted file and decrypt
    with open(encrypted_file, "rb") as enc_file:
        encrypted = enc_file.read()
    
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Save decrypted file
    with open(encrypted_file.replace(".enc", "_decrypted"), "wb") as dec_file:
        dec_file.write(decrypted)

# Example usage
encrypt_file("example.txt", "public_key.pem")
decrypt_file("example.txt.enc", "private_key.pem")

