import os, time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from plaintext import plaintexts
import my_aes as aes

key = os.urandom(32)
iv = os.urandom(16)

cipher_cbc = Cipher(algorithms.AES(key), modes.CBC(iv))
cipher_ctr = Cipher(algorithms.AES(key), modes.CTR(iv))


def cryptography_cbc_time():
    start = time.time()
    for p in plaintexts:
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(bytes(p, 'latin-1')) + padder.finalize()
        encryptor = cipher_cbc.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        decryptor = cipher_cbc.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return time.time() - start


def my_aes_cbc_time():
    start = time.time()
    for p in plaintexts:
        _, my_ciphertext = aes.encrypt(p, key, iv, mode='CBC')
        my_plaintext = aes.decrypt(my_ciphertext, iv, key)
    return time.time() - start


print(f'Cryptography library - CBC mode: {cryptography_cbc_time()}s')
print(f'My AES-CBC Implementation: {my_aes_cbc_time()}s')


def cryptography_ctr_time():
    start = time.time()
    for p in plaintexts:
        encryptor = cipher_ctr.encryptor()
        ciphertext = encryptor.update(bytes(p, 'latin-1')) + encryptor.finalize()
        decryptor = cipher_ctr.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return time.time() - start


def my_aes_ctr_time():
    start = time.time()
    for p in plaintexts:
        _, my_ciphertext = aes.encrypt(p, key, iv, mode='CTR')
        my_plaintext = aes.decrypt(my_ciphertext, iv, key, mode='CTR')
    return time.time() - start


print(f'Cryptography library - CTR mode: {cryptography_ctr_time()}s')
print(f'My AES-CTR Implementation: {my_aes_ctr_time()}s')

