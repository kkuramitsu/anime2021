!wget https://1.bp.blogspot.com/-OBrXImM0Sd4/X5OcFkxjEnI/AAAAAAABb40/HSDcWu_nYSUbAmRlWro9bHF6pkZJEyFngCNcBGAsYHQ/s789/animal_mawashi_guruma_chinchira.png
!git clone https://github.com/kkuramitsu/anime2021.git
from anime2021.anime import AShape, AStudio, ACanvas, AImage
!pip install apng
import os, IPython
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

import math

def chinchira_shape(shape):
    studio = AStudio(400,300)

    studio.append(shape)

    frames = 50
    for t in range(frames):      
        x = 400 - 8*t
        y = 150
        shape.cx = x
        shape.cy = y
        studio.render()
    return studio.create_anime(delay=50)
  
class RollingChinchira(AImage):

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        r = min(self.width, self.height)/2
        for i in range(180):
            slope = math.pi * 2 * 10 * (tick/180)
            ox = self.cx + r * math.cos(i * slope)
            oy = self.cy + r * math.sin(i * slope)
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
    
IPython.display.Image(chinchira_shape(RollingChinchira()))
