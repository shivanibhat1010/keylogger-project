# Function to encrypt a message using Caesar Cipher
def encrypt(text, shift):
    result = ""  # This will store the final encrypted message
    for char in text:
        if char.isalpha():  # Check if character is a letter (A-Z or a-z)
            # Get ASCII start point: 65 for 'A' or 97 for 'a'
            start = ord('A') if char.isupper() else ord('a')

            # Encrypt the character by shifting within alphabet range
            # Steps: Convert to position (0-25), shift, wrap around, convert back to char
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # If not a letter (like space or punctuation), add as it is
            result += char
    return result  # Return the final encrypted message

# Function to decrypt text (just reverse the shift)
def decrypt(text, shift):
    # Call encrypt with negative shift to get back original message
    return encrypt(text, -shift)

# Main function to handle user input and display output
def main():
    print("Caesar Cipher Program")  # Title
    # Ask user if they want to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # Take the message from the user
    message = input("Enter your message: ")

    # Take shift value, and handle error if not a number
    try:
        shift = int(input("Enter the shift value (number): "))
    except ValueError:
        print("Shift must be a number.")  # Error message
        return  # Exit the program

    # If user chose encryption
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    # If user chose decryption
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

    # If user entered invalid choice
    else:
        print("Invalid option. Please choose 'e' or 'd'.")

# Run the program
if __name__ == "__main__":
    main()
