from anime2021.anime import AShape, AStudio,RollingPolygon,AImage,test_shape
ikura= 'https://1.bp.blogspot.com/-xonUgxf-ZeI/VD3SAWXBACI/AAAAAAAAoMw/dB8f1xojw0g/s800/food_sushi_ikuradon.png'
shape=AImage(100,100,image=ikura)
IPython.display.Image(test_shape(shape))
class GuruGuruikura(AShape):
    def __init__(self, width=50, height=None, cx=None, cy=None, color=None,N=5):
        AShape.__init__(self, width, height, cx, cy)
        self.poly = RollingPolygon(width,height,N=N)
        self.ikura = AImage(width,height,image=ikura)
    
    def render(self, canvas, tick):
        self.poly.cx=self.cx
        self.poly.cy=self.cy
        self.ikura.cx=self.cx
        self.ikura.cy=self.cy
        self.poly.render(canvas,tick)
        self.ikura.render(canvas,tick)   
