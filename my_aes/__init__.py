# -*- coding: utf-8 -*-

from my_aes.cbc_mode import encrypt_cbc_mode, decrypt_cbc_mode
from my_aes.ctr_mode import encrypt_ctr_mode, decrypt_ctr_mode


def encrypt(plaintext, key, iv=None, mode='CBC'):
    valid_mode = ['CBC', 'CTR']
    valid_key_length = [16, 24, 32]

    if mode not in valid_mode:
        raise ValueError('Invalid mode')

    if len(key) not in valid_key_length:
        raise ValueError('Invalid key length')

    if mode == 'CBC':
        iv, ciphertext = encrypt_cbc_mode(plaintext, key, iv)
    else:
        iv, ciphertext = encrypt_ctr_mode(plaintext, key, iv)

    return iv, ciphertext


def decrypt(ciphertext, iv, key, mode='CBC'):
    valid_mode = ['CBC', 'CTR']
    valid_key_length = [16, 24, 32]

    if mode not in valid_mode:
        raise ValueError('Invalid mode')

    if len(key) not in valid_key_length:
        raise ValueError('Invalid key length')

    if mode == 'CBC':
        return decrypt_cbc_mode(ciphertext, iv, key)
    return decrypt_ctr_mode(ciphertext, iv, key)
