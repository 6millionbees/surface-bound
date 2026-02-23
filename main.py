# Arden Boettcher
# 12/10/25
# Your Blood Will Boil

import curses



def main(scr: curses.window):
    curses.start_color()
    import formatting as form
    import multiple_choice as mult
    curses.noecho()
    curses.nocbreak()
    curses.curs_set(0)

    curses.init_color(4, 300, 300, 1000)

    scr.keypad(True)

    c: int = 0
    running = True

    while running:
        scr.erase()



        scr.refresh()
        c = scr.getch()
        if c == 10:
            break

    return



if __name__ == "__main__":
    curses.wrapper(main)
    quit()
