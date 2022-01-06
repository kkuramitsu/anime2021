from anime2021.anime import AShape, ACanvas, AStudio, RollingPolygon, AImage, test_shape
import math
import os, IPython, io, requests
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

souri ='https://1.bp.blogspot.com/-rSrAU03JJbY/YVwDNR5oH1I/AAAAAAABfeI/03tKPPUdT4cWEc-43Y40_bKnFjPWb9JPACNcBGAsYHQ/s937/seiji_souridaijin_kaiken3.png'
shape = AImage(100, 100, image=souri)
IPython.display.Image(test_shape(shape))

kisha ='https://3.bp.blogspot.com/-mm8xgjd7Uu4/WLEuxFBBQgI/AAAAAAABCGU/yQ-G1edCZCsUFfu5p5EU8iuZX4awrywYQCLcB/s800/job_shinbun_kisya.png'
shape = AImage(60, 60, image=kisha)
IPython.display.Image(test_shape(shape))

class Kishakaikenn(AShape):
  def __init__(self,width=50, height=None, cx=None, cy=None,N=10):
    AShape.__init__(self, width, height, cx, cy)
    self.Souri = AImage(width, height, image=souri)
    self.Kisha = AImage(width, height, image=kisha)

  def render(self, canvas, tick):
    self.Souri.cx = self.cx*0.7
    self.Souri.cy = self.cy*0.7
    self.Kisha.cx = self.cx
    self.Kisha.cy = self.cy
    self.Souri.render(canvas, tick)
    self.Kisha.render(canvas, tick)
    
shape = Kishakaikenn(50,50)
IPython.display.Image(test_shape(shape))
