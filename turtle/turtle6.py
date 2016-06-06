from turtle import *

def branch(length):
    """
    長さを引数として受け取って枝を書く。フラクタルみたいな図になる
    """
    if length < 1:  # lengthが10以下になったら終了
        return
    forward(length)
    left(30)
    branch(length/2)  # 内部でもう一回branchを呼び出す。
    right(60)
    branch(length/2) # 右側の枝を書く
    left(30)
    forward(-length) # 分岐点に戻る

branch(200)

print("done")