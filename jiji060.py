from anime2021.anime import AShape, AStudio,RollingPolygon,AImage

class GuruGurujiji(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.nami = AImage(width, height, image=jiji)

  def render(self, canvas, tick):
    #描画する前に中心座標を同期する
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.nami.cx = self.cx
    self.nami.cy = self.cy
    self.poly.render(canvas, tick)
    self.nami.render(canvas, tick)
