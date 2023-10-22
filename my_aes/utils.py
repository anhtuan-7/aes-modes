# -*- coding: utf-8 -*-
import math

txt = "The Advanced Encryption Standard (AES), also known by its original name Rijndael, " \
            "is a specification for the encryption of electronic data established by " \
            "the U.S. National Institute of Standards and Technology (NIST) in 2001."


def int_xor(array_1, array_2):
    result = []
    l1 = len(array_1)
    l2 = len(array_2)

    if l1 < l2:
        for i in range(0, l1):
            result.append(array_1[i] ^ array_2[i])
    else:
        for i in range(0, l2):
            result.append(array_1[i] ^ array_2[i])

    return result


def pkcs7_padding(text, block_size=16):
    # padding = x01 -> x10 (1 -> 16)
    padding = block_size - len(text) % block_size

    padding_char = ""
    for c in range(0, padding):
        padding_char = padding_char + chr(padding)

    padded_text = text + padding_char
    return padded_text


def pkcs7_unpadding(text, block_size=16):
    padding = ord(text[-1])
    return text[:-padding]



