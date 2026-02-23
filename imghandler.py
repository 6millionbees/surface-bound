import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.animation as animation
import matplotlib as mpl
from PIL import Image as mage
from PIL import ImageSequence
from numpy import asarray

# matplotlib Colors
WHITE = "ffffff"
BLACK = "000000"
RED = "ff0000"
GREEN = "00ff00"
BLUE = "0000ff"

class Image:
  def __init__(self, src="images/backup.png", size=(4, 4)):
    mpl.rcParams["toolbar"] = "None"
    self.fig, self.ax = plt.subplots()
    self.fig.set_size_inches(size[0], size[1])
    self.ax.set_axis_off()
    self.img = plt.imshow(image.imread(src))

  def show(self, bg=(1, 1, 1), block=True):
    # A bug with this is that the background doesn't work with multiple
    # instances of this class being displayed at the same time
    self.fig.patch.set_facecolor(bg)
    plt.show(block=block)


class GifImage(Image):
  def __init__(self, src, size=(4, 4)):
    mpl.rcParams["toolbar"] = "None"
    self.fig, self.ax = plt.subplots()
    self.fig.set_size_inches(size[0], size[1])
    self.ax.set_axis_off()

    self.find_frames(src)



  def find_frames(self, src):
    # I'm going to break this down step by step

    # This is a list that stores the frames for the animation to use
    self.ims = []
    # This opens the image useing PIL.Image.open()
    # The reason the Image module is named weird is becauase too many things
    # used the word "Image" already
    im = mage.open(src)
    for frame in ImageSequence.Iterator(im):
      # This saves the first frame in the correct format
      self.ims.append(
        # For some reason it has to be in a list
        # Don't ask because I don't know
        [
          # This converts the array made by asarray()
          # Into a useable AxesImage
          plt.imshow(
            # This converts the Pil.Image.Image into an array
            asarray(
              # This calls the previously image that was opend previously
              # And converts the format to the correct one because
              # for some reason PIL opens the first frame of gifs
              # completely wrong
              frame.convert("RGB")
            )
          )
        ]
      )
    # this is important but only for macos
    # comment when compiling for other operating systems
    # del self.ims[-1]



  def show(self, delay=50, finish_delay=0, bg=WHITE):
    self.ani = animation.ArtistAnimation(
      self.fig,
      self.ims,
      interval=delay,
      blit=True,
      repeat_delay=finish_delay
    )
    super().show(bg)


# man fuck this. It's not even worth it

# class AniBGImage(Image):
#   def __init__(self, src="images/backup.png", size=(4, 4)):
#     super().__init__(src, size)

#   def show(
#       self,
#       bgs: list[tuple[float, float, float]]=[(1, 1, 1)],
#       delay_s=1):
#     self.fig.patch.set_facecolor(bgs[0])
#     plt.show(block=False)
#     x = 0
#     if plt.get_fignums():
#       self.fig.patch.set_facecolor(bgs[x])
#       x += 1
#       if x >= len(bgs):
#         x = 0

GifImage("images/merged.gif").show(delay=200, bg=BLACK)