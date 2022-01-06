!wget https://3.bp.blogspot.com/-zVqoR4cK0PA/UUhH7n6hv0I/AAAAAAAAO5s/zLOIWix4Jvw/s400/money_chokinbako.png

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
    width:int #幅
    height:int #高さ
    cx:int #中心点のｘ
    cy:int #中心点のｙ
    scale:float #スケール

    def __init__(self, width, height=None, cx=None, cy=None):
        self.width = width
        self.height = width if height is None else height
        self.cx = self.width / 2 if cx is None else cx
        self.cy = self.height / 2 if cy is None else cy
        self.scale = 1.0

    def bounds(self):  # 左上の座標と幅、高さを計算する
        w = self.width * self.scale
        h = self.height * self.scale
        ox = self.cx - w/2
        oy = self.cy - h/2
        return ox, oy, w, h

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=(127,127,127))
  
IPython.display.Image(test_shape(AImage(image='money_chokinbako.png')))
