from anime2021.anime import AShape, AStudio, RollingPolygon, AImage, test_shape, ACanvas, AText
import IPython
shape = RollingPolygon(100, 100, N=4)
IPython.display.Image(test_shape(shape))
tree = 'https://2.bp.blogspot.com/-iPxVfxnIS28/XJB4szPInUI/AAAAAAABR5U/PtRjqO-35uIkFXoIO6m_VYWtQb1kTqj5wCLcBGAs/s150/christmas_mark_check1_tree.png'
shape = AImage(100,100,image=tree)
IPython.display.Image(test_shape(shape))
studio = AStudio()
shape = RollingPolygon(width=200, N=10, color='yellow')
studio.append(shape)
studio.append(AImage(width=200, image=tree))
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())
