!git clone https://github.com/kkuramitsu/anime2021

from anime2021.anime import AShape,AStudio,RollingPolygon,AImage,test_shape

!wget https://3.bp.blogspot.com/-zVqoR4cK0PA/UUhH7n6hv0I/AAAAAAAAO5s/zLOIWix4Jvw/s400/money_chokinbako.png
class GuruGuruNami(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.nami = AImage(width, height, image='money_chokinbako.png')

  def render(self, canvas, tick):
    #描画する前に中心座標を同期するする
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.nami.cx = self.cx
    self.nami.cy = self.cy
    self.poly.render(canvas, tick)
    self.nami.render(canvas, tick)
    
shape=GuruGuruNami(100,100,N=7)
IPython.display.Image(test_shape(shape))
