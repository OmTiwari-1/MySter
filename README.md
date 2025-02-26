Secure Data Hiding in Images Using Steganography


📌 Project Overview


This project implements a simple steganography technique to hide a secret message inside an image. The message is encrypted into the image using pixel values, making it difficult to detect. The encrypted image can then be shared securely, and only authorized users with the correct passcode can decrypt and retrieve the hidden message.


🚀 Features


Hide a secret message inside an image.
Encrypt and save the image with the hidden message.
Retrieve and decrypt the hidden message from the image.
Password protection for added security.


📂 Project Structure


📁 Secure-Image-Steganography
├── encoder.py              # Encrypts the message into the image
├── decoder.py              # Decrypts the message from the image
├── mypic.jpg               # pic used in this code
├── README.md               # Project documentation



🛠 Installation
Prerequisites

Ensure you have Python installed on your system. You also need the following Python libraries:

pip install opencv-python tkinter



💡 Usage
1️⃣ Encrypt a Message into an Image
Run the encoder.py script to hide a message inside an image:
python encoder.py

A file selection window will open. Choose an image.
Enter the secret message to be hidden.
Enter a passcode for protection.
The encrypted image will be saved as encryptedImage.png.


2️⃣ Decrypt the Hidden Message
Run the decoder.py script to extract the message:
python decoder.py

A file selection window will open. Choose the encrypted image.
Enter the passcode.
The hidden message will be displayed and saved in decrypted_message.txt.


🛡 Security Note


Ensure you securely share the passcode with authorized users.
The encryption method used here is basic and can be enhanced for better security.


👨‍💻 Contributing
Contributions are welcome! Feel free to submit pull requests to improve the project.

📞 Contact
For any questions, reach out via GitHub Issues.


Happy Coding! 🚀

