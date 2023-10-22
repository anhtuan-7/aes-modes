# -*- coding: utf-8 -*-

from my_aes.cbc_mode import encrypt_cbc_mode, decrypt_cbc_mode
from my_aes.ctr_mode import encrypt_ctr_mode, decrypt_ctr_mode


def encrypt(plaintext, key, iv=None, mode='CBC'):
    valid_mode = ['CBC', 'CTR']
    if mode not in valid_mode:
        raise ValueError('Invalid mode or output format')

    if mode == 'CBC':
        iv, ciphertext = encrypt_cbc_mode(plaintext, key, iv)
    else:
        iv, ciphertext = encrypt_ctr_mode(plaintext, key, iv)

    return iv, ciphertext


def decrypt(ciphertext, iv, key, mode='CBC'):
    valid_mode = ['CBC', 'CTR']
    if mode not in valid_mode:
        raise ValueError('Invalid mode')

    if mode == 'CBC':
        return decrypt_cbc_mode(ciphertext, iv, key)
    return decrypt_ctr_mode(ciphertext, iv, key)
