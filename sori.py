import IPython
from anime2021.anime import *

sori_url = 'https://1.bp.blogspot.com/-rIQi1ymlKbo/X9lJoHXKDBI/AAAAAAABc7Y/HGHIRWxT1_8sAzbH6hs0LplsIWPSSQMegCNcBGAsYHQ/s872/sori_snow_girl.png'

class Sorisuberi(AShape):
  color: any

  def __init__(self, width=100, height=None, cx=None,cy=None, image=sori_url):
    AShape.__init__(self, width, height, cx, cy)
    if image.startswith('http'):
      self.pic = Image.open(io.BytesIO(requests.get(image).content))
    else:
      self.pic = Image.open(image)
  
  def render(self, canvas, tick):
    ox, oy, w, h = self.bounds()
    pic = self.pic.resize((int(w), int(h)))
    canvas.image.paste(pic, (int(ox), int(oy)), pic)

  def sorisuberi_shape(shape):
    studio = AStudio(300,300)
    studio.append(shape)
    for i in range(10):
      shape.cx += 10
      shape.cy += 5
      studio.render() 

    for j in range(10):
      shape.cx -= 10
      shape.cy += 5
      studio.render()

    for k in range(10):
      shape.cx += 10
      shape.cy += 5
      studio.render()
    return studio.create_anime(delay=100)
