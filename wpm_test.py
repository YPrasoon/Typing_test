
#WPM speed test

import curses
from curses import wrapper
import time
import random

def load_text():
    with open("wpm-testfile.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()
    
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("WELCOME TO THE SPEED TYPING TEST")
    stdscr.addstr("\n Press any key to enter :")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2, 0, f"your average speed is: {wpm} wpm")
    
    for i,char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(1 , i, char, color)

def wpm_test(stdscr):
    target_text = load_text()
    current_text =[]
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed / 60) /5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text.strip():
            stdscr.nodelay(False)
            break

        try:
            key =stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        
        elif ( len(current_text) < len(target_text) ):
            current_text.append(key)
           

def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        
        stdscr.addstr(3,0, " you completed the text! Well done! \n to exit: Press esc \n to continue: Press any other key...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper (main)
