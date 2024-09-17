import string
import getpass

def pwd_strength_check():
        password = getpass.getpass('Enter Password: ')
        strength = 0
        remarks = ''
        upper_count = lower_count = digit_count = special_char_count = 0
        
        for char in list(password):
            if char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.ascii_lowercase:
                lower_count += 1
            elif char in string.digits:
                digit_count += 1
            else:
                special_char_count += 1

        if upper_count >= 1:
            strength += 1
        if lower_count >= 1:
            strength += 1
        if digit_count >= 1:
            strength += 1
        if special_char_count >= 1:
            strength += 1


        if strength == 1:
         remarks = "Password is too weak.\nYou must revise a strong password"
        elif strength == 2:
         remarks = "Weak password.\nYou must revise a stronger password"
        elif strength == 3:
         remarks = "Password is okay but you could make it stronger"
        elif strength == 4 :
         remarks = "Strong password"


        
        print(f"password strength: {(strength/ 4) * 100}%")
        print(f"\nRemarks: {remarks}")

        print("\nYour Password contains: ")
        print(f"{upper_count} upper case letters\n{lower_count} lower case letters\n{digit_count} digits\
            \n{special_char_count} special characters\n")



def new_pwd_check(newPassword = False):
        old_pwd  = "Would you like to check how strong your password is? (yes/no)"
        another_pwd = "Would you like to try another password and check its strength? (yes/no)"

        ask_user = another_pwd if newPassword else old_pwd
        choice = input(ask_user).lower()

        if choice == 'yes':
          return True
        elif choice == 'no':
            print("Thank you for trying this program.\nBye")
            return False
        else:
            print('There\' has been some input error. Please try again.')




if __name__ == '__main__':
        print(' --- Password Strength Checker --- ')
        pwd_check = new_pwd_check()
        while pwd_check:
            pwd_strength_check()
            pwd_check = new_pwd_check(True)

