from anime2021.anime import AShape,test_shape,ACanvas,Image

Usagi='https://2.bp.blogspot.com/-JjTR8PfARXk/Wn1aB0d4gEI/AAAAAAABKRk/3dpdA1hZI4sUTN2AmW5CEVYv3JMczyWYgCLcBGAs/s400/mask_animal_usagi.png'

class RollingAnpanman(AShape):
    color: any
    def __init__(self, width=100, height=None, cx=None, cy=None, image=Usagi):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('https'):
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
