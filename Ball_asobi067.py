from anime2021.anime import ACanvas, AShape, AStudio, RollingPolygon, AImage, test_shape
import math
import os, IPython, io, requests
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

inu ='https://3.bp.blogspot.com/-eWUkffYSgLw/Ur1HWZEfLYI/AAAAAAAAces/an_LOPKVFVA/s800/dog_chihuahua.png'
shibahu='https://4.bp.blogspot.com/-rQYpijn8kMQ/VYJrvHrN9VI/AAAAAAAAujY/xm2VHKF3oPM/s800/pattern_shibafu.png'


class Ball_asobi(AShape): 
  def __init__(self, width=50, height=None, cx=None, cy=None, N=30):
    AShape.__init__(self, width, height, cx, cy)
    self.Ball=RollingPolygon(width, height, N=N)
    self.Inu=AImage(width=width*2, height=height*2, image=inu)

  def render(self, canvas, tick):
    self.Inu.cx = self.cx+40
    self.Inu.cy = self.cy-20
    self.Ball.cx = self.cx
    self.Ball.cy = self.cy
    self.Ball.render(canvas, tick)
    self.Inu.render(canvas, tick)
