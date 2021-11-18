from anime2021.anime import ACircle,AShape, AStudio, RollingPolygon, AImage, test_shape, TrailCircle

class nagarebosi(TrailCircle):

  def __init__(self, width=50, height=None, cx=None, cy=None,N=5):
    AShape.__init__(self,width,height,cx,cy)
    self.poly = TrailCircle(width,height,color="white")
    self.irasuto = AImage(width,height, image=irasuto)

  def render(self,canvas,tick):
    self.poly.cx=self.cx
    self.poly.cy=self.cy
    self.irasuto.cx=self.cx
    self.irasuto.cy=self.cy
    self.poly.render(canvas,tick)
    self.irasuto.render(canvas,tick)
