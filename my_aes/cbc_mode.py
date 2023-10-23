import os, math
import pyaes
from my_aes.utils import pkcs7_padding, pkcs7_unpadding, int_xor, txt


def encrypt_cbc_mode(plaintext, key, iv=None):
    iv = iv or os.urandom(16)
    aes = pyaes.AES(key)
    ciphertext = []

    # Padding
    plaintext_pad = pkcs7_padding(plaintext)
    plaintext_pad_bytes = [ord(c) for c in plaintext_pad]
    number_of_blocks = int(len(plaintext_pad) / 16)

    # CBC Block[0]
    c0 = aes.encrypt(int_xor(plaintext_pad_bytes[0:16], iv))
    ciphertext.append(c0)

    # CBC
    for i in range(1, number_of_blocks):
        block = plaintext_pad_bytes[i*16: (i*16 + 16)]
        c = aes.encrypt(int_xor(block, ciphertext[i-1]))
        ciphertext.append(c)

    ciphertext_string = ""
    for c in ciphertext:
        ciphertext_string += "".join([chr(k) for k in c])

    return iv, bytes(ciphertext_string, encoding="latin-1")


def decrypt_cbc_mode(ciphertext, iv, key):
    aes = pyaes.AES(key)
    plaintext = ""

    # Block[0]
    block = ciphertext[0:16]
    decrypted = int_xor(aes.decrypt(block), iv)
    decrypted_text = [chr(c) for c in decrypted]
    plaintext += "".join(decrypted_text)

    # Other Blocks
    for i in range(1, math.ceil(len(ciphertext)/16)):
        prev_block = ciphertext[(i*16-16):i*16]
        current_block = ciphertext[i*16:(i*16+16)]
        decrypted = int_xor(aes.decrypt(current_block),prev_block)
        decrypted_text = [chr(c) for c in decrypted]
        plaintext += "".join(decrypted_text)

    return pkcs7_unpadding(plaintext)


if __name__ == "__main__" :
    my_key = os.urandom(16)  # 128 bits
    i1, c1 = encrypt_cbc_mode(txt, my_key)
    print(i1)
    print(c1)
    print(decrypt_cbc_mode(c1, i1, my_key))
