class guruguru3():
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
            self.bodies.append(shape) 
            return shape
        def render(self, caption=''):
            canvas = ACanvas(self.width, self.height, self.background)
            for body in self.bodies:
                body.render(canvas, self.frame)
            filename = f'frame{self.frame}.png'
            canvas.image.save(filename)
            self.files.append(filename)
            self.frame += 1
        def create_anime(self, filename='anime.png', delay=100):
            APNG.from_files(self.files, delay=int(delay)).save(filename)
            for image in self.files:
                os.remove(image)
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
        cx:int #中心点のx
        cy:int #中心点のｙ
        scale:float #スケール
        def __init__(self, width, height=None, cx=None, cy=None):
            self.width = width
            self.height = width if height is None else height
            self.cx = self.width / 2 if cx is None else cx
            self.cy = self.height / 2 if cy is None else cy
            self.scale = 1.0
        def bounds(self):  #左上の座標と幅、高さを計算する
            w = self.width * self.scale
            h = self.height * self.scale
            ox = self.cx - w/2
            oy = self.cy - h/2
            return ox, oy, w, h
        def render(self, canvas: ACanvas, tick: int):
            ox, oy, w, h = self.bounds()
            canvas.draw.rectangle((ox, oy, ox+w, oy+h), fill=(127,127,127))


    class ARectangle(AShape):color: any
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
    def get_color(c): #カラーテーマからランダムに選ぶ
        if c is None:
            return random.choice(ColorTheme)
        if isinstance(c, int):
            return ColorTheme[c % len(ColorTheme)]
        return c

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
            r = min(self.width, self.height)/2
            points = []
            for i in range(self.N):
                x = self.cx + r * math.cos(theta*i + self.slope)
                y = self.cy + r * math.sin(theta*i + self.slope)
                points.append((x, y))
            canvas.draw.polygon(points, fill=self.color)
    class RollingPolygon(APolygon):
        def render(self, canvas: ACanvas, tick: int):
            theta = math.pi * 2 / self.N
            slope = math.pi * 2 * 30 * (tick/180)  
            r = min(self.width, self.height)/2
            points = []
            for i in range(self.N):
                x = self.cx + r * math.cos(theta*i + self.slope + slope)
                y = self.cy + r * math.sin(theta*i + self.slope + slope)
                points.append((x, y))
            canvas.draw.polygon(points, fill=self.color)
            
    class AText(AShape):
        data: str
        color: any
        def __init__(self, width=300, height=None, cx=None, cy=None, data='ABC', color=None):
            AShape.__init__(self, width, height, cx, cy)
            self.data = data
            self.color = get_color(color)
        def render(self, canvas: ACanvas, tick: int):
            canvas.draw.text((self.cx, self.cy), str(self.data), fill=self.color)
            
    import math
    studio = AStudio()
    shape =  RollingPolygon(width=200, N=5, color='orange')
    studio.append(shape)
    studio.append(RollingPolygon(width=200, N=4, color='beige'))
    studio.append(RollingPolygon(width=200, N=3, color='pink'))
    studio.append(AText(width=170, data="spin", color='red'))
    for i in range(60):
    studio.render()
    IPython.display.Image(studio.create_anime())
