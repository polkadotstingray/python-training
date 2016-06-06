from turtle import *

degree = 1
distance = 50

for i in range(40):
    forward(distance)  # 50の長さを線を描く（1回目）
    right(degree)      # 方向転換
    degree += 2        # 回転する角度を増していく
    distance -= 1      # 線の長さを短くしていく

input()  # 最後の行になんか書いておかないと怒られる