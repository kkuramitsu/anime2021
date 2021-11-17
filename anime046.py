from anime2021.anime import AShape, RollingPolygon, AImage

import IPython

sinamon="https://pics.prcm.jp/647a40a3a449f/85207406/png/85207406.png"
shape = AImage(100,100,image=sinamon)
IPython.display.Image(test_shape(shape))

class GuruGurusinamon(AShape):
  def __init__(self,width=50, height=None, cx=None, cy=None, N=8):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.sinamon=AImage(width, height, image=sinamon)

  def render(self, canvas, tick):
    self.poly.cx=self.cx
    self.poly.cy=self.cy
    self.sinamon.cx=self.cx
    self.sinamon.cy=self.cy
    self.poly.render(canvas, tick)
    self.sinamon.render(canvas, tick)
