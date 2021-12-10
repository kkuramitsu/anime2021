import math

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

from anime2021.anime import AShape, RollingPolygon, AImage

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
