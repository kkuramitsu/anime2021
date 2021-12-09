import os, IPython
from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', 40)
import math
from anime2021.anime import AStudio, AShape, get_color, test_shape, AImage, ARectangle, ACanvas

class ACircle(AShape):
  color: any

  def __init__(self,width=100,height=100,cx=None,cy=None,color=None):
    AShape.__init__(self,width,height,cx,cy)
    self.color=get_color(color)

  def render(self,canvas: ACanvas,frame: int):
    ox,oy,w,h=self.bounds()
    canvas.draw.ellipse((ox,oy,ox+w,oy+h),fill=self.color,outline='#7d7d7d')

class AText(AShape):
    data: str
    font: ImageFont
    color: any

    def __init__(self, width=300, height=None, cx=None, cy=None, data='ABC', font=font, fontsize=None, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.data = data
        self.font = font
        if fontsize is not None:
            self.font = get_font(fontsize)
        self.color = get_color(color)

    def render(self, canvas: ACanvas, frame: int):
        # スーパークラスのメソッドを読んで描画域を確認する
        AShape.render(self, canvas, frame)
        if self.font is None:
            canvas.draw.text((self.cx, self.cy), str(self.data), fill=self.color)
        else:
            # フォントの大きさをとって位置合わせする
            w, h = canvas.draw.textsize(str(self.data), self.font)
            canvas.draw.text((self.cx - w//2, self.cy-h//2), str(self.data), font=self.font, fill=self.color)

class AWing(AShape): # 4枚羽
  color: any

  def __init__(self,width=None,height=None,cx=None,cy=None,color=None):
    AShape.__init__(self,width,height,cx,cy)
    self.color=get_color(color)

  def render(self,canvas: ACanvas, tick: int):
    points=[]
    x1=self.cx
    y1=self.cy
    x2=x1
    y2=y1-self.height/2
    x3=x1+self.width/4
    y3=y2
    points.append((x1,y1,x2,y2,x3,y3))
    y2+=self.height
    x3-=self.width/2
    y3+=self.height
    points.append((x1,y1,x2,y2,x3,y3))
    x2+=self.width/2
    y2=y1
    x3=x2
    y3=y2+self.height/4
    points.append((x1,y1,x2,y2,x3,y3))
    x2-=self.width
    x3=x2
    y3-=self.height/2
    points.append((x1,y1,x2,y2,x3,y3))
    for i in range(4):
      canvas.draw.polygon(points[i],fill=self.color)

class Roline(AShape):
  slope: float
  theta: float
  color: any
  N: int

  def __init__(self,width=None,height=None,cx=None,cy=None,color=None,slope=0.0,theta=None,N=2):
    AShape.__init__(self,width,height,cx,cy)
    self.color=get_color(color)
    self.slope=slope
    self.theta=theta
    self.N=N

  def render(self,canvas: ACanvas,tick: int):
        theta = math.pi * 2 / self.N
        slope = math.pi * 2 * 30 * (tick/360)
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope + slope)
            y = self.cy + r * math.sin(theta*i + self.slope + slope)
            points.append((x,y))
        canvas.draw.line(points,fill=self.color,width=1)

def Fan_png(): #扇風機の画像を作る(fan.png)
  studio=AStudio(400,400)
  shape0= AText(170,50,200,50,color="white",data="mini fan")
  studio.append(shape0)
  shape1=ARectangle(110,30,200,300,color="#afafb0")
  studio.append(shape1)
  shape2 = ACircle(180,40,200,330,color="#c1c1c1")
  studio.append(shape2)
  shape3= ACircle(200,200,200,200,color="#c1c1c1")
  studio.append(shape3)
  shape4 = AWing(170,170,200,200,color='#c5e1f1')
  studio.append(shape4)
  shape5 = Roline(180,180,200,200,theta=30,color="#c5e1f1")
  studio.append(shape5)
  for w in range(90):
    studio.render()
  studio.create_anime(filename='fan.png')
