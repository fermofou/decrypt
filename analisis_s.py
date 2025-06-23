import string

letter_frequency_table = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.361, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
}

def encrypt_char(char, key):
    if char in key:
        return key[char]
    else:
        return char

def swap_lettersS(key, letter1, letter2):
    # Swap the positions of the letters in the key
    new_key = {k: (letter2 if v == letter1 else letter1 if v == letter2 else v) for k, v in key.items()}
    return new_key

def substitution_cipherS(text, key):
    if not isinstance(key, dict) or len(key) != 26:
        raise ValueError("The key must be a dictionary with 26 letter mappings.")

    text = text.upper()  # Ensure text is in uppercase
    encrypted_text = ''.join(encrypt_char(char, key) for char in text)
    return encrypted_text



def substitution_analysisS(input_path, output_path):
    # Read the encrypted text from input file
    with open(input_path, 'r') as file:
        encrypted_text = file.read().upper()

    # Count the frequency of each letter in the encrypted text
    letter_counts = {char: encrypted_text.count(char) for char in string.ascii_uppercase}

    # Sort the letters by frequency
    sorted_encrypted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    sorted_expected_letters = sorted(letter_frequency_table, key=letter_frequency_table.get, reverse=True)

    # Create the decryption key
    decryption_key = {encrypted: expected for (encrypted, _), expected in zip(sorted_encrypted_letters, sorted_expected_letters)}

    # Decrypt the text using the generated key
    decrypted_text = substitution_cipherS(encrypted_text, decryption_key)

    """ #here is how i had the addition to swap letters by user :)
    #show user the result, to add needed change
    exit=True
    while(exit):
        print("First 15 lines of decrypted text:")
        print('\n'.join(decrypted_text.splitlines()[:15]))
        swap_input = input("Do you want to swap two letters in the key? (yes/no): ")

        if swap_input.lower() in ('yes','y'):
            letter1 = input("Enter the first letter to swap: ").upper()
            letter2 = input("Enter the second letter to swap: ").upper()
            if letter1 in decryption_key and letter2 in decryption_key:
                decryption_key = swap_letters(decryption_key, letter1, letter2)
                print(f"Letters '{letter1}' and '{letter2}' swapped in the key.")
                decrypted_text = substitution_cipher(encrypted_text, decryption_key)

            else:
                print("Both characters must be a letter from a to z.")
                return decryption_key
        else:
            with open(output_path, 'w') as file:
                file.write(decrypted_text)

            exit=False
    """

    # Write the decrypted text to the output file
    with open(output_path, 'w') as file:
        file.write(decrypted_text)

    return decryption_key

# Example usage:
# substitution_analysis('encrypted.txt', 'decrypted.txt')
