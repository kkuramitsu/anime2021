from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape
import IPython

shokan='https://1.bp.blogspot.com/-P7kfu7ps8cQ/XhwqQ_oKFeI/AAAAAAABW9g/dHjpNuVa-AsOY0fKxY5h_ZHtaymlJnRrwCNcBGAsYHQ/s400/fantasy_mahoujin_syoukan.png'

studio = AStudio()
shape = RollingPolygon(width=160, N=5,color='purple')
studio.append(shape)
shape = RollingPolygon(width=160, N=5,slope=2,color='blue')
studio.append(shape)
shape = RollingPolygon(width=150, N=4,color='green')
studio.append(shape)
shape = AImage(150, 150, image=shokan)
studio.append(shape)

for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())
