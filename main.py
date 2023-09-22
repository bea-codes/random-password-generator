"""
Simple password generator built with Python.
2023
"""

letters_lowercase = "abcdefgijklmnopqrstuvwyxz"
letter_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
special_chars = "!@#$%*()|/?[]{\}"
numbers ="1234567890"

def start():
	print("Bea's Password Generator")
	password_len = None

	while (isinstance(password_len, int) != True):
		try:
			password_len = int(input("Insert length for your password:\n"))
		except KeyboardInterrupt:
			break
		except:
				print("Please insert a number.\n")
	generate_password()

def generate_password():
	print("Generating your password...")
	password_len = 10 # Tamanho da senha arbirtrário para fins de desenvolvimento...
	





if __name__ == "__main__":
	start()