# Cài đặt AES với chế độ CBC và CTR 

- Chương trình sử dụng hàm AES của thư viện `pyaes`

## Cách sử dụng hàm AES trong thư viện `pyaes`

```python
import os
import pyaes

key_128 = os.urandom(16)
aes = pyaes.AES(key_128)

plaintext = "Hello World!!!!!"
plaintext_bytes = [ord(c) for c in plaintext]

ciphertext = aes.encrypt(plaintext_bytes)
print(repr(ciphertext))

decrypted = aes.decrypt(ciphertext)
decrypted_text = [chr(c) for c in decrypted]
print(repr(decrypted_text))
```
