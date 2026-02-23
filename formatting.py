# Arden Boettcher
# 12/9/25
# Formatting functions

import curses



def usable_string(string: str, width=75) -> list[str]:
    if width < 10:
        raise ValueError("Width must be >= 10")
    usable = []
    split_string: list[str] = string.split()

    while split_string:
        x = -1
        temp_str = ""

        for word in split_string:
            if len(temp_str + word) > width:
                break
            x += 1
            temp_str += word + " "

        temp_str = temp_str[0: -1]

        if x < -1:
            usable.append(split_string[0][0:width - 1] + "-")
            usable.append(split_string[0][width - 1: -1])
        usable.append(temp_str)
        split_string = split_string[x + 1:]

    return usable



def print_usable(usable: list[str], scr, font, start=0) -> None:
    y = start
    for line in usable:
        try:
            scr.addstr(y, 0, line, font)
        except curses.error:
            pass
        y += 1
    return None




class RichText():
    pass