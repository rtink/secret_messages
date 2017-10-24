import os
import sys
from polybius import Polybius
from atbash import Atbash
from keyword_cipher import Keyword_cipher


def clear():
    '''Clear screen'''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    '''Welcome user to Secret Messages'''
    clear()
    print(input("Welcome to Secret Messages. Press any key to continue"))


def byebye():
    '''Say good-bye when user quits'''
    print("Bye Bye!!")
    sys.exit()


def cipher_menu():
    '''Create a menus for Secret Messages and
    retrieve user inputs'''
    while True:

        '''Gives user a choice of ciphers to choose from'''
        ciphers = {'1': 'polybius', '2': 'atbash', '3': 'keyword'}

        print("Choose a NUMBER from the menu below")

        for key, item in ciphers.items():
            print("{}: {}".format(key, item))

        choice = input("Enter your number here or enter q to quit ->\n ")

        if choice == 'q':
            break

        if choice in ciphers:
            '''Input is valid, ok to execute cipher'''
            clear()
            cipher_choice = ciphers[choice]
            while True:
                crypt = {'1': 'encrypt', '2': 'decrypt'}
                print("Choose a NUMBER from menu below")
                for key, item in crypt.items():
                    print("{}: {}".format(key, item))
                choice2 = input("Enter your number or b to go back->\n")

                if choice2 == 'b':
                    break

                if choice2 in crypt:
                    clear()
                    encrypt_decrypt_choice = crypt[choice2]
                    text = input(
                        "What message do you want to {}->\n".format(
                            str(encrypt_decrypt_choice)))
                    message = text.lower()
                    while True:
                        if cipher_choice == 'polybius':
                            if encrypt_decrypt_choice == 'encrypt':
                                user_choice = Polybius()
                                user_choice.encrypt(message)
                                ciper_replay()
                        if cipher_choice == 'polybius':
                            if encrypt_decrypt_choice == 'decrypt':
                                user_choice = Polybius()
                                user_choice.decrypt(message)
                                ciper_replay()
                        if cipher_choice == 'atbash':
                            if encrypt_decrypt_choice == 'encrypt':
                                user_choice = Atbash()
                                user_choice.encrypt(message)
                                ciper_replay()
                        if cipher_choice == 'atbash':
                            if encrypt_decrypt_choice == 'decrypt':
                                user_choice = Atbash()
                                user_choice.decrypt(message)
                                ciper_replay()
                        if cipher_choice == 'keyword':
                            if encrypt_decrypt_choice == 'encrypt':
                                user_keyword = input(
                                    "Chose a keyword to use-> \n").lower()
                                user_choice = Keyword_cipher(user_keyword)
                                user_choice.encrypt(message)
                                ciper_replay()
                        if cipher_choice == 'keyword':
                            if encrypt_decrypt_choice == 'decrypt':
                                user_keyword = input(
                                    "Chose a keyword to use in the cipher.\n"
                                    "If you want to decrypt the message you "
                                    "encrypted you must supply the same "
                                    "keyword-> \n").lower()
                                user_choice = Keyword_cipher(user_keyword)
                                user_choice.decrypt(message)
                                ciper_replay()


def ciper_replay():
    cipher_again = input("Enter M to play again, Enter Q to quit.\n").lower()
    if cipher_again == 'm':
        cipher_menu()
    elif cipher_again == 'q':
        byebye()


if __name__ == '__main__':
    # welcome the user
    welcome()
    # give user cipher choices
    cipher_menu()
    # end program
    byebye()
