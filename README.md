# Image Encryption Tool

A simple Python tool for encrypting and decrypting images by swapping the red and blue channels.

## Prerequisites

- Python 3.x
- Pillow library (`pip install Pillow`)
- NumPy library (`pip install numpy`)

## Installation

1. Clone the repository:
git clone https://github.com/kennykage101/PRODIGY_CS_02.git


2. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Run the script:
python imagencrypt.py
2. Choose the desired option:
   - 1: Encrypt an image
   - 2: Decrypt an image
3. Enter the path to the input image file when prompted.
4. The encrypted or decrypted image will be saved as `encrypted_image.png` or `decrypted_image.png`, respectively, in the same directory as the script.

## Code Structure

The script consists of the following components:

- `ImageEncryptionTool` class:
  - `__init__(self, key: int = 123)`: Initializes the tool with an encryption key (default: 123).
  - `encrypt_image(self, image_path: str) -> None`: Encrypts the image by swapping the red and blue channels.
  - `decrypt_image(self, image_path: str) -> None`: Decrypts the image by swapping the red and blue channels (reverse of encryption).
- `main()` function: Handles user input and calls the appropriate encryption or decryption method.

## Notes

- This encryption method (swapping red and blue channels) is not a secure encryption algorithm. If you need to encrypt images for security purposes, consider using a more robust encryption algorithm like AES or RSA.
- The script assumes that the input image file is in a format supported by the Pillow library (e.g., JPEG, PNG, BMP).
- The encrypted and decrypted images are saved in the PNG format.


