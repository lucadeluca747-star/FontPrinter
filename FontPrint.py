import pyfiglet
import time
import keyboard
import os
os.system("cls")
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
bom = True
listening = True
print(GREEN + pyfiglet.figlet_format("Font\nPrinter", font="ansi_shadow") + RESET)
time.sleep(0.5)
def stop_program(event):
    global bom, listening
    if listening:   
        bom = False
    os.system("cls")


keyboard.on_press_key("esc", stop_program)


while bom:
    try:
        listening = False
        obj = str(input(CYAN + "\n cosa vuoi stampare: \n" + RESET))
        a = input(CYAN + "\n quanto tempo deve esserci tra una stampa e l'altra? (secondi)\n" + RESET)
        listening = True

        for f in pyfiglet.FigletFont.getFonts():
            if not bom:
                break
            print(f, "\n")
            print(pyfiglet.figlet_format(obj, font=f))
            time.sleep(float(a))

    except:
        print("Errore...", end="")
        time.sleep(3)
        print(" riprovando...", end="")
        time.sleep(5)
        os.system("cls" )
        os.system("pip install pyfiglet")
        os.system("pip install pyfiglet")
        try:
            import pyfiglet
            import keyboard
        except:
            print(" \n errore fatale del programma, impossibile importare pyfiglet, riavviare il programma o provare ad installlare pyfiglet manualmente")