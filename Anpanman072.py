from anime2021.anime import AShape,test_shape,ACanvas,Image

Anpanman='https://pics.prcm.jp/64eda603621c9/82347972/png/82347972.png'

class RollingAnpanman(AShape):
    color: any
    def __init__(self, width=100, height=None, cx=None, cy=None, image=Anpanman):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('https://pics.prcm.jp/64eda603621c9/82347972/png/82347972.png'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox-100), int(oy)), pic)
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        canvas.image.paste(pic, (int(ox+100), int(oy)), pic)
        canvas.image.paste(pic, (int(ox), int(oy+100)), pic)
        canvas.image.paste(pic, (int(ox), int(oy-100)), pic)
