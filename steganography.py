import os
import base64
import hashlib
import hmac
from cryptography.fernet import Fernet
from PIL import Image

# Function to generate a Fernet key from user input
def get_key(user_key):
    return base64.urlsafe_b64encode(user_key.ljust(32).encode())

# Generate a digital signature using HMAC-SHA256
def generate_signature(data, key):
    return hmac.new(get_key(key), data, hashlib.sha256).digest()

# Encrypt message and generate a digital signature
def encrypt_message(message, key):
    cipher = Fernet(get_key(key))
    encrypted_message = cipher.encrypt(message.encode())
    signature = generate_signature(encrypted_message, key)
    return encrypted_message, signature

# Decrypt message and verify digital signature
def decrypt_message(encrypted_message, received_signature, key):
    expected_signature = generate_signature(encrypted_message, key)

    # Integrity check
    if hmac.compare_digest(expected_signature, received_signature):
        try:
            cipher = Fernet(get_key(key))
            decrypted_message = cipher.decrypt(encrypted_message).decode()
            return decrypted_message, "✅ Integrity Check Passed"
        except Exception:
            return "❌ ERROR: Decryption failed!", "❌ Integrity Check Failed"
    else:
        return "❌ ERROR: Integrity check failed! Message may have been altered.", "❌ Integrity Check Failed"

# Encode secret message inside an image
def encode_image(image_path, secret_text, key, output_path="encoded_image.png"):
    img = Image.open(image_path).convert("RGBA")  # Convert to RGBA to handle all image types
    pixels = img.load()

    # Encrypt message and get signature
    encrypted_message, signature = encrypt_message(secret_text, key)
    combined_data = encrypted_message + signature  # Append signature at the end
    binary_text = ''.join(format(byte, '08b') for byte in combined_data) + '1111111111111110'  # End delimiter

    width, height = img.size
    binary_index = 0

    for y in range(height):
        for x in range(width):
            if binary_index < len(binary_text):
                pixel = list(pixels[x, y])  # Convert to list to modify
                pixel[0] = (pixel[0] & 0b11111110) | int(binary_text[binary_index])  # Modify LSB of red channel
                binary_index += 1
                pixels[x, y] = tuple(pixel)  # Convert back to tuple
            else:
                break
        else:
            continue
        break

    img.save(output_path)
    print(f"✅ Message successfully hidden in '{output_path}'.")

# Decode the hidden message from an image
def decode_image(image_path, key):
    img = Image.open(image_path).convert("RGBA")  # Convert to RGBA
    pixels = img.load()

    width, height = img.size
    binary_text = ""

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            binary_text += str(pixel[0] & 1)  # Extract LSB of red channel

            # Stop if the delimiter is found
            if binary_text.endswith('1111111111111110'):
                binary_text = binary_text[:-16]  # Remove delimiter
                break
        else:
            continue
        break

    # Convert binary back to bytes
    byte_array = bytearray(int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8))

    # Extract encrypted message and signature
    encrypted_message = byte_array[:-32]  # Extract encrypted message
    signature = byte_array[-32:]  # Extract signature

    # Decrypt and verify integrity
    decrypted_message, integrity_status = decrypt_message(bytes(encrypted_message), bytes(signature), key)
    
    print(f"\n🔍 {integrity_status}")
    return decrypted_message

# Main Program
if __name__ == "__main__":
    choice = input("Do you want to (E)ncode or (D)ecode? ").strip().upper()

    if choice == "E":
        image_path = input("Enter the path of the image to hide the message: ").strip()
        secret_message = input("Enter the secret message to hide: ").strip()
        key = input("Enter the encryption key (16-32 characters): ").strip()

        if len(key) < 16 or len(key) > 32:
            print("❌ ERROR: Key must be between 16 and 32 characters!")
        else:
            encode_image(image_path, secret_message, key)
            decode_option = input("Do you want to decode the message now? (yes/no): ").strip().lower()
            if decode_option == "yes":
                print("Decoded Message:", decode_image("encoded_image.png", key))

    elif choice == "D":
        encoded_image_path = input("Enter the path of the encoded image: ").strip()
        key = input("Enter the decryption key: ").strip()
        print("Decoded Message:", decode_image(encoded_image_path, key))

    else:
        print("❌ ERROR: Invalid option. Please enter 'E' to encode or 'D' to decode.")
