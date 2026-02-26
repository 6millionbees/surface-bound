# Pseudocode

<ol>
  <li>
    <a href="#struct">Information Structure</a>
  </li>
</ol>

## <font id="struct">Information Structure</font>

The main thing I tend to struggle with when it comes to imagining how a game will work internally is the information structure. So I'm going to plan it from the get-go before I make any long term structuring mistakes.

### Main Class
The thing that runs
```Python
def Main(scr):
    # Main function is in a curses Wrapper
    # Most things are initialized in here

    while True:
        # Pick the save or start a new one
        if load:
            Game(scr).load(save)
        elif new:
            Game(scr).new()
        # The load and new functions also start the game loop
```









