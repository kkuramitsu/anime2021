from anime2021.anime import *
import IPython

def test_shape(shape, A=100, B=100, a=1, b=1, delta=0):
    studio = AStudio(400,300,'darkblue')

    studio.append(shape)

    frames = 60
    for t in range(frames):      
        x = 200 + A*math.cos(a*(2*math.pi*t/frames))
        y = 150 - B*math.sin(b*(2*math.pi*t/frames) + delta)
        shape.cx = x
        shape.cy = y
        studio.render()

    return studio.create_anime(delay=50)


santa = 'https://1.bp.blogspot.com/-8FaGc_NoAiU/UYzXHqVasJI/AAAAAAAAR4k/540GCCzmI38/s800/christmas_santa_sori.png'
shape =AImage(152,74,image=santa)
IPython.display.Image(test_shape(shape))
