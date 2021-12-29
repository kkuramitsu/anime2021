from anime2021.anime import AShape

# デフォルトカラーが水色のハートマークを作ります
class AHeart(AShape):
  color : any

  def __init__(self, color="lightblue", width=50, height=50, cx=None, cy=None):
    AShape.__init__(self, width, height, cx, cy)
    self.color = color
  
  def Render(self, canvas, tick):
    ox, oy, w, h = self.Bounds()
    canvas.draw.pieslice((ox, oy, ox+w//2, oy+h//2), start=180, end=360, fill=self.color)
    canvas.draw.pieslice((ox+w//2, oy, ox+w, oy+h//2), start=180, end=360, fill=self.color)
    canvas.draw.rectangle((ox, oy+h//4, ox+w, oy+h//4+h//8),fill=self.color)
    canvas.draw.polygon(((ox, oy+h//4+h//8), (ox+w//2, oy+h), (ox+w, oy+h//4+h//8)), fill=self.color)
