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

    def setPosition(self, x, y, align=(0, 0)):
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

class guru:
  studio = AStudio()
  shape =  RollingPolygon(width=200, N=5, color='orange')
  studio.append(shape)
  studio.append(RollingPolygon(width=200, N=4, color='beige'))
  studio.append(RollingPolygon(width=200, N=3, color='pink'))
  studio.append(AText(width=170, data="spin", color='red'))
  for i in range(60):
    studio.render()
  IPython.display.Image(studio.create_anime())
