def caesar_cipher(plaintext, shift):
    """
    Encrypts the plaintext using the Caesar cipher with the given shift value.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character by the specified amount, wrapping around the alphabet if necessary
            shifted_char = chr((ord(char) - 65 + shift) % 26 +
                               65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext


# Get the plaintext and key from the user
plaintext = input('Enter the plaintext: ')
key = int(input('Enter the key: '))

# Encrypt the plaintext using the key
ciphertext = caesar_cipher(plaintext, key)
print('Ciphertext:', ciphertext)
