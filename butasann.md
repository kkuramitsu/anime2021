studio = AStudio()
shape = RollingPolygon(width=200, N=5)
studio.append(shape)
studio.append(AImage(width=200, image='kotowaza_buta_shinju.png'))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())

![image](https://user-images.githubusercontent.com/94042887/147764838-341523fd-061c-49ee-8ac7-8f98611c8d97.png)
