class ACircle1(object):    
    width:int  #幅
    height:int #高さ
    cx:int #中心点のx
    cy:int #中心点のy
    scale:float #スケール

    def __init__(self, width, height=None, cx=None, cy=None):
        self.width = width
        self.height = width if height is None else height
        self.cx = self.width / 2 if cx is None else cx
        self.cy = self.height / 2 if cy is None else cy
        self.scale = 1.0

    def bounds(self):  # 左上の座標と幅,高さを計算する
        w = self.width * self.scale
        h = self.height * self.scale
        ox = self.cx - w/2
        oy = self.cy - h/2
        return ox, oy, w, h

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        canvas.draw.ellipse((ox, oy, ox+w, oy+h),outline='blue')
