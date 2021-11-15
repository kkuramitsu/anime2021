from anime2021.anime import AShape, RollingPolygon, AImage

# test

class GuruGuruNami(AShape):
  def __init__(self, width=100, height=None, cx=None, cy=None, N=3):
    AShape.__init__(self, width, height, cx, cy)
    self.N = N
    self.rolling = RollingPolygon(width, height, cx, cy, N)
    self.image = AImage(width, height, cx, cy)

  def render(self, canvas, tick):
    # 描画する前に中心を同期する
    self.rolling.cx = self.cx
    self.rolling.cy = self.cy
    self.image.cx = self.cx
    self.image.cy = self.cy
    self.rolling.render(canvas, tick)
    self.image.render(canvas, tick)
