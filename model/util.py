import sys
sys.path
sys.path.append(r'C:\secure-erp-python-Cyarek')

import random
import string

def generate_characters(nr_of_characters, allowed_characters):
    random_characters = []
    for _ in range(nr_of_characters):
        random_characters.append(random.choice(allowed_characters))
    return random_characters

def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    list_of_characters = []
    generated_id = ''
    random_character = ''

    list_of_characters.extend(generate_characters(number_of_capital_letters, string.ascii_uppercase))
    list_of_characters.extend(generate_characters(number_of_small_letters, string.ascii_lowercase))
    list_of_characters.extend(generate_characters(number_of_digits, string.digits))
    list_of_characters.extend(generate_characters(number_of_special_chars, allowed_special_chars))

    for _ in range(len(list_of_characters)):
        random_character = random.choice(list_of_characters)
        generated_id = generated_id + random_character
        list_of_characters.remove(random_character)

    return generated_id
