# Cryptography Exercises

This repository contains various cryptographic exercises demonstrating symmetric encryption with the Fernet algorithm and asymmetric encryption/signing using Rivest-Shamir-Adleman(RSA) algorithm.

## Directory Structure
```markdown
_CODE/
  Asymmetric Exercise 1/
    data.txt
    decrypted_data.txt
    encrypted_data.txt
    private.pem
    public.pem
  Asymmetric Exercise 2/
    private.pem
    public.pem
    signature
  asymmetric1.py
  asymmetric2.py
  symmetric.py
```

## Overview

- `symmetric.py`: Demonstrates symmetric encryption using the `Fernet` module from the `cryptography` library.
- `asymmetric1.py`: Shows how to generate RSA keys, encrypt/decrypt a large message in chunks, and save the results to files.
- `asymmetric2.py`: Demonstrates RSA key generation, signing a message, and verifying the signature.

### Dependencies

- `cryptography`: For symmetric encryption.
- `rsa`: For RSA encryption and signing.

### How to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/ByteBard7881/Cryptography.git
   cd Cryptography
   ```

2. Install the required dependencies:
   ```bash
   pip install cryptography rsa
   ```

### How to Run

#### Symmetric Encryption

1. Run `symmetric.py` to encrypt and decrypt a message using Fernet:
   ```bash
   python symmetric.py
   ```
   
   This script will generate a key, encrypt a message, save the key in `key.txt`, and print the original, encrypted, and decrypted messages.

#### Asymmetric Encryption (Exercise 1)

1. Run `asymmetric1.py` to perform RSA encryption and decryption:
   ```bash
   python asymmetric1.py
   ```
   
   This script will:
   - Generate RSA keys (4096 bits) and save them as `public.pem` and `private.pem`.
   - Encrypt a large message by splitting it into chunks and save the encrypted data in `encrypted_data.txt`.
   - Decrypt the message and save the result in `decrypted_data.txt`.

#### Asymmetric Signing and Verification (Exercise 2)

1. Run `asymmetric2.py` to sign and verify a message:
   ```bash
   python asymmetric2.py
   ```

   This script will:
   - Generate RSA keys (4096 bits) and save them as `public.pem` and `private.pem`.
   - Sign a message and save the signature.
   - Verify the signature using the public key.

### File Descriptions

- **Asymmetric Exercise 1**:
  - `data.txt`: Contains the original message.
  - `encrypted_data.txt`: Contains the encrypted message.
  - `decrypted_data.txt`: Contains the decrypted message.
  - `public.pem`: RSA public key.
  - `private.pem`: RSA private key.

- **Asymmetric Exercise 2**:
  - `public.pem`: RSA public key.
  - `private.pem`: RSA private key.
  - `signature`: Contains the signed message.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments

- [Cryptography Library](https://cryptography.io)
- [Python-RSA Library](https://stuvel.eu/rsa)
```