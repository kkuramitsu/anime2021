# ハートマークを作成します
## 使い方
### デフォルト設定のハートマークを作成します
```
studio = AStudio(300, 300)
heart = AHeart()
studio.append(heart)
studio.render()
IPython.display.Image(studio.create_anime(delay=800))
```

### ハートマークの色を変えてみたい場合はこのようなコードになります
```
studio = AStudio(300, 300)
heart = AHeart("lightcoral")
studio.append(heart)
studio.render()
IPython.display.Image(studio.create_anime(delay=800))
```

### 色に加えて、大きさも変えたい場合はこのようなコードになります
```
# 意図的にゆがませるとき以外はwidthとheightの値は同じ方が良いです
studio = AStudio(300, 300)
heart = AHeart("tomato", 100, 100)
studio.append(heart)
studio.render()
IPython.display.Image(studio.create_anime(delay=800))
```
