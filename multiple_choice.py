# Arden Boettcher
# 12/10/25
# multiple choice menus

# There is actually a stack overflow post for this exact thing
# I'm going to do it slightly differently but it will be heavily inspired
# Luckily for me it isn't plagerism if you make it but better
import curses
import formatting as form


class Menu():
  """A multiple choice menu<br>
  It takes input by calling the .input() method"""
  def __init__(self,
    scr:curses.window,
    text_color:   int = 7,
    bg_color:     int = 0,
    select_color: int = 4,
    bg_select:    int = 0,
    title:        str = "fix the title",
    choices:      list[tuple[str, int]] = [("something went wrong", 0)],
    pos:          tuple[int, int]=(0, 0)
  ):
    self.scr = scr
    self.title = title
    self.choices = choices
    self.pos = pos
    self.selected = 0
    curses.init_pair(7, text_color, bg_color)
    curses.init_pair(8, select_color, bg_select)
    self.colors = (curses.color_pair(7), curses.color_pair(8))

  def draw(self):
    """Displays the menu once onto Menu.scr at the target pos"""
    x = 0
    self.scr.addstr(self.pos[1], self.pos[0], self.title, self.colors[0])
    for k, v in self.choices:
      if x == self.selected:
        self.scr.addstr(self.pos[1] + x + 1, self.pos[0] + 1,f"> {k}", self.colors[1])
      else:
        self.scr.addstr(self.pos[1] + x + 1, self.pos[0] + 1,f"> {k}", self.colors[0])
      x += 1

  def loop(self, end_button: int = 10):
    """Creates a loop until the menu is closed"""
    c = 0
    while c != end_button:
      self.scr.erase()

      self.draw()

      c = self.scr.getch()

      self.input(c)

      self.scr.refresh()

    return self.choices[self.selected][1]

  def input(self, key):
    """Handles the menus logic after taking keyboard input"""

    if key == curses.KEY_UP and self.selected > 0:
      self.selected -= 1
    if key == curses.KEY_DOWN and self.selected < len(self.choices) - 1:
      self.selected += 1


