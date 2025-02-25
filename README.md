🔐 Secure Image Steganography with Encryption & Digital Signature


📌 Project Overview
This project integrates Steganography, Cryptography, and Digital Signature Verification to provide secure data hiding in images. By combining AES encryption with LSB-based image steganography, the message remains confidential and tamper-proof, ensuring authenticity and security.

🚀 Features

✅ AES Encryption – Secures the message before hiding it in an image.

✅ LSB Steganography – Uses Least Significant Bit (LSB) technique for data hiding.

✅ Digital Signature – Ensures message integrity and prevents tampering.

✅ Authenticity Check – Verifies if the extracted message is unaltered.

✅ User-Friendly – Simple CLI-based interaction.

🛠️ Technologies Used
Programming Language: Python
Libraries Used:
PIL – For image processing
cryptography – For AES encryption
hashlib – For digital signature verification
os – For file handling
📂 How to Use the Code (Step-by-Step)
🔹 Setup & Installation

1️⃣ Install required dependencies:
bash
Copy
Edit
pip install pillow cryptography
2️⃣ Place the image you want to encode in the same folder as the script.

3️⃣ Ensure your encryption key is exactly 16, 24, or 32 characters long.

🔹 Encoding (Hiding a Secret Message)

1️⃣ Run the script:
bash
Copy
Edit
python newstego.py
2️⃣ Select (E) Encode when prompted.

3️⃣ Enter the image file name (e.g., input.png).

4️⃣ Type the secret message you want to hide.

5️⃣ Enter a secure encryption key (16, 24, or 32 characters long).

6️⃣ The program will create an encoded image (output.png) with the hidden message.

🔹 Decoding (Extracting the Hidden Message)

1️⃣ Run the script again:
bash
Copy
Edit
python newstego.py
2️⃣ Select (D) Decode when prompted.

3️⃣ Enter the encoded image file name (e.g., output.png).

4️⃣ Provide the correct decryption key (same key used during encoding).

5️⃣ If the key is correct, the hidden message will be displayed.

6️⃣ The integrity check will confirm whether the message is authentic or tampered with.

📌 Example
Encoding Process:
bash
Copy
Edit
Do you want to (E)ncode or (D)ecode? E
Enter the path of the image to hide the message: input.png
Enter the secret message to hide: Hello, World!
Enter the encryption key (16, 24, or 32 characters): SecureKey123456
Message successfully hidden in output.png
Decoding Process:
bash
Copy
Edit
Do you want to (E)ncode or (D)ecode? D
Enter the path of the encoded image: output.png
Enter the decryption key: SecureKey123456
Extracted Message: Hello, World!
Integrity Check: ✅ Message is authentic.
📌 Future Enhancements
Support for audio & video steganography
Cloud-based encoding/decoding
AI-powered steganalysis resistance
💡 Notes:
Do not modify the encoded image after encoding; it may corrupt the hidden message.
If you enter an incorrect decryption key, you won't get the correct message.
The integrity check ensures authenticity by verifying the digital signature.
