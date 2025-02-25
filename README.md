# Secure Data Hiding in Images Using Steganography & Cryptography

## Overview
This project combines **Steganography and Cryptography** to securely hide messages inside images. It ensures **confidentiality** through encryption and **integrity** through a digital signature.

## Features
- **Image Steganography**: Hides text within an image.
- **AES Encryption**: Secures hidden messages with a user-defined key.
- **Digital Signature Verification**: Ensures the message has not been tampered with.
- **User-Friendly CLI**: Simple command-line interface for encoding and decoding messages.

## Requirements
- Python 3.x
- Required Libraries: Install using
  ```sh
  pip install pillow cryptography
  ```

## How to Use
### Encoding (Hiding a Message)
1. Run the script and choose **Encode**.
2. Provide the image path.
3. Enter the secret message.
4. Set an encryption key (16-32 characters).
5. The program generates an encoded image with a hidden, encrypted message.

### Decoding (Retrieving the Message)
1. Run the script and choose **Decode**.
2. Provide the encoded image path.
3. Enter the encryption key.
4. The script verifies integrity and decrypts the message.

## Integrity Verification
After decoding, the script will confirm if the integrity check is **successful** or **failed**, ensuring the message has not been altered.

## Author
Developed by Vepada Sri Charan – Feel free to improve and explore!

## Contact
For queries or suggestions, reach out via email:- vepadasricharan@gmail.com.

