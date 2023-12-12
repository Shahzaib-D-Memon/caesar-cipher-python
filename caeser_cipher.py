def encrypt(message, shift):
    """Encrypts a message using the Caesar Cipher."""
    result = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet character
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(message, shift):
    """Decrypts a message encrypted with the Caesar Cipher."""
    return encrypt(message, -shift)

def main():
    # Get user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
