from anime2021.anime import ACanvas, AShape, AStudio, ARectangle


!wget https://1.bp.blogspot.com/-8vjnbp_AXMM/USSkq9AIKTI/AAAAAAAANV0/PQ6FLf-xUks/s1600/alien_ufo.png

!wget https://2.bp.blogspot.com/-A0Rk-ZNi4OI/VXOUSDVDoAI/AAAAAAAAuJU/4NngWeOUZW4/s400/hawaii_maunakea.png

import math

class AUFO(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='alien_ufo.png'):
        AShape.__init__(self, width, height, cx, cy)
        self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)

    def FlyingUFO(shape, A=100, B=100, a=1, b=1, delta=0):
        # スタジオを用意
        studio = AStudio(400,300)

        # スタジオに背景を追加する
        studio.append(AUFO(width=400, height=300, image='hawaii_maunakea.png'))    

        # スタジオにUFOを追加する
        studio.append(shape)

        frames = 60
        for t in range(frames):      
            x = 200 + A*math.cos(a*(2*math.pi*t/frames))
            y = 150 - B*math.sin(b*(2*math.pi*t/frames) + delta)
            # 被写体の中心を移動させる
            shape.cx = x
            shape.cy = y
            # 全ての移動が終わったら、撮影
            studio.render()

        # 動画を編集して表示する
        return studio.create_anime(delay=50)
