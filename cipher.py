def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
def main():
    plain_text = input("Please enter a sentence: ")
    encrypted_text = caesar_cipher(plain_text, 5)
    print("The encrypted sentence is:", encrypted_text)
if __name__ == "__main__":
    main()
