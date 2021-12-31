!rm -rf anime2021  # 再クローンできるように前のファイルを消す
!git clone https://github.com/kkuramitsu/anime2021.git
import IPython

from anime2021.anime import AShape, RollingPolygon, AImage

swimmer = 'https://knsoza1.com/wp-content/uploads/2021/05/5d28bf2c5ebf67d7332fd35b7d68df18.png'

class RollingPolygon(AShape):
  def __init__(self, width=100, height=None, cx=None, cy=None, image=swimmer, scale=1.0):
    AShape.__init__(self, width, height, cx, cy)
    self.N = N
    self.rolling = RollingPolygon(width, height, cx, cy, N)
    self.image = AImage(width, height, cx, cy)

  def render(self, canvas, tick):
    # 描画する前に中心を同期する
    self.rolling.cx = self.cx
    self.rolling.cy = self.cy
    self.image.cx = self.cx
    self.image.cy = self.cy
    self.rolling.render(canvas, tick)
    self.image.render(canvas, tick)
    for i in range(180):
            sx = self.cx + i * math.cos(2 * pi * i /tick)
            sy = self.cy + i * math.sin(2 * pi * i /tick)
    canvas.image.paste(pic, (int(sx), int(sy)), pic)
  def swimmer_shape(shape):

    studio = AStudio(400,400)
    studio.append(shape)
    frames = 50
    for t in range(frames):      
        x = 400 - 5*t
        y = 200
        shape.cx = x
        shape.cy = y
        studio.render()
    return studio.create_anime(delay=50)
