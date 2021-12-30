from anime2021.anime import *
chinchira_url = 'https://1.bp.blogspot.com/-OBrXImM0Sd4/X5OcFkxjEnI/AAAAAAABb40/HSDcWu_nYSUbAmRlWro9bHF6pkZJEyFngCNcBGAsYHQ/s789/animal_mawashi_guruma_chinchira.png'

class RollingChinchira(AImage):
    def __init__(self, width=100, height=100, cx=None, cy=None, image=chinchira_url, scale=1.0):
      self.width = width
      self.height = height
      self.scale = scale
      if image.startswith('http'):
          self.pic = Image.open(io.BytesIO(requests.get(image).content))
      else:
          self.pic = Image.open(image)

    def render(self, canvas: ACanvas, tick: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        r = min(self.width, self.height)/2
        for i in range(180):
            slope = math.pi * 2 * 10 * (tick/180)
            ox = self.cx + r * math.cos(i * slope)
            oy = self.cy + r * math.sin(i * slope)
        canvas.image.paste(pic, (int(ox), int(oy)), pic)

def chinchira_shape(shape):
    studio = AStudio(400,300)
    studio.append(shape)
    frames = 50
    for t in range(frames):      
        x = 400 - 8*t
        y = 150
        shape.cx = x
        shape.cy = y
        studio.render()
    return studio.create_anime(delay=50)
