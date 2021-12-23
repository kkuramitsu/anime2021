from anime2021.anime import AShape, AStudio,RollingPolygon,AImage
import IPython

gori='https://3.bp.blogspot.com/-Zj8Jc4pEVXI/XBC4OkmH8kI/AAAAAAABQ1A/uwmZ7Dzup6QNIKAiO8eHUVOjiIRtnHWtgCLcBGAs/s800/animal_chara_gorilla_girl.png'
banana='https://4.bp.blogspot.com/-t3Fr_Y_xuc0/VNH6f0IGMjI/AAAAAAAArSY/Q0f6FXo84uc/s800/banana_kawa_muke.png'

class GuruGuruGorilla(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.gorilla = AImage(width, height, image=gori)
    self.banana = AImage(width, height, image=banana)

  def render(self, canvas, tick):
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.gorilla.cx = self.cx
    self.gorilla.cy = self.cy
    self.banana.cx = self.cx+50
    self.banana.cy = self.cy+50
    self.poly.render(canvas, tick)
    self.gorilla.render(canvas, tick)
    self.banana.render(canvas, tick)
