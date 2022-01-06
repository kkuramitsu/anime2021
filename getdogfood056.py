!rm -rf anime2021  
!git clone https://github.com/kkuramitsu/anime2021.git
import IPython
from anime2021.anime import *  
from PIL import Image, ImageDraw, ImageFont
from apng import APNG 
EMPTY   = 0
BLOCK   = 1
GOAL    = 2
VISITED = 3

mazedata = '''
XXXXXXXXXXXX
X  XXX X  XX
X      X   X
XX XXX XXX X
X  X X XGX X
XX   X     X
XXXXXXXXXXXX
'''
# maze[(x,y)]

def make_maze(mazedata):
  tbl = {
      ' ': EMPTY,
      'X': BLOCK,
      'G': GOAL,
  }

  maze={}

  for y, line in enumerate(mazedata.split('\n')[1:]):
    for x, c in enumerate(line):
      maze[(x,y)] = tbl[c]

  return x+1, y, maze

X, Y, maze = make_maze(mazedata)
def print_maze(maze, X, Y):
  TBL = {  # 変換テーブルを作っています。
      BLOCK: '🅿️',
      EMPTY: '⛳️',
      GOAL: '😄',
  }
  for y in range(Y):
    for x in range(X):
      print(TBL[maze[(x,y)]], end='')
    print()

print_maze(maze, X, Y)
food='https://1.bp.blogspot.com/-sYFQZVURwuQ/WVd6COv1n9I/AAAAAAABFNc/h-joocViebg0xAx7E-C9MyxIRmQOVgSiQCEwYBhgL/s800/pet_esa_sara_full.png'
block_size = 300 // max(X, Y)
studio = AStudio(300, 300)
for y in range(Y):
  for x in range(X):
    xx = x * block_size + block_size // 2
    yy = y * block_size + block_size // 2



    if maze[(x,y)] == BLOCK:
      block = ARectangle(block_size, block_size, xx, yy, color='pink')
      studio.append(block)
    if maze[(x,y)] == GOAL:
      block = AImage(block_size, block_size, xx, yy,image=food)
      studio.append(block)

inu = 'https://1.bp.blogspot.com/-CpjK6doN9lU/XYhOYM-oK4I/AAAAAAABVHg/68vPZMzgvxUBAYflTAazrX08pgp460KbwCNcBGAsYHQ/s1600/pet_darui_dog.png'
image = AImage(block_size, block_size,100,image=inu)

robot = AImage(block_size, block_size,image=inu)
studio.append(robot)


def set_location(robot, x, y):
  robot.cx = x * block_size + block_size // 2
  robot.cy = y * block_size + block_size // 2

set_location(robot, 1, 1)  
studio.render() 

set_location(robot, 1, 2)
studio.render()

set_location(robot, 2, 2)
studio.render()

set_location(robot, 3, 2)
studio.render()

set_location(robot, 4, 2)
studio.render()

set_location(robot, 5, 2)
studio.render()

set_location(robot, 6, 2)
studio.render()

set_location(robot, 6, 3)
studio.render()

set_location(robot, 6, 4)
studio.render()

set_location(robot, 6, 5)
studio.render()

set_location(robot, 7, 5)
studio.render()

set_location(robot, 8, 5)
studio.render()

set_location(robot, 8, 4)
studio.render()

IPython.display.Image(studio.create_anime(delay=400))
