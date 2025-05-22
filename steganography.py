from PIL import Image
import os
import sys

def encode_message(image_path, message, output_path):
    # Add null terminator to mark end of message
    binary_message = ''.join([format(ord(char), '08b') for char in message]) + '00000000'

    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    encoded_image = image.copy()
    pixels = encoded_image.load()

    width, height = encoded_image.size
    index = 0

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if index < len(binary_message):
                r = (r & ~1) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                g = (g & ~1) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                b = (b & ~1) | int(binary_message[index])
                index += 1
            pixels[x, y] = (r, g, b)

            if index >= len(binary_message):
                break
        if index >= len(binary_message):
            break

    encoded_image.save(output_path)
    print(f"[+] Message encoded and saved to {output_path}")

def decode_message(image_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = image.load()

    width, height = image.size
    binary_data = ''
    decoded_message = ''

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == '\0':  # Null byte = end of message
            break
        decoded_message += char

    print(f"[+] Decoded message: {decoded_message}")

def main():
    print("=== Steganography Tool ===")
    while True:
        print("\nChoose an option:")
        print("1. Encode a message into an image")
        print("2. Decode a message from an image")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path to the input image: ")
            message = input("Enter the message to encode: ")
            output_path = input("Enter the path to save the output image: ")
            encode_message(image_path, message, output_path)
        elif choice == '2':
            image_path = input("Enter the path to the image with a hidden message: ")
            decode_message(image_path)
        elif choice == '3':
            print("Exiting Steganography Tool.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
