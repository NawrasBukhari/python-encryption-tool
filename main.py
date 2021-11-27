"""
Password protected program to hide valuable data, passwords any desired intel or functional tools
responses of entries will be represented in colorful text to the user
program will not appear the intel until you pass the authentication
This program can be transformed into .exe easily after adjusting the parameters
use the next:
#----------------------------------------------------------------------------#
# 1- python -m pip install pyinstaller                                       #
# 2- pyinstaller --onefile main.py --icon=iconkazakh.ico                     #
# --icon: it is used for adding a small icon to the header                   #
# --onefile for specifying the targeted file to be assembled as .exe         #
#----------------------------------------------------------------------------#
This code has been conducted by: --> Nawras Bukhari <--
"""
# -->  Importing packages Begins  <-- #
import time
# -->  Importing packages Ends    <-- #


def main():
    red_color = "\033[1;31;40m"
    green_color = "\033[1;32;40m"
    # --------------------------------------------------BEGIN-------------------------------------------------- #
    """  Here agreement of replies Begins  """
    agreement = "You are eligible person who is authorised to use this program for the desired purposes\n" \
                "You will use this tool for educational purposes only, not for harming, sabotage or destroying data\n" \
                "If you would like to continue please write yes or no to close the program\n" \
                f"{red_color}You Have only 3 times to try so no bruteforce will work on me{green_color}\n" \
                f"{red_color}I agree that I understand the rules that have been written here," \
                f" and I accept them all{green_color} "

    no = f"{green_color}You have {red_color}not {green_color}chosen yes which will terminate the program..."

    """  Here agreement of replies ends  """
    # --------------------------------------------------END---------------------------------------------------- #
    # ----------------------------------------------------------------------------------------------------------------#
    # --------------------------------------------------BEGIN-------------------------------------------------- #
    """  Here customizations of replies Begins  """
    red_color = "\033[1;31;40m"
    green_color = "\033[1;32;40m"
    safe_greetings = f"{green_color}Welcome to your safe"  # If login was successful
    key_admin_error = f"{red_color}Oops it seems that You have missed the point of this program"
    login_error = f"{red_color}You Entered wrong credentials!"  # if the user entered the user name wrongly or both
    # of them
    password_error = f"{red_color}Your password is wrong!"  # If the user entered the login right but the password is
    # wrong,
    # like a hint
    # The number of times the user should try to login before the termination of process

    """  Here customizations of replies ends  """
    # --------------------------------------------------END---------------------------------------------------- #
    # ------------------------------------------------------------------------------------------------------------------#
    # --------------------------------------------------BEGIN-------------------------------------------------- #
    """  Here credentials Begins  """

    login_admin = 'admin'  # credentials of login
    password_admin = "123456"  # Credentials of password
    key_admin = "wow"  # Key for extra layer of security
    attempts = 0

    """  Here credentials Ends  """
    # --------------------------------------------------END---------------------------------------------------- #
    # ------------------------------------------------------------------------------------------------------------------#
    # --------------------------------------------------BEGIN-------------------------------------------------- #
    """  Here credentials Begins  """
    credit = """
    version: Beta\n
    release: 27/11/2021\n
    author: Nawras Bukhari\n
    contact: admin@kazakhsdevelopers.com\n
    facebook: https://facebook.com/nawras.2000
    """
    """  Here customizations of replies ends  """
    # --------------------------------------------------END---------------------------------------------------- #
    # ------------------------------------------------------------------------------------------------------------------#

    while True and attempts < 3:  # Let the user try by giving him unlimited loop
        print(agreement)  # showing agreement for the user
        agree = input("write yes or no: \n=>")  # Here the user will enter his permission
        if agree != 'yes':  # If agree is answered as no
            print(no)  # It will print the decline answer
            quit()  # Program will be ending
        else:  # If the user answers as yes
            print("You are being redirected...")  # for showing reality of execution
            time.sleep(2)
            print(f'{red_color}**WARNING** Case is very sensitive **WARNING**{green_color}')
            login = input("Enter your Your username Here: ")  # Here the inserting of user login happens
            password = input("Enter Admin password Here: ")  # Here the inserting of user password happens
            key = input("Enter Key word Here: ")  # Key for extra layer of security
            # --------------------------------------Extra---------------------------------#

            # --------------------------------------Extra---------------------------------#
            if login != login_admin:  # If the credentials does not matches the login_admin variable
                print(login_error)  # It will print the login_error variable, check above to rephrase
                attempts += 1

            elif password != password_admin:  # If the password does not matches the password_admin variable
                print(password_error)  # It will print the password_error variable that have been defined above
                attempts += 1
            elif key_admin != key:
                print(key_admin_error)
                attempts += 1
            else:
                def content():
                    print(safe_greetings)
                    while True:
                        choice = input("Choose option from the next menu"
                                       f"\n{green_color}1 - Password of secret № 1 or tool "
                                       f"\n{green_color}2 - Password of secret № 2 or tool"
                                       f"\n{green_color}3 - Password of secret № 3 or tool"
                                       f"\n{green_color}4 - Password of secret № 4 or tool"
                                       f"\n5 - Surprise {red_color}(Not recommended){green_color}"
                                       "\n6 - credits "
                                       f"\n7 - {red_color}Quit\n{green_color}=>"

                                       )
                        while True:
                            if choice == '1':
                                print('email: test@test.com\npassword: 123456')
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '2':
                                print('email: test@test.com\npassword: 123456')
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '3':
                                print('email: test@test.com\npassword: 123456')
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '4':
                                print('email: test@test.com\npassword: 123456')
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '5':
                                print("option 5")
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '6':
                                print(credit)
                                time.sleep(3)
                                break
                            # ------------------------------------------------------------------------------------------------------------------#
                            elif choice == '7':
                                print("Bye Bye")
                                quit()
                content()
                break


main()
