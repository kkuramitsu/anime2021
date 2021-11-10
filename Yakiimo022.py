imo = 'https://4.bp.blogspot.com/-gFQhyqhny64/WOswK2INfTI/AAAAAAABDwE/yfhjD811kD0IdYrvQVGEvZMBzqIBZfoQQCLcB/s800/sweets_yakiimo.pngshape'
shape = AImage(100,100,image=imo)
IPython.display.Image(test_shape(shape))

class GuruGuruImo(AShape):
    def __init__(self,width=50, height=None, cx=None, cy=None, N=5):
        AShape.__init__(self, width, height, cx, cy)
        self.poly = RollingPolygon(width, height, N=N)
        self.imo = AImage(width, height, image=imo)
    
    def render(self, canvas, tick):
        self.poly.cx = 300- self.cx
        self.poly.cy = 300- self.cy
        self.imo.cx = self.cx
        self.imo.cy = self.cy
        self.poly.render(canvas, tick)
        self.imo.render(canvas, tick)
        
shape = GuruGuruImo(100,100,N=7)
IPython.display.Image(test_shape(shape))
