from math import cos, pi, sin
import os
import io
import requests
from PIL import Image, ImageDraw, ImageFont
import random
import math

try:
  from apng import APNG
except ModuleNotFoundError:
  os.system('pip install apng')
  from apng import APNG

# キャンバス

class ACanvas(object):
    width: int  # 横幅
    height: int  # 高さ
    background: any
    image: Image
    draw: ImageDraw

    def __init__(self, width=400, height=300, background='white'):
        self.width = width
        self.height = height
        self.background = background
        self.image = Image.new(
            'RGBA', (self.width, self.height), self.background)
        self.draw = ImageDraw.Draw(self.image, 'RGBA')

# 描画オブジェクト

LEFT = -1
CENTER = 0
RIGHT = 1
TOP = -1
BOTTOM = 1


class AShape(object):
    cx: int
    cy: int
    width: int
    height: int
    scale: float

    def __init__(self, width, height=None, cx=None, cy=None):
        self.width = width
        self.height = width if height is None else height
        self.cx = self.width / 2 if cx is None else cx
        self.cy = self.height / 2 if cy is None else cy
        self.scale = 1.0

    def setPosition(self, x, y, align=(CENTER, CENTER)):
        self.cx = x + (self.width//2) * align[0]
        self.cy = y + (self.height//2) * align[1]

    def bounds(self):
        w = self.width * self.scale
        h = self.height * self.scale
        ox = self.cx - w/2
        oy = self.cy - h/2
        return ox, oy, w, h

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=(127, 127, 127))


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

    def append(self, obj: AShape):
        self.bodies.append(obj)
        return obj

    def render(self, caption=''):
        canvas = ACanvas(self.width, self.height, self.background)
        for body in self.bodies:
            body.render(canvas, self.frame)
        if caption != '':  # キャプションを表示する
            cx = self.width // 2
            cy = self.height - 20
            tw, th = canvas.draw.textsize(caption)
            canvas.draw.rectangle((20, cy-th, self.width-20, cy+th), fill=(0, 0, 0, 0))
            canvas.draw.text((cx-tw/2, cy-th/2), caption, fill='white')
        filename = f'frame{self.frame}.png'
        canvas.image.save(filename)
        self.files.append(filename)
        self.frame += 1

    def create_anime(self, filename='anime.png', delay=200):
        APNG.from_files(self.files, delay=int(delay)).save(filename)
        for image in self.files:
            os.remove(image)  # 不要なファイルは消す
        self.files = []
        return filename

    def anime_demo(self):
        cx = self.width // 2
        cy = self.height // 2
        for i, t in enumerate(range(100)):
            for body in self.bodies:
                px = body.cx - cx
                py = body.cy - cy
                theta = math.atan(px/py) + (math.pi / 90)
                r = math.hypot(px, py)
                px = r * math.cos(theta)
                py = r * math.sin(theta)
                body.setPosition(cx+px, cy+py)
            self.render()
        return self.create_anime()


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


class ARectangle(AShape):
    color: any

    def __init__(self, width=50, height=50, cx=None, cy=None, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.color = get_color(color)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=self.color)


class ACircle(AShape):
    color: any

    def __init__(self, width=10, height=None, cx=None, cy=None, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.color = get_color(color)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.ellipse((ox, oy, ox+w, oy+h), fill=self.color)


class TrailCircle(ACircle):

    def __init__(self, width=10, height=None, cx=None, cy=None, color=None):
        ACircle.__init__(self, width, height, cx, cy, color)

    def render_trail(self, canvas: ACanvas, frame: int):
        if not hasattr(self, 'trails'):
            self.trails = ((self.cx, self.cy),) * min(max(self.width//10, 3), 10)
        r = len(self.trails)+2
        for x, y in self.trails:
            canvas.draw.ellipse((x-r, y-r, x+r, y+r), fill='red')
            r -= 1  # 半径を小さく
        self.trails = ((self.cx, self.cy),) + self.trails[:-1]

    def render(self, canvas: ACanvas, frame: int):
        self.render_trail(canvas, frame)
        super().render(canvas, frame)


class APolygon(AShape):
    color: any
    slope: float

    def __init__(self, width=100, height=None, cx=None, cy=None, N=3, slope=0.0, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.N = N
        self.color = get_color(color)
        self.slope = slope

    def render(self, canvas: ACanvas, frame: int):
        theta = math.pi * 2 / self.N
        r = min(self.width, self.height)/2
        p = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope)
            y = self.cy + r * math.sin(theta*i + self.slope)
            p.append((x, y))
        canvas.draw.polygon(p, fill=self.color)

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

nami_url = 'https://1.bp.blogspot.com/-2ut_UQv3iss/X-Fcs_0oAII/AAAAAAABdD8/jrCZTd_xK-Y6CP1KwOtT_LpEpjp-1nvxgCNcBGAsYHQ/s1055/onepiece03_nami.png'

class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image=nami_url):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)

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

## Text

if os.path.exists('/usr/share/fonts') and not os.path.exists('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'):
  os.system('apt-get -y install fonts-ipafont-gothic')

def get_font(fontsize):
  if os.path.exists('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'):
    return ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', fontsize)
  # Macの場合
  return ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc', fontsize)


class AText(AShape):
    data: str
    font: ImageFont
    color: any

    def __init__(self, width=300, height=None, cx=None, cy=None, data='ABC', font=None, fontsize=None, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.data = data
        self.font = font
        if fontsize is not None:
            self.font = get_font(fontsize)
        self.color = get_color(color)

    def render(self, canvas: ACanvas, frame: int):
        # スーパークラスのメソッドを読んで描画域を確認する
        #AShape.render(self, canvas, frame)
        if self.font is None:
            canvas.draw.text((self.cx, self.cy), str(self.data), fill=self.color)
        else:
            # フォントの大きさをとって位置合わせする
            w, h = canvas.draw.textsize(str(self.data), self.font)
            canvas.draw.text((self.cx - w//2, self.cy-h//2), str(self.data), font=self.font, fill=self.color)

### Misc
  
def monte(n):
    studio = AStudio(200, 200)
    ox, oy = 0, 200
    c = 1
    for n in range(1, n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1.0:
            color = 'pink'
            c += 1
        else:
            color = 'red'
        studio.append(ACircle(10, 10, ox+x*200, oy-y*200, color=color))
        studio.render(f'pi={(4*c/n):.8}')
    studio.create_anime()


#monte(100)


class NoShape(AShape):

    def __init__(self, width, height, cx, cy):
        AShape.__init__(self, width, height, cx, cy)

    def render(self, canvas: ACanvas, frame: int):
        # 何も表示しない
        pass


class ABoard(AShape):
    data: dict

    def __init__(self, w=300, h=None, cx=None, cy=None, data=None, views={0: NoShape}):
        AShape.__init__(self, w, h, cx, cy)
        self.data = {} if data is None else data
        self.views = views

    def get_shape(self, x, y):  # 形状を取る
        shape = self.data.get((x, y), 0)
        if shape in self.views:
            return self.views[shape]
        if shape == 0:
            return NoShape
        if isinstance(shape, str) or isinstance(shape, int):
            #rect = lambda w, h, cx, cy: ARectangle(w, h, cx, cy, color=shape)
            def rect(w, h, cx, cy): return APolygon(
                w, h, cx, cy, N=3, color=shape)
            self.views[shape] = rect
            return rect
        return ARectangle

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        maxX = max(x for x, y in self.data.keys()) + 1
        maxY = max(y for x, y in self.data.keys()) + 1
        dx = w / maxX
        dy = h / maxY
        for i in range(maxX):
            for j in range(maxY):
                cx = ox + dx*i + dx/2
                cy = oy + dy*j + dy/2
                shape = self.get_shape(i, j)
                shape(dx-2, dy-2, cx, cy).render(canvas, frame)

# test_anime()
# test_shape(TrailCircle(width=50))


def test_board():
    studio = AStudio(300, 300)
    board = studio.append(ABoard())
    studio.append(AImage(width=100,
                         image='https://1.bp.blogspot.com/-2ut_UQv3iss/X-Fcs_0oAII/AAAAAAABdD8/jrCZTd_xK-Y6CP1KwOtT_LpEpjp-1nvxgCNcBGAsYHQ/s1055/onepiece03_nami.png'))
    board.data[(5, 4)] = 1
    board.data[(4, 5)] = 2
    studio.render()
    board.data[(2, 2)] = 3
    studio.render()
    board.data[(1, 1)] = 4
    board.data[(1, 3)] = 4
    studio.render()
    board.data[(0, 0)] = 5
    studio.render()

    studio.create_anime()

# test_board()


#test_shape(AText(data='うまく表示される？', fontsize=32))
