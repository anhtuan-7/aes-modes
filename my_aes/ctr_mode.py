# -*- coding: utf-8 -*-
import os, math
import pyaes
from my_aes.utils import int_xor, txt


def encrypt_ctr_mode(plaintext, key, iv=None):
    iv = iv or os.urandom(16)
    aes = pyaes.AES(key)
    ciphertext = []

    iv_bytes = iv
    iv_int = int.from_bytes(iv, "big")

    number_of_blocks = math.ceil(len(plaintext) / 16)
    for i in range(0, number_of_blocks):
        block = [ord(c) for c in plaintext[i*16:(i*16+16)]]
        f = aes.encrypt(iv_bytes)
        ciphertext.append(int_xor(block, f))
        iv_int += 1
        iv_bytes = iv_int.to_bytes(16, "big")

    ciphertext_string = ""
    for c in ciphertext:
        ciphertext_string += "".join([chr(k) for k in c])

    return iv, bytes(ciphertext_string, encoding="latin-1")


def decrypt_ctr_mode(ciphertext, iv, key):
    aes = pyaes.AES(key)
    plaintext = ""

    iv_bytes = iv
    iv_int = int.from_bytes(iv, "big")

    for i in range(0, math.ceil(len(ciphertext)/16)):
        f = aes.encrypt(iv_bytes)
        plaintext += "".join([chr(c) for c in int_xor(ciphertext[i*16:i*16+16], f)])
        iv_int += 1
        iv_bytes = iv_int.to_bytes(16, "big")

    return plaintext


if __name__ == "__main__":
    my_key = os.urandom(16)
    i1, c1 = encrypt_ctr_mode(txt, my_key)
    print(i1)
    print(c1)
    print(decrypt_ctr_mode(c1, i1, my_key))

