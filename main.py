"""
Simple password generator built with Python.
2023
"""

import random


chars = [
    "abcdefghijklmnopqrstuvwyxz",
    "ABCDEFGHIJKLMNOPQRSTUVWYXZ",
    "!@#$%*()|/?[]{}\\",
    "1234567890",
]


def start():
    print("Bea's Password Generator")
    password_len = None

    while isinstance(password_len, int) != True:
        try:
            password_len = int(input("Insert length for your password:\n"))
        except KeyboardInterrupt:
            break
        except:
            print("Please insert a number.\n")
    generate_password(password_len)


def generate_password(password_len):
    print("Generating your password...")
    list_password = []
    for c in range(password_len):
        type_of_char = chars[random.randrange(4)]
        len_type_of_char = len(type_of_char)
        c = type_of_char[random.randrange(len_type_of_char)]
        list_password.append(c)

    password = "".join(list_password)
    print(f"Here's your new password:\n{password}")


if __name__ == "__main__":
    start()
