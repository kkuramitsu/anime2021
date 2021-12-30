#グルグル図形  
###anime024.pyに書かれているように以下の分を実行する。
>from anime2021.anime import AStudio, RollingPolygon, AShape, AText, test_shape
 import IPython

>studio = AStudio()
 shape =  RollingPolygon(width=200, N=5, color='orange')
 studio.append(shape)
 studio.append(RollingPolygon(width=200, N=4, color='beige'))
 studio.append(RollingPolygon(width=200, N=3, color='pink'))
 studio.append(AText(width=170, data="spin", color='red'))
 for i in range(60):
     studio.render()
 IPython.display.Image(studio.create_anime())
 
 
