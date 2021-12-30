from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape

import IPython
url = 'https://2.bp.blogspot.com/-b0lC9mqjlZM/VJF_M8s2-sI/AAAAAAAApz8/OKUfHncQlPk/s800/animalface_panda.png'
IPython.display.Image(test_shape(shape))

class GuruGuruPanda(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.pien = AImage(width, height, image=url)

  def render(self, canvas, tick):
    #描画する前に中心座標を同期する
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.pien.cx = self.cx
    self.pien.cy = self.cy
    self.poly.render(canvas, tick)
    self.pien.render(canvas, tick)
