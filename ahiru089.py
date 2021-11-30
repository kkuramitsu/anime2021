from anime2021.anime import ,AShape, AStudio, 

import math

def test_shape2(shape, A=100, B=100, a=5, b=4, delta=-math.pi/4):
    studio = AStudio(300,300)

    studio.append(shape)

    frames = 60
    for t in range(frames):      
        x = 150 + A*math.cos(a*(2*math.pi*t/frames))
        y = 150 - B*math.sin(b*(2*math.pi*t/frames) + delta)
        shape.cx = x
        shape.cy = y
        studio.render()

    return studio.create_anime(delay=1/100000000000)

  class Ahiru(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='furo_ducky.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas2, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)

!wget https://3.bp.blogspot.com/-9i7uW0JycJc/UZmCRl25KCI/AAAAAAAATfc/5uBk-6YxV_Q/s800/furo_ducky.png

IPython.display.Image(test_shape2(Ahiru(image='furo_ducky.png')))
