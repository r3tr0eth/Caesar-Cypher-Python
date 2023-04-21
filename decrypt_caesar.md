### Project Description

This project implements the Caesar cipher in Python. The decrypt_caesar function takes in a plaintext message and a shift value, and returns the encrypted ciphertext. The ciphertext is obtained by shifting each character in the plaintext by the specified number of positions in the alphabet, wrapping around if necessary.

### Usage
To use this project, simply call the decrypt_caesar function with the plaintext message and the desired shift value. The function returns the encrypted ciphertext.

````
def decrypt_caesar(ciphertext, key):

    # Create an empty string to hold the decrypted message
    plaintext = ''

    # Loop through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the distance between the current character and the letter 'a' (for lowercase letters)
            # or 'A' (for uppercase letters)
            base = ord('a') if char.islower() else ord('A')
            distance = ord(char) - base

            # Apply the key to the distance to get the new distance
            new_distance = (distance - key) % 26

            # Determine the new character by adding the new distance to the base character
            new_char = chr(base + new_distance)
        else:
            # If the character is not a letter, leave it as-is
            new_char = char

        # Add the new character to the plaintext
        plaintext += new_char

    return plaintext
````
### Execution

```
# Get the plaintext and key from the user
ciphertext = input('Enter the plaintext: ')
key = int(input('Enter the key: '))

# Decrypt the ciphertext using the key

decrypted_plaintext = decrypt_caesar(ciphertext, key)
print('Decrypted plaintext:', decrypted_plaintext)
````
### Example

Here's an example of how to use the caesar_cipher function:

```
Enter the plaintext: khoor zruog
Enter the key: 3
Decrypted plaintext: hello world
```
### Limitations
This implementation of the Caesar cipher only handles uppercase and lowercase letters, and leaves all other characters (such as spaces and punctuation) unchanged. It also assumes that the plaintext does not contain any accented or non-Latin characters. Additionally, the security of the Caesar cipher is relatively weak, and it can be easily broken by modern cryptanalysis techniques. Therefore, it should not be used for sensitive data or in situations where strong security is required.