from anime2021.anime import AShape, RollingPolygon, AImage

import IPython

doraemon="https://pluspng.com/img-png/png-doraemon-doraemon-new-png-images-411.png"
shape = AImage(100,100,image=doraemon)
IPython.display.Image(test_shape(shape))

class GuruGurusinamon(AShape):
  def __init__(self,width=50, height=None, cx=None, cy=None, N=8):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.doraemon=AImage(width, height, image=doraemon)

  def render(self, canvas, tick):
    self.poly.cx=self.cx
    self.poly.cy=self.cy
    self.doraemon.cx=self.cx
    self.doraemon.cy=self.cy
    self.poly.render(canvas, tick)
    self.doraemon.render(canvas, tick)
