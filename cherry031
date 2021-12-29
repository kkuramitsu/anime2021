import IPython
from anime2021.anime import AShape, AStudio, ACanvas, test_shape, ARectangle, APolygon, RollingPolygon 
import math
 
class GuruGuruwashingmachine(AShape): 
  def __init__(self, width=100,height=150, N=None, cx= None, cy=None, color=None):
    studio = AStudio()
    AShape.__init__(self,width,height,cx,cy)
    self.shape = ARectangle(width,height,cx=105,cy=155,color='lightgray')
    self.shape1 = APolygon(width,N=1000,cx=190,cy=20,color='white')
    self.shape2 = RollingPolygon(width, N=10,cx=105,cy=205,color='skyblue')

    
    for i in range(100):
      studio.render()

  def render(self,canvas,tick):
    self.shape.cx = self.cx
    self.shape.cy = self.cy
    self.shape1.cx = self.cx
    self.shape1.cy = self.cy
    self.shape2.cx = self.cx
    self.shape2.cy = self.cy
    self.shape.render(canvas,tick)
    self.shape1.render(canvas,tick)
    self.shape2.render(canvas,tick)

IPython.display.Image(test_shape(GuruGuruwashingmachine()))
