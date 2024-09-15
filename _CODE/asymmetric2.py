import rsa

directory = "./Asymmetric Exercise 2/"

# Creating private and public keys
public_key, private_key = rsa.newkeys(4096)

with open(directory+"public.pem", "wb") as file:
    file.write(public_key.save_pkcs1("PEM"))

with open(directory+"private.pem", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))
    
# Reading private and public keys
with open(directory+"public.pem", "rb") as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())
    
with open(directory+"private.pem", "rb") as file:
    public_key = rsa.PrivateKey.load_pkcs1(file.read())
    
# Signing the private key
sign_message = "Blue bird is the red tree"
signature = rsa.sign(sign_message.encode(), private_key, "SHA-256")

# Save the signature
with open(directory+"signature", "wb") as file:
    file.write(signature)
    
# Verify the signature
print(rsa.verify(sign_message.encode(), signature, public_key))