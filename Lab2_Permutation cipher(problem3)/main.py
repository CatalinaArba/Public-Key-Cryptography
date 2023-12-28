
#3. Permutation cipher.

def encrypt(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()

    # Calculate the number of rows in the grid
    num_rows = len(plaintext) // len(key)

    if len(plaintext) % len(key) != 0:
        num_rows += 1

    # Create an empty grid to store the characters
    grid = [['' for _ in range(len(key))] for _ in range(num_rows)]

    # Fill the grid with characters from the plaintext
    index = 0
    for row in range(num_rows):
        for col in range(len(key)):
            if index < len(plaintext):
                grid[row][col] = plaintext[index]
                index += 1

    # Rearrange the grid columns based on the key
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ""
    for row in grid:
        for col_index in key_indices:
            cipher_text += row[col_index]
    return cipher_text


def decrypt(ciphertext, key):
    # Calculate the number of rows in the grid
    num_rows = len(ciphertext) // len(key)

    if len(ciphertext) % len(key) != 0:
        num_rows += 1

    # Create an empty grid to store the characters
    grid = [['' for _ in range(len(key))] for _ in range(num_rows)]

    # Rearrange the grid columns based on the key
    key_indices = sorted(range(len(key)), key=lambda k: key[k])

    # Fill the grid with characters from the ciphertext
    index = 0
    for row in range(num_rows):
        for col_index in key_indices:
            if index < len(ciphertext):
                grid[row][col_index] = ciphertext[index]
                index += 1

    # Reconstruct the original plaintext
    plaintext = ""
    for row in grid:
        plaintext += ''.join(row)

    return plaintext


key = "KEY"
plaintext = "HELLO WORLD"
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
