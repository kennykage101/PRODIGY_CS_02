import numpy as np
from PIL import Image
from typing import Optional

class ImageEncryptionTool:
    def __init__(self, key: int = 123):
        """
        Initialize the ImageEncryptionTool with an encryption key.

        Args:
            key (int, optional): The encryption key. Defaults to 123.
        """
        self.key = key

    def encrypt_image(self, image_path: str) -> None:
        """
        Encrypt an image by swapping the red and blue channels.

        Args:
            image_path (str): The path to the input image file.
        """
        with Image.open(image_path) as image:
            pixels = np.array(image)
            pixels[:, :, [0, 2]] = pixels[:, :, [2, 0]]  # Swap in-place
            encrypted_image = Image.fromarray(pixels.astype(np.uint8))
            encrypted_image.save("encrypted_image.png")

    def decrypt_image(self, image_path: str) -> None:
        """
        Decrypt an image by swapping the red and blue channels.

        Args:
            image_path (str): The path to the encrypted image file.
        """
        with Image.open(image_path) as image:
            pixels = np.array(image)
            pixels[:, :, [0, 2]] = pixels[:, :, [2, 0]]  # Swap in-place
            decrypted_image = Image.fromarray(pixels.astype(np.uint8))
            decrypted_image.save("decrypted_image.png")

def main():
    tool = ImageEncryptionTool()

    print("1. Encrypt image")
    print("2. Decrypt image")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        image_path = input("Enter the image path: ")
        tool.encrypt_image(image_path)
        print("Image encrypted successfully!")
    elif choice == 2:
        image_path = input("Enter the encrypted image path: ")
        tool.decrypt_image(image_path)
        print("Image decrypted successfully!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
1