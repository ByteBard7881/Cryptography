from cryptography.fernet import Fernet

original_message = "akusdybskdeuybeskuydgbskuazdhb"
print(original_message)

# Generating Fernet Key
key = Fernet.generate_key()

with open('./key.txt', 'wb') as file:
    file.write(key)

fnt = Fernet(key)

encrypted_message = fnt.encrypt(original_message.encode())
print(encrypted_message)

decrypted_message = fnt.decrypt(encrypted_message.decode())
print(decrypted_message)