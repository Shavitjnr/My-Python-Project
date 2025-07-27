import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4.")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
