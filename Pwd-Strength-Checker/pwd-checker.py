# needs rechecking and improvement

import string
import getpass

def pwd_checker():
    password = getpass.getpass('Enter Password: ')
    strength = 0
    remarks = ''
    upper_count = lower_count = digit_count = special_char_count = wspace_count = 0

    for char in list(password):
        if char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.digits:
            digit_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_char_count += 1

    if upper_count > 1:
        strength += 1
    if lower_count > 1:
        strength += 1
    if digit_count > 1:
        strength += 1
    if special_char_count > 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1

    if strength == 1 | 2 | 3:
        remarks = "Very poor password."
    elif strength == 4:
        remarks = "Weak password."
    elif strength == 5 | 6:
       remarks = "Good password but could be better."
    elif strength == 7 | 8 | 9 | 10:
        remarks = "Strong password."


    
    print(f"password strength: {strength}")
    print(f" {remarks}")

    print("Your Password contains: ")
    print(f"{upper_count} upper case letters\n{lower_count} lower case letters\n{digit_count} digits\
    {special_char_count} special characters\n{wspace_count} white space.")

# the following case is written in case the user wants to improve the password.

def improve_pwd(newPassword = False):
    valid = False
    if newPassword == True:
       choice = input('Would you like to try a new password: (yes/no)')
    else: 
       choice = input('Would you like to check password: (yes/no)')
    
    while not valid:
        if choice.lower()  == 'yes':
            return True
        elif choice.lower() == 'no':
            return False
        else:
            print('Invalid. Try Again')

if __name__ == '__main__':
    print('--- Password Strength Checker ---')
    if_improve_pwd = improve_pwd()
    while pwd_checker:
        pwd_checker()
        if_improve_pwd = improve_pwd(True)
