from turtle import *

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1: # positionを絶対値に変換 pos()の返値(x,y)の絶対値が(x^2+y^2)^0.5かは不明
        break

print("done")