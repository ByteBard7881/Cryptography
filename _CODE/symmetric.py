from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_AES(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    cipher_text, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    return cipher_text, tag, nonce

def decrypt_AES(key, nonce, cipher_text, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data =  cipher.decrypt_and_verify(cipher_text, tag)
    return data

data = b'secret data'
key = get_random_bytes(32)

print(f"Key: {key}")
cipher_text, tag, nonce = encrypt_AES(key, data)
print(f"Cipher text: {cipher_text}\n" + f"Tag: {tag}\n" + f"Nonce: {nonce}")

data = decrypt_AES(key, nonce, cipher_text, tag)
print(f"Data: {data}")