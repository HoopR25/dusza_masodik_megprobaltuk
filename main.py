import sys
from pathlib import Path
import fileread
import cards
import kazamata
import game_mode
import uj_gamemode
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
    uj_gamemode.betoltokepernyo()
    pass

# ! teszt mod/automata jatek
def run_automated_test(test_dir_path):
    with open(Path(test_dir_path) / 'in.txt', 'r') as f:
        fileread.read_file(f, test_dir_path)
        pass

if __name__ == "__main__":
    main()