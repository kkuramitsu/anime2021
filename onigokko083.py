from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape
onigokko = 'https://1.bp.blogspot.com/-rFNl6X4--Sk/WMJLQXDlyoI/AAAAAAABCfE/CDKXcIEG2sA92ziYtlXnR_fvFodIrOxwwCLcB/s450/shimekiri_owareru_businesswoman.png'

class Onigokko(AShape):

    def __init__(self, width=100, height=None, cx=None, cy=None, color='#fff001', N=5):
        AShape.__init__(self, width, height, cx, cy)
        self.poly = RollingPolygon(width, height, N=N, color=color)
        self.onigokko = AImage(width, height, image=onigokko)

    def render(self, canvas, tick):
      self.poly.cx = self.cx
      self.poly.cy = self.cy
      self.onigokko.cx = self.cx
      self.onigokko.cy = self.cy
      self.poly.render(canvas, tick)
      self.onigokko.render(canvas, tick)
