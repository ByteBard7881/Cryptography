import rsa

directory = "./Asymmetric Exercise 1/"

# Creating public and private keys
public_key, private_key = rsa.newkeys(4096)

with open(directory+"public.pem", "wb") as file:
    file.write(public_key.save_pkcs1("PEM"))

with open(directory+"private.pem", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))


# Reading private and public keys
with open(directory+"public.pem", "rb") as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())

with open(directory+"private.pem", "rb") as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

print(private_key)
print("\n \n")
print(public_key)

# Encryption
original_message = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

with open(directory+"data.txt", "wb") as file:
    file.write(original_message.encode())
    
def split_into_chunks(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

max_chunk_size = 501

with open(directory+"data.txt", "rb") as file:
    data = file.read()

# print(data)

message_chunks = split_into_chunks(data, max_chunk_size)

encrypted_chunks = []
for chunk in message_chunks:
    encrypted_chunk = rsa.encrypt(chunk, public_key)
    encrypted_chunks.append(encrypted_chunk)

with open(directory+"encrypted_data.txt", "wb") as file:
    for chunk in encrypted_chunks:
        file.write(chunk)
    
print("Encryption complete!")

# Decryption
with open(directory+"encrypted_data.txt", "rb") as file:
    encrypted_data = file.read()
    
chunk_size = 512

def split_encrypted_data(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

encrypted_chunks = split_encrypted_data(encrypted_data, chunk_size)

decrypted_chunks = []
for chunk in encrypted_chunks:
    decrypted_chunk = rsa.decrypt(chunk, private_key)
    decrypted_chunks.append(decrypted_chunk)

decrypted_message = b''.join(decrypted_chunks)

with open(directory+"decrypted_data.txt", "wb") as file:
    file.write(decrypted_message)

print("Decryption complete!")