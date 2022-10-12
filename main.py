import secrets
import string


def app_title():
    print("### Password Generator ###")
    print("\tGenerate safe enough passwords with python's secret module.")
    print("\tYou can read 'PEP 506 – Adding A Secrets Module.\n"
          "\tTo The Standard Library' for more details.\n")


def exclude_set_from_set(to_exclude, from_set):
    return from_set-to_exclude


def main():
    app_title()

    #todo choose character sets
    #print("Which characters should be used for the password?")


    # create the character sets
    letters = string.ascii_uppercase + string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    stop_bool = False
    while not stop_bool:
        print("Characters to be used during password generation: ")
        print("\t(1) " + letters)
        print("\t(2) " + digits)
        print("\t(3) " + special_chars)
        print("Choose option 1, 2, 3 if you need to edit or enter 0 to move on.")

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


if __name__ == '__main__':
    main()

