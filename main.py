import secrets
import random
import string


def app_title():
	print("### Password Generator ###")
	print("\tGenerate safe enough passwords with python's secret module.")
	print("\tYou can read 'PEP 506 – Adding A Secrets Module.\n"
		  "\tTo The Standard Library' for more details.\n")


def choose_character_sets() -> tuple:
	"""
	Lets the command line user choose which character sets are used
	in password generation. Available character sets:
	string.ascii_uppercase + string.ascii_lowercase = letters,
	string.ascii_digits = numbers, and string.punctuation = special chars.
	:return: tuple of boolean values
		where each boolean represents the use of the character set
		in password generation.
	"""
	has_letters = False
	has_numbers = False
	has_special_chars = False
	stop_bool = False
	while not stop_bool:
		print("Character sets to be used during password generation: ")
		print("\t1 for Yes, 2 for No")
		print("\tShould letters be used?")
		has_letters = True if int(input()) == 1 else False
		print(has_letters)
		print("\tShould numbers be used?")
		has_numbers = True if int(input()) == 1 else False
		print("\tShould special chars be used?")
		has_special_chars = True if int(input()) == 1 else False
		print("End = 1? Repeat = 2?")
		stop_bool = True if int(input()) == 1 else False

	return has_letters, has_numbers, has_special_chars


def edit_character_sets(has_letters: bool, has_numbers: bool,
						has_special_chars: bool) -> tuple:
	letters = ""
	digits = ""
	special_chars = ""
	# create the character sets
	if has_letters:
		letters = string.ascii_uppercase + string.ascii_lowercase
	if has_numbers:
		digits = string.digits
	if has_special_chars:
		special_chars = string.punctuation

	stop_bool = False
	while not stop_bool:
		print("Characters to be used during password generation: ")
		print("\t(1) " + letters)
		print("\t(2) " + digits)
		print("\t(3) " + special_chars)
		print(
			"Choose option 1, 2, 3 if you need to edit or enter 0 to move on.")

		option = int(input("Enter option: "))
		if option == 0:
			stop_bool = True
			print("Exiting")
		elif option == 1:
			print("Option 1 was selected.")
			print("\tEnter character(s) without space in between: ")
			to_exclude = set(input())
			letters = "".join(sorted(set(letters) - to_exclude))
		elif option == 2:
			print("Option 2 was selected.")
			print("\tEnter character(s) without space in between: ")
			to_exclude = set(input())
			digits = "".join(sorted(set(digits) - to_exclude))
		elif option == 3:
			print("Option 3 was selected.")
			print("\tEnter character(s) without space in between: ")
			to_exclude = set(input())
			special_chars = "".join(sorted(set(special_chars) - to_exclude))
		else:
			print("Invalid option selected. Try again.")

	return letters, digits, special_chars


def how_many_chars_of_each_set_and_pwd_length() -> tuple:
	n_pwd = 0
	n_letters = 0
	n_digits = 0
	n_special_chars = 0
	stop_bool = False
	while not stop_bool:
		print("How long should the password be?")
		print("\tEnter a positive number.")
		n_pwd = int(input())
		print("How many letters should the password contain?")
		print("\tEnter a positive number.")
		n_letters = int(input())
		print("How many digits should the password contain?")
		print("\tEnter a positive number.")
		n_digits = int(input())
		print("How many special chars should the password contain?")
		print("\tEnter a positive number.")
		n_special_chars = int(input())

		if n_pwd == (n_letters + n_digits + n_special_chars):
			stop_bool = True
		else:
			print("Password length not equal to sum of each char set length.")
			print("Try again.")

	return n_pwd, n_letters, n_digits, n_special_chars


#def generate_password(pwd_length: int, n_letters: int, n_digits: int,
#					  n_special_chars: int) -> string:

#	if pwd_length == n_letters + n_digits + n_special_chars:

#	else:
#		return "The pwd length and the sum of the char set choices don't match."


def main():
	app_title()

	has_letters, has_numbers, has_special_chars = choose_character_sets()
	letters, digits, special_chars = edit_character_sets(has_letters,
															 has_numbers,
															 has_special_chars)
	n_pwd, n_letters, n_digits, n_special_chars = \
		how_many_chars_of_each_set_and_pwd_length()
	#generate_password(n_pwd, n_letters, n_digits, n_special_chars)

	if n_pwd == n_letters + n_digits + n_special_chars:
		set1 = "".join(secrets.choice(letters) for i in range(n_letters))
		set2 = "".join(secrets.choice(digits) for i in range(n_digits))
		set3 = "".join(secrets.choice(special_chars) for i in range(n_special_chars))

		password_ordered = set1+set2+set3
		password_list = list(password_ordered)
		random.shuffle(password_list)
		password = ''.join(password_list)
		print(password)


if __name__ == '__main__':
	main()
