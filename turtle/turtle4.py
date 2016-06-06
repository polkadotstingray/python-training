from turtle import *  # turtle:ある種のお絵かきソフト

speed('fastest')    # 描画スピードと思われる

for i in range(40):  # turtle3 と同じふるまいをifを使って書く。right(10)は2回でるからelseに投げ込む
    forward(100)
    if i % 4 == 1:
        right(160)
    elif i % 4 == 3:
        right(20)
    else:
        right(10)

print("done")