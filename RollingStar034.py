from anime2021.anime import AShape, AStudio, AImage, ACanvas

class AStar(AShape):
  color: any
  slope: float

  def __init__(self, width=100, height=None, cx=None, cy=None, N=5, slope=0.0, color='yellow'):
    AShape.__init__(self, width, height, cx, cy)
    self.N = N
    self.slope = slope
    self.color =color

  def render(self, canvas: ACanvas, frame: int):
    import math
    theta = math.pi * 2 / (self.N * 2)
    # 半径
    r = min(self.width, self.height)/2
    r_out = r #  中心からとげまでの距離(半径)
    r_in = r/2 # 中心から谷までの距離(半径)
    # 頂点の数だけ頂点の座標を計算する
    points = []
    for i in range(self.N * 2):
      if (i%2 == 0):
        R = r_out
      else:
        R = r_in
      x = self.cx + R * math.cos(theta*i + self.slope)
      y = self.cy + R * math.sin(theta*i + self.slope)
      points.append((x, y))
    canvas.draw.polygon(points, fill=self.color)
    
    
class RollingStar(AStar):

  def render(self, canvas: ACanvas, tick: int):
    import math
    theta = math.pi * 2 / (self.N * 2)
    slope = math.pi * 2 * 30 * (tick/180)
    # 半径
    r = min(self.width, self.height)/2
    r_out = r #  中心からとげまでの距離(半径)
    r_in = r/2 # 中心から谷までの距離(半径)
    # 頂点の数だけ頂点の座標を計算する
    points = []
    for i in range(self.N * 2):
      if (i%2 == 0):
        R = r_out
      else:
        R = r_in
      x = self.cx + R * math.cos(theta*i + self.slope + slope)
      y = self.cy + R * math.sin(theta*i + self.slope + slope)
      points.append((x, y))
    canvas.draw.polygon(points, fill=self.color)
    
