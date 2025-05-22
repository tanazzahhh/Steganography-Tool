# Steganography Tool - Encode and Decode Hidden Messages in Images

## 📌 Description

This Python-based **Steganography Tool** allows you to **hide secret messages** within image files and retrieve them later — a technique commonly used in information security to prevent detection of sensitive data. Unlike cryptography which encrypts data, **steganography hides the existence of the data itself**.

This tool works entirely from the **Command Line Interface (CLI)** and supports both **encoding** and **decoding** of messages using popular image formats like `.png` and `.jpg`.

---

## Use Cases

- **Private Communication**: Hide confidential messages inside seemingly innocent images.
- **Cybersecurity Learning**: Learn fundamentals of data hiding, image manipulation, and Python I/O.
- **Forensics & Digital Investigation**: Explore methods to conceal and detect hidden content.
- **Research & Education**: Ideal for students and developers studying steganography and secure data transfer.

---

## Features

- **Encode messages** into image pixels using LSB (Least Significant Bit) technique.
- **Decode hidden messages** from encoded images with 1-click CLI access.
- **Supports JPG, JPEG, and PNG** image formats.
- Clean and user-friendly CLI menu.
- Exits automatically upon completion or when "Exit" is selected.
- Simple implementation with no external dependencies beyond `Pillow`.

---


### Requirements
- Python 3.x
- Pillow (`pip install pillow`)

### Installation
1. Clone this repository or download the `steganography_tool.py` file.
2. Ensure you have a source image (`input.png` or similar) in your working directory.

---

## How to Use

### 1. **Run the tool**
```bash
python steganography_tool.py
```

### 2. **Choose an option**
```text
1. Encode a message into an image
2. Decode a message from an image
3. Exit
```

---

### Example Workflow

#### Encoding
- Choose option `1`
- Enter:
  - Path to input image (`input.png`)
  - Message to hide (e.g. `"Top Secret Data"`)
  - Output image name (`output.png`)
- Tool embeds the message and creates a new image file with the hidden content.

#### Decoding
- Choose option `2`
- Enter:
  - Path to encoded image (`output.png`)
- Tool displays the hidden message if one is found.

---

## 📂 File Structure

```
.
├── steganography_tool.py   # Main script
├── input.png               # Example input image
├── output.png              # Image with hidden message
```

---

## Notes

- Output images with hidden messages look visually identical to original images.
- Works best with uncompressed image formats (PNG preferred).
- This is a basic tool; for enhanced security, consider combining with **cryptography** (future enhancement idea).

---

## Concepts Covered

- Steganography (LSB-based)
- Bitwise operations
- Python PIL image manipulation
- CLI design with menus
- Data encoding and retrieval

---

## Contributing

Pull requests and suggestions are welcome! If you have ideas to extend functionality — like adding cryptographic encryption, password protection, or batch processing — feel free to contribute.

---

## Author

Developed by **Tanazzah Shaikh**
Cybersecurity Student & Enthusiast
