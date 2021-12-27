from anime2021.anime import *

import math
  
class RollingChinchira(AImage):
    
    def __init__(self, width=100, height=None, cx=None, cy=None):
        self.Chinchira_image = AImage(width, height, image=Chinchira_image)
        
    def chinchira_shape(test_shape):
        frames = 50
        for t in range(frames):      
            x = 400 - 8*t
            y = 150
            shape.cx = x
            shape.cy = y
            studio.render()
        return studio.create_anime(delay=50)

    def render(self, canvas: ACanvas, tick: int):
        r = min(self.width, self.height)/2
        for i in range(180):
            slope = math.pi * 2 * 10 * (tick/180)
            ox = self.cx + r * math.cos(i * slope)
            oy = self.cy + r * math.sin(i * slope)
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
    
IPython.display.Image(RollingChinchira(shape))
