import math
from anime2021.anime import AShape, AImage ,APolygon,ACanvas,AStudio

def naname(shape, A=100, B=100, a=1, b=1, delta=0):
    # スタジオを用意
    studio = AStudio(300,300)

    # スタジオに被写体を一つ追加する
    studio.append(shape)

    frames = 60
    for t in range(frames):      
        x = 30 + A*t*0.1
        y = 30 + B*t*0.1
        # 被写体の中心を移動させる
        shape.cx = x
        shape.cy = y
        # 全ての移動が終わったら、撮影
        studio.render()

    # 動画を編集して表示する
    return studio.create_anime(delay=50)

class Movemove(APolygon):

    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 2 / self.N
        slope = math.pi * 2 * 30 * (tick/180)  # 自転させる
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope + slope)
            y = self.cy + r * math.sin(theta*i + self.slope + slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)



class Move(AShape):
  def __init__(self, width=100, height=None, cx=None, cy=None, N=3):
    AShape.__init__(self, width, height, cx, cy)
    self.N = N
    self.rolling = Movemove(width, height, cx, cy, N)
    self.image = AImage(width, height, cx, cy)

  def render(self, canvas, tick):
    # 描画する前に中心を同期する
    self.rolling.cx = self.cx
    self.rolling.cy = self.cy
    self.image.cx = self.cx
    self.image.cy = self.cy
    self.rolling.render(canvas, tick)
    self.image.render(canvas, tick)
