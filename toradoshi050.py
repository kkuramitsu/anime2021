from anime2021.anime import ACanvas, AShape, AStudio, RollingPolygon, AImage, test_shape
import math
import os, IPython, io, requests
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

tora ='https://1.bp.blogspot.com/-ixn6Lst2PGA/YQs0bRVsxlI/AAAAAAABe9E/XJuLl3RnBNwMo9uHlazF9SBYoNfMJtBcwCNcBGAsYHQ/s400/eto_tora_banzai.png'



class toradoshi(AShape): 
  def __init__(self, width=50, height=None, cx=None, cy=None, N=30):
    AShape.__init__(self, width, height, cx, cy)
    self.Ball=RollingPolygon(width, height, N=N)
    self.Tora=AImage(width=width*2, height=height*2, image=tora)

  def render(self, canvas, tick):
    self.Tora.cx = self.cx
    self.Tora.cy = self.cy
    self.rolling.cx = self.cx
    self.rolling.cy = self.cy
    self.Tora.render(canvas, tick)
    self.rolling.render(canvas, tick)
