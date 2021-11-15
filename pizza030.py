from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape

pizza='https://4.bp.blogspot.com/-SvHA8OvoyFU/UWya7q7KGzI/AAAAAAAAQiE/Dsd2NDPUF4U/s1600/pizza_margherita.png'
import IPython
class GuruGuruPizza(AShape):
  def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
    AShape.__init__(self, width, height, cx, cy)
    self.poly = RollingPolygon(width, height, N=N)
    self.pizza = AImage(width, height, image=pizza)

  def render(self, canvas, tick):
    self.poly.cx = self.cx
    self.poly.cy = self.cy
    self.pizza.cx = self.cx
    self.pizza.cy = self.cy
    self.poly.render(canvas, tick)
    self.pizza.render(canvas, tick)
