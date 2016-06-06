from turtle import *

# 角度のリストを登録する
curve = [10, 160, 10, 20]
speed("fastest")

for i in range(40):
    forward(100)
    degree = curve[i % len(curve)]  # i % len(curve)= i mod 4 の計算をしている。
# len() でリストの個数を返す
    right(degree)  # ループするたびに回転する角度が変わる

print(len(curve))