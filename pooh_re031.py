import IPython
from anime2021.anime import AShape, AStudio, ACanvas, test_shape, ARectangle, APolygon, RollingPolygon 
 

class GuruGuruwashingmachine(AShape): 
  def __init__(self, width=100,height=150, N=None, cx= None, cy=None, color=None):
    AShape.__init__(self,width,height,cx,cy)
    self.squa = ARectangle(width,height,cx=105,cy=155,color='lightgray')
    self.cir = APolygon(width,N=1000,cx=190,cy=20,color='white')
    self.poly = RollingPolygon(width, N=10,cx=105,cy=205,color='skyblue')

  def render(self,canvas,tick):
    self.squa.cx = self.cx
    self.squa.cy = self.cy
    self.cir.cx = self.cx
    self.cir.cy = self.cy
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.squa.render(canvas,tick)
    self.cir.render(canvas,tick)
    self.poly.render(canvas,tick)
