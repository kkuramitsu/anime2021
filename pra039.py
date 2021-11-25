import IPython
from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape

kurage = 'https://4.bp.blogspot.com/-fIDkYYbfqWc/WYlXpOn6RHI/AAAAAAABF68/9d4s4MBxWakSuHu-EEpPbpy5sV2GBceYQCLcBGAs/s400/fish_character_kurage.png'

class GuruGuruKurage(AShape):
  def __init__(self,width=50,height=50,cx=None,cy=None,N=5):
    AShape.__init__(self,width,height,cx,cy)
    self.poly=RollingPolygon(width,height,N=N)
    self.kurage=AImage(width,height,image=kurage)

  def render(self,canvas,tick):
    self.poly.cx=self.cx
    self.poly.cy=self.cy
    self.kurage.cx=self.cx
    self.kurage.cy=self.cy
    self.poly.render(canvas,tick)
    self.kurage.render(canvas,tick)
