from anime2021.anime import AShape, RollingPolygon, AImage

class GuruGuruSuperman(AShape):
  def __init__(self,width=50,height=None,cx=None,cy=None,N=50):
    AShape.__init__(self,width,height,cx,cy)
    self.poly=RollingPolygon(width,height,N=N)
    self.superman=AImage(width,height,image='superman_hero.png')
  def render(self,canvas,tick):
    self.poly.cx=self.cx
    self.poly.cy=self.cy
    self.superman.cx=self.cx
    self.superman.cy=self.cy
    self.poly.render(canvas,tick)
    self.superman.render(canvas,tick)
