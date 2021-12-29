from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape

class meromerosanji(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=7):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.sanji = AImage(width, height, image=sanji)

  def render(self, canvas, tick):
    #描画する前に中心座標を同期するする
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.sanji.cx = self.cx
    self.sanji.cy = self.cy
    self.poly.render(canvas, tick)
    self.sanji.render(canvas, tick)
