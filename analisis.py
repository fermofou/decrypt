import string
from multiprocessing import Pool
from collections import Counter

# Define the letter frequency table
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

def swap_letters(key, letter1, letter2):
    new_key = {k: (letter2 if v == letter1 else letter1 if v == letter2 else v) for k, v in key.items()}
    return new_key

def substitution_cipher(text, key, ncores):
    if not isinstance(key, dict) or len(key) != 26:
        raise ValueError("The key must be a dictionary with 26 letter mappings.")
    for k, v in key.items():
        if k not in string.ascii_uppercase or v not in string.ascii_uppercase:
            raise ValueError("Both keys and values in the dictionary must be uppercase letters.")
    text = text.upper()  # Ensure all text is uppercase

    with Pool(ncores) as pool:
        encrypted_text = pool.starmap(encrypt_char, [(char, key) for char in text])
    # encrypted_text = [encrypt_char(char, key) for char in text]

    return ''.join(encrypted_text).upper()

def count_letters(text_chunk):
    return Counter(text_chunk)

def combine_counters(counters):
    combined = Counter()
    for counter in counters:
        for char, count in counter.items():
            if char in string.ascii_uppercase:
                combined[char] += count
    return combined

def substitution_analysis(input_path, output_path, ncores):

    with open(input_path, 'r') as file:
        encrypted_text = file.read().upper()

    chunk_size = len(encrypted_text) // ncores
    text_chunks = [encrypted_text[i:i + chunk_size] for i in range(0, len(encrypted_text), chunk_size)]

    letter_counts = {char: encrypted_text.count(char) for char in string.ascii_uppercase}

    sorted_encrypted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    sorted_expected_letters = sorted(letter_frequency_table, key=letter_frequency_table.get, reverse=True)

    decryption_key = {encrypted: expected for (encrypted, _), expected in zip(sorted_encrypted_letters, sorted_expected_letters)}

    decrypted_text = substitution_cipher(encrypted_text, decryption_key, ncores)
    
    with open(output_path, 'w') as file:
        file.write(decrypted_text)

    return decryption_key

def swap_lettersManual(text, letter1, letter2):
    temp_letter = '¤'  # A rare character unlikely to appear in the text
    swapped_text = text.replace(letter1, temp_letter).replace(letter2, letter1).replace(temp_letter, letter2)
    return swapped_text

    