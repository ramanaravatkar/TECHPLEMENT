import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print("Generated password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
