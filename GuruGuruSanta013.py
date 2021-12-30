from PIL import Image
from anime2021.anime import AStudio, AShape,  test_shape, ACanvas
import IPython,io,requests,math

small_star7_yellow = 'https://1.bp.blogspot.com/-8FaGc_NoAiU/UYzXHqVasJI/AAAAAAAAR4k/540GCCzmI38/s500/christmas_santa_sori.png'
christmas_santa_sori = 'https://2.bp.blogspot.com/-iLvMf6s3b6M/V0QnoQqvVzI/AAAAAAAA69w/AdU5l6HIy3MX5CTXrfbMNNLbuksyyoC3QCLcB/s800/small_star7_yellow.png'

class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='small_star7_yellow'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        
class AImage2(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='christmas_santa_sori'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        
class GuruGuruSanta(AShape):
    
    def __init__(self, width=100, height=None, cx=None, cy=None, N=3):
        AShape.__init__(self, width, height, cx, cy)
        self.N = N
        self.image = AImage(width, height, cx, cy)
        self.image2 = AImage2(width, height, cx, cy)
    def render(self, canvas, tick):
        self.image.cx = self.cx
        self.image.cy = self.cy
        self.image2.cx = self.cx
        self.image2.cy = self.cy
        self.image.render(canvas, tick)  
        self.image2.render(canvas, tick) 
 
