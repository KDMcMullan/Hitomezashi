# Plot Hitomezashi Stitch patters, with set probabilities of
# starting with a stich on either axis.
# Ken McMullan 12-Jan-2022.

from tkinter import *
from random import random, seed

cWidth = 1280 # window
cHeight = 768

pX = 0.25 # probability of starting "on"
pY = 0.75 # probability of starting "on"

grid = 8 # grid size

root = Tk()
frame = Frame(root, width = cWidth, height = cHeight)
frame.pack(expand = True, fill=BOTH)
canvas = Canvas(frame, bg='black', width = cWidth, height = cHeight)

# plot the image

for y in range(0,cHeight,grid):
  alt = random() < pX
  for x in range(0,cWidth,grid):
    if alt:
      canvas.create_line(x,y,x+grid+1,y,fill="white")
    alt = not alt

for x in range(0,cWidth,grid):
  alt = random() < pY
  for y in range(0,cHeight,grid):
    if alt:
      canvas.create_line(x,y,x,y+grid+1,fill="white")
    alt = not alt

canvas.pack(expand = True, fill = BOTH)
root.update()
