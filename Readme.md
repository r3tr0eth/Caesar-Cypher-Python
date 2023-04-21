## Caesar Cipher

The Caesar cipher is a simple encryption technique that involves shifting each letter of a message by a fixed number of positions in the alphabet. This technique is named after Julius Caesar, who allegedly used it to encode his private correspondence.

### Project Description

This project implements the Caesar cipher in Python. The caesar_cipher function takes in a plaintext message and a shift value, and returns the encrypted ciphertext. The ciphertext is obtained by shifting each character in the plaintext by the specified number of positions in the alphabet, wrapping around if necessary.

### Usage
To use this project, simply call the caesar_cipher function with the plaintext message and the desired shift value. The function returns the encrypted ciphertext.

````
def caesar_cipher(plaintext, shift):
    """
    Encrypts the plaintext using the Caesar cipher with the given shift value.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character by the specified amount, wrapping around the alphabet if necessary
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext`
````
### Execution

```
# Get the plaintext and key from the user
plaintext = input('Enter the plaintext: ')
key = int(input('Enter the key: '))

# Encrypt the plaintext using the key
ciphertext = caesar_cipher(plaintext, key)
print('Ciphertext:', ciphertext)
````
### Example

Here's an example of how to use the caesar_cipher function:

```
Enter the plaintext: hello world
Enter the key: 3
Ciphertext: khoor zruog
```
### Limitations
This implementation of the Caesar cipher only handles uppercase and lowercase letters, and leaves all other characters (such as spaces and punctuation) unchanged. It also assumes that the plaintext does not contain any accented or non-Latin characters. Additionally, the security of the Caesar cipher is relatively weak, and it can be easily broken by modern cryptanalysis techniques. Therefore, it should not be used for sensitive data or in situations where strong security is required.