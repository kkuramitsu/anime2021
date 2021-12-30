studio = AStudio()
shape = RollingPolygon(width=200, N=5)
studio.append(shape)
studio.append(AImage(width=200, image='kotowaza_buta_shinju.png'))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())

