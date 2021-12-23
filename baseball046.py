from anime2021.anime import ACanvas, AShape, AStudio, RollingPolygon, AImage, test_shape

import IPython, math, io, requests
from PIL import Image, ImageDraw, ImageFont
from apng import APNG


ball="https://3.bp.blogspot.com/-5Amsx8iWzrY/VxTO8HOSLtI/AAAAAAAA5-s/CNMdpDaK3Sc0mZ2fo5XHOKkPezAueqCBACLcB/s800/baseball_ball.png"

baseball="https://4.bp.blogspot.com/-quWItRwa6_c/WGYivhxYZ4I/AAAAAAABAto/340idi7Eoe8_rtp-LkI-n88b4Vdpj2PrACLcB/s800/baseball_suburi.png"


class GuruGuruball(AShape):
  def __init__(self,width=30, height=None, cx=None, cy=None, image=ball):
    AShape.__init__(self, width, height, cx, cy)
    if image.startswith('https'):
      self.pic = Image.open(io.BytesIO(requests.get(image).content))
    else:
      self.pic = Image.open(image)
  
  def render(self,canvas: ACanvas, frame: int):
    ox, oy, w, h = self.bounds()
    pic = self.pic.resize((int(w), int(h)))
    canvas.image.paste(pic, (int(ox), int(oy)), pic)

  def BASEBALL(shape, a=100, b=50, c=1, d=1, e=-300):
    studio=AStudio(300,300)
    studio.append(GuruGuruball(width=200,height=200, image=baseball))
    studio.append(shape)
    frames = 5
    for t in range(frames):      
      x = 20 + a*math.cos(c*(2*math.pi*t/frames))
      y = 100 - b*math.sin(d*(2*math.pi*t/frames) + e)
      shape.cx = x
      shape.cy = y
      studio.render()
    return studio.create_anime()
