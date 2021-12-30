!pip install apng
import os, IPython
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

class AStudio(object):
    bodies: list
    frame: int

    def __init__(self, width=400, height=300, background='white'):
        self.width = width
        self.height = height
        self.background = background
        self.bodies = []
        self.files = []
        self.frame = 0
    
    def append(self, shape):
        self.bodies.append(shape) # 被写体を追加する
        return shape

    def render(self, caption=''):
        # 新しいキャンバスを作る
        canvas = ACanvas(self.width, self.height, self.background)
        # リスト上の形状を順番に描画する
        for body in self.bodies:
            body.render(canvas, self.frame)
        # PNG画像に保存する
        filename = f'frame{self.frame}.png'
        canvas.image.save(filename)
        self.files.append(filename)
        self.frame += 1
    
    def create_anime(self, filename='anime.png', delay=100):
        APNG.from_files(self.files, delay=int(delay)).save(filename)
        for image in self.files:
            os.remove(image) # 不要なファイルは消す
        self.files = []
        return filename

class ACanvas(object):
    width:int    #横幅
    height:int   #高さ
    background: any  #背景色
    image: Image
    draw: ImageDraw
    
    def __init__(self, width=400, height=300, background='white'):
        self.width = width
        self.height = height
        self.background = background
        self.image = Image.new('RGBA', (self.width, self.height), self.background)
        self.draw = ImageDraw.Draw(self.image, 'RGBA')

!wget https://3.bp.blogspot.com/-l2e4Wv0g8GM/XLAdOrVvdQI/AAAAAAABSWk/XJPqJNncrWcUG7JoD7m1xepZInDtcFBRACLcBGAs/s800/kotowaza_buta_shinju.png

class RollingPolygon(APolygon):

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

studio = AStudio()
shape = RollingPolygon(width=200, N=5)
studio.append(shape)
studio.append(AImage(width=200, image='kotowaza_buta_shinju.png'))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())
