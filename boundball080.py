from anime2021.anime import AShape, ACircle, ACanvas, Image

import math

def boundball(shape, A=100, B=100, a=1, b=1, delta=0):
  studio = AStudio(300,300)
  studio.append(shape)

  frames = 30
  for t in range(frames):
    x = 150 + A*math.cos(a*(math.pi*t/frames))
    y = 150 - B*math.sin(b*(math.pi*t/frames) + delta)
    shape.cx = x
    shape.cy = y
    studio.render()
  for t in range(frames):
    x = 150 - A*math.cos(a*(math.pi*t/frames))
    y = 150 - B*math.sin(b*(math.pi*t/frames) + delta)
    shape.cx = x
    shape.cy = y
    studio.render()

  return studio.create_anime(delay=50)
