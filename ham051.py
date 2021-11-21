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

class AShape(object):    
    width:int
    height:int
    cx:int
    cy:int
    scale:float

    def __init__(self, width, height=None, cx=None, cy=None):
        self.width = width
        self.height = width if height is None else height
        self.cx = self.width / 2 if cx is None else cx
        self.cy = self.height / 2 if cy is None else cy
        self.scale = 1.0

    def bounds(self):  # 四隅を計算する
        w = self.width * self.scale
        h = self.height * self.scale
        ox = self.cx - w/2
        oy = self.cy - h/2
        return ox, oy, w, h

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=(127,127,127))

class ARectangle(AShape):
    color: any

    def __init__(self, width=50, height=50, cx=None, cy=None, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.color = get_color(color)

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=self.color)

## カラーテーマ
import random

ColorTheme = [
    '#de9610', '#c93a40', '#fff001', '#d06d8c', '#65ace4', '#a0c238',
    '#56a764', '#d16b16', '#cc528b', '#9460a0', '#f2cf01', '#0074bf',
]

def get_color(c):
    if c is None:
        return random.choice(ColorTheme)
    if isinstance(c, int):
        return ColorTheme[c % len(ColorTheme)]
    return c

import math

def test_shape(shape, A=100, B=100, a=1, b=1, delta=0):
    # スタジオを用意
    studio = AStudio(300,300)

    # スタジオに被写体を一つ追加する
    studio.append(shape)

    frames = 60
    for t in range(frames):      
        x = 150 + A*math.cos(a*(2*math.pi*t/frames))
        y = 150 - B*math.sin(b*(2*math.pi*t/frames) + delta)
        # 被写体の中心を移動させる
        shape.cx = x
        shape.cy = y
        # 全ての移動が終わったら、撮影
        studio.render()

    # 動画を編集して表示する
    return studio.create_anime(delay=50)

class APolygon(AShape):
    color: any
    slope: float # 最初の傾き

    def __init__(self, width=100, height=None, cx=None, cy=None, N=3, slope=0.0, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.N = N
        self.slope = slope
        self.color = get_color(color)

    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 2 / self.N
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope)
            y = self.cy + r * math.sin(theta*i + self.slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)

studio = AStudio()
shape = APolygon(width=200, N=5)
studio.append(shape)
studio.render()

import math
studio = AStudio()
shape = APolygon(width=150, N=5)
studio.append(shape)

for i in range(60):
    shape.slope = (2 * math.pi * i) / 60 
    studio.render()

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
shape = RollingPolygon(width=150, N=16)
studio.append(shape)
for i in range(60):
    studio.render()

!wget https://1.bp.blogspot.com/-bMoxdDzfYoM/WRaS26J5TJI/AAAAAAABEMM/UdsT37sCCsUvi1COVVBWcJIkxETg7m-tQCLcB/s800/animal_hamstert_mawashiguruma.png

class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='animal_hamstert_mawashiguruma.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            # URLから直接読み込む
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)

studio = AStudio()
shape = RollingPolygon(width=200, N=16, color='red')
studio.append(shape)
studio.append(AImage(width=200, image='animal_hamstert_mawashiguruma.png'))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())
