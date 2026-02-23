## <span style="color: #9f9">Ideas

### <span style="color: #f9f">The Code</span>

The idea for how the code will be laid out goes somewhat like this:

```python
def Main():
  # main menu type shit
  # load save, new save, and options
  # saves (and the options) will be stored in json files
  # there will be other functions for the file handling that need to be called here

  # if you load a save or make a new one then it initializes and runs the game class
  Game(save, scr).run()

  # if you select options it will open an options menu
  options()
```

<span style="color: #82ffcdff">Game class</span>

```python
class Game:
  def __init__(self, save, scr)
    # the save object is probably just going to be a complicated dictionary
    self.save_data = save
    self.scr = scr

  def run(self):
    self.running = True

    while self.running:
      # game loop!!!

      # displays the text
      self.draw()

      # takes user input either using the curses module or the keyboard module
      self.input_handler()

      # I'm not really sure how to incorporate one-time events into the game loop
      # I'm sure I'll figure it out, I'll come back to this later if I do.
```

<span style="color: #82ffcdff">Rich Text class</span>

This one is so annoyingly complex and requires too many different formatting options that I don't even have a code snippet for it

I'm thinking of creating



### <span style="color: #f9f">Saving</span>
I want a file saving system similar to most rpgs (such as disco elysium)<br>

for example:

**New Game** - Self explanitory<br>
**Load Save** - Will go into more depth<br>

What the load save option would look like:

```
Load Save
> playthrough_name date savetype
> evil_mode 12-9 11:24 autosave
 ```

I'm thinking there will be a limited number of saves (obvi) and they're either in save slots or unorganized (unoragnized might be better because it allows for savescumming)

### <span style="color: #f9f">Images</span>

For just a better experience overall I would like there to be images. I want to figure out if I can display images within the terminal or if I need to use an outside display (like PIL). I wonder if PIL works within curses, probbly not but it's worth a shot.

If the images don't work in the terminal then I can probably just open a new window when I want to show an image.

I hope the windows stay there when the image opens.<br>
If I can't get images to work then I guess I'll just kill myself /j... unless...

<span style="color: darkseagreen;">more recent arden here:</span> I got images to work, we using matplotlib because I like the zoom and it looks better than pillow

I am figuring out how to customize the toolbar. The goal is to have my very own img displaying function/class to standardize the images.<br>
I also want to prevent the image from clipping with the weird bounding box they have, but I have no idea what it's called to change it. I think this has something to do with subplots but these fuckers have a hard time speaking with real words.

<span style="color: lightgreen;">about 4 hours ahead of prev arden here:</span> JESUS FUCKING CHRIST THAT WAS INSANE. I did not need to get gifs to work and man that sucked to go through but now that it's over I am overjoyed and very tired. I love programming, I love it so much. Programming hits that absolutely perfect sweet spot between difficult and rewarding that fucks hard.

This would be the place where I write documentation but the source code already has a fuck ton of comments so I'll let them speak for themselves.

### <span style="color: #f9f">General vibe</span>

I want to have a mix between multple choice menus navigated by the arrow keys, to buttons, to number puzzles, to time restricted clicking games. I want the player to feel under pressure, like a mistake will kill them, they need to follow the procedure.

**<span style="color: #F43">The Creature</span>** - <span style="font-style: italic">bumbumbumbumbumbumbumbum Mr. Diveman bring me a dive</span>

The creature has not changed from the concept art, I still feel like the imagery will go hard as fuck. They're still an old fashioned diving suit with a tube coming from the back of their neck going upwards to fade into the inky abyss.



### <span style="color: #f9f">Gameplay</span>

There will be a resource management system, you get money for doing a job well and you spend the money to do jobs better. You will never have enough money for everything.

There will be two modes

- <span style="color: #82ffcdff">Story</span><br>
This will be the favorite child, this is where all of my energy will be poured into

- <span style="color: #82ffcdff">Endless</span><br>
You unlock it by completing the story and you just try to surive as long as possible without dying (you will be able to save scum but idgaf it's an honor thing)