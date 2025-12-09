import sys
from pathlib import Path
import fileread
import cards
import kazamata
#import game_mode
import os
import uj_gamemode
import jatekosmenu
from time import sleep


import os
import platform
import subprocess

def maximize_console():
    system = platform.system()
    
    if system == "Windows":
        try:
            import win32gui
            import win32con
            import win32console

            # Get console window handle
            hwnd = win32console.GetConsoleWindow()
            if hwnd:
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        except ImportError:
            print("win32gui not installed. Cannot maximize console on Windows.")
    
    elif system == "Linux":
        # Try using xdotool (X11)
        try:
            term_class = os.environ.get("TERM", "")
            subprocess.run([
                "xdotool", "search", "--onlyvisible", "--class", term_class,
                "windowsize", "100%", "100%"
            ])
        except FileNotFoundError:
            # Fallback: resize with ANSI escape codes
            os.system("printf '\\e[8;50;150t'")
    
    else:
        # Other OSes: do nothing
        pass

def maximize():
    os.system("title Damareen")
    handle = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)



def main():
    if len(sys.argv) == 1:
        print("Használat: python script.py [--ui | <test_dir_path>]")
        
        sys.exit(1)

    if sys.argv[1] == "--ui":
        run_ui()
    else:
        run_automated_test(sys.argv[1])


# ! jatek mod
def run_ui():
    maximize_console()
    uj_gamemode.betoltokepernyo()
    pass

# ! teszt mod/automata jatek
def run_automated_test(test_dir_path):
    with open(Path(test_dir_path) / 'in.txt', 'r') as f:
        fileread.read_file(f, test_dir_path)
        pass

if __name__ == "__main__":
    main()


