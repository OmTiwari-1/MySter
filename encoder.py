import cv2
import os
import tkinter as tk
from tkinter import filedialog


def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    return file_path


def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return None

    # Dictionary to map characters to ASCII values
    char_to_ascii = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = char_to_ascii[msg[i]]  # Store ASCII value

        # Move to the next pixel position
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m >= img.shape[1]:  # Move to next row when column limit is reached
                m = 0
                n += 1
                if n >= img.shape[0]:  # Prevent overflow
                    break

    encrypted_image_path = os.path.join(
        os.path.dirname(image_path), "encryptedImage.png"
    )
    cv2.imwrite(encrypted_image_path, img)
    print(f"✅ Encrypted image saved as: {encrypted_image_path}")

    # Save the password to a file
    password_file_path = os.path.join(os.path.dirname(image_path), "password.txt")
    with open(password_file_path, "w", encoding="utf-8") as f:
        f.write(password)

    print(f"🔑 Password saved in: {password_file_path}")
    return encrypted_image_path


def main_encrypt():
    image_path = select_image()
    if not image_path:
        print("No image selected. Exiting...")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypted_image_path = encrypt_image(image_path, msg, password)

    if encrypted_image_path:
        os.system(f'start "" "{encrypted_image_path}"')


if __name__ == "__main__":
    main_encrypt()

