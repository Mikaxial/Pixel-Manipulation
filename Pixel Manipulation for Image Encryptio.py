from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    # Open the image
    image = Image.open(image_path)
    encrypted_image = image.copy()
    # Perform encryption
    for x in range(encrypted_image.width):
        for y in range(encrypted_image.height):
            r, g, b = encrypted_image.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_image.putpixel((x, y), (r, g, b))
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    image = Image.open(image_path)
    decrypted_image = image.copy()
    # Perform decryption
    for x in range(decrypted_image.width):
        for y in range(decrypted_image.height):
            r, g, b = decrypted_image.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_image.putpixel((x, y), (r, g, b))
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? Enter E or D--> ").upper()
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (an integer)--> "))
    # File path where the images will be saved
    encrypted_output_path = "C:/Users/MIS/Downloads/Course/Prodigy Tech/encrypted_image.png"
    decrypted_output_path = "C:/Users/MIS/Downloads/Course/Prodigy Tech/decrypted_image.png"

    if choice == 'E':
        encrypt_image(image_path, key, encrypted_output_path)
    elif choice == 'D':
        decrypt_image(image_path, key, decrypted_output_path)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
