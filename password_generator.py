#Password Generator Project
import random
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letter_list=[letters[char] for char in range(random.randint(8, 10))]

    symbols_list=[symbols[char] for char in range(random.randint(2, 4))]

    numbers_list=[numbers[char] for char in range(random.randint(2, 4))]

    password_list=letter_list+symbols_list+numbers_list

    random.shuffle(password_list)

    password=''.join(password_list)


    return password