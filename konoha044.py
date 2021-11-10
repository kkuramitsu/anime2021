class AMove4(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='onepiece03_nami.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            # URLから直接読み込む
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox+frame*30), int(oy+frame*10)), pic)
