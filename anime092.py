from anime2021.anime import AShape

class Rectangle(AShape):
  color : any

  def __init__(self,  width=50, height=50, cx=None, cy=None,color=None):
    AShape.__init__(self, width, height, cx, cy)
    self.color = get_color(color)
  
  def render(self, canvas, tick):
    ox, oy, w, h = self.bounds()
    canvas.draw.rectangle((ox,oy,ox+w,oy+h),fill=self.color)
