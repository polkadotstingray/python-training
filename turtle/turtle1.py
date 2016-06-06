from turtle import *

forward(100)  # moduleを参照してるから赤いと思われる。動くからよし
left(120)
forward(100)
left(120)
forward(100)

for i in range(6):
    forward(100)
    right(60)

# left,rightで方向転換、時計回りか反時計か。（）で角度
# forwardで線を書く。（）で長さ

