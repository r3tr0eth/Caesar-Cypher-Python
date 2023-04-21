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


# Get the plaintext and key from the user
ciphertext = input('Enter the plaintext: ')
key = int(input('Enter the key: '))

# Decrypt the ciphertext using the key

decrypted_plaintext = decrypt_caesar(ciphertext, key)
print('Decrypted plaintext:', decrypted_plaintext)
