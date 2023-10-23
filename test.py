# Checking if my encryption mode was implemented correctly
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

import my_aes as aes

test = True

plaintexts = [
    "AES is a variant of the Rijndael block cipher developed by two Belgian cryptographers, "
    "Joan Daemen and Vincent Rijmen, who submitted a proposal to NIST during the AES selection process.",
    "Rijndael is a family of ciphers with different key and block sizes.",
    "For AES, NIST selected three members of the Rijndael family, each with a block size of 128 bits, "
    "but three different key lengths: 128, 192 and 256 bits."
]

key = os.urandom(16)
iv = os.urandom(16)

cipher_cbc = Cipher(algorithms.AES(key), modes.CBC(iv))
cipher_ctr = Cipher(algorithms.AES(key), modes.CTR(iv))

# CBC Encrypt
for p in plaintexts:
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(bytes(p, 'latin-1')) + padder.finalize()
    encryptor = cipher_cbc.encryptor()
    correct_aes_ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    _, my_ciphertext = aes.encrypt(p, key, iv, mode='CBC')

    if my_ciphertext != correct_aes_ciphertext:
        test = False


# CBC Decrypt
for p in plaintexts:
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(bytes(p, 'latin-1')) + padder.finalize()
    encryptor = cipher_cbc.encryptor()
    correct_aes_ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    my_plaintext = aes.decrypt(correct_aes_ciphertext, iv, key)
    if my_plaintext != p:
        test = False

# CTR Encrypt
for p in plaintexts:
    encryptor = cipher_ctr.encryptor()
    correct_aes_ciphertext = encryptor.update(bytes(p, 'latin-1')) + encryptor.finalize()

    _, my_ciphertext = aes.encrypt(p, key, iv, mode='CTR')
    if my_ciphertext != correct_aes_ciphertext:
        test = False

# CTR Decrypt
for p in plaintexts:
    encryptor = cipher_ctr.encryptor()
    correct_aes_ciphertext = encryptor.update(bytes(p, 'latin-1')) + encryptor.finalize()

    my_plaintext = aes.decrypt(correct_aes_ciphertext, iv, key, mode='CTR')
    if my_plaintext != p:
        test = False

if test is True:
    print("Encryption mode was implemented correctly")
