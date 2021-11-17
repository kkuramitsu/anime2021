class AAhiru(AShape):
    color: any
    slope: float

    def __init__(self, width=100, height=None, cx=None, cy=None, N=3, slope=0.0, color=None, image='animalface_duck.png'):
        AShape.__init__(self, width, height, cx, cy)
        self.N = N
        self.slope = slope
        self.color = get_color(color)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)
    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 2 / self.N
        slope = math.pi * 2 * 30 * (tick/180) 
        r = min(self.width, self.height)/2
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope + slope)
            y = self.cy + r * math.sin(theta*i + self.slope + slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
