from anime2021.anime import AShape, AStudio,RollingPolygon, AImage, test_shape

ball = 'https://1.bp.blogspot.com/-1iDWPBndzRw/XLAc7H1xAyI/AAAAAAABSUE/iUX77Mmnd_cKXdRAwiPS4uQE63BT1vEgQCLcBGAs/s800/character_sports_soccer.png' 
shape = AImage(100,100,image= ball)
IPython.display.Image(test_shape(shape))

class GruGruball(AShape):
   def __init__(self,width=50,height=None,cx=None, cy=None, N=5):
       AShape.__init__(self,width,height,cx,cy)
       self.poly = RollingPolygon(width, height, N=N)
       self.ball = AImage(width, height, image=ball)

   def render(self, canvas, tick):

      self.poly.cx = self.cx
      self.poly.cy = self.cy
      self.ball.cx = self.cx
      self.ball.cy = self.cy
      self.poly.render(canvas, tick)
      self.ball.render(canvas, tick)
