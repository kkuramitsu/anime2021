class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='music_dance_lesson_woman.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            # URLから直接読み込む
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        
studio = AStudio()
shape = RollingPolygon(width=200, N=5)
studio.append(shape)
studio.append(AImage(width=200, image='music_dance_lesson_woman.png'))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())
