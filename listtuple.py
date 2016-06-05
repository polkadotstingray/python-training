a = [1, 2, 3, 4, 5]
print(a)
print(a[1:4])
# [ 1 2 3 4 5 ]
#  0 1 2 3 4 5  リストに対してのindexの数字の関係
# [1:4]1の後ろから4の前までを引っ張る
print(a[2:100])  # index外を指定しても怒られない
print(a[::2])  # 偶数番目を取り出す<-正確には2個おきに取り出す
# [::1]ではリストがフルで表示。たぶんデフォルトが::1

a[2:4] = ['Three', 'Four', 'Five']
print(a)  # [1, 2, 3, 4, 5] の3,4の要素2個を3つに置き換える
del a[2:]
print(a)  # index2以降を削除

b = 1
c = 2
b, c = c, b  # 同時に入れ替える代入が可能
print(b, c)  # 一旦変数dに避難させる必要がなくなる

# ##########  ソート  ######### #
def to_lower(s):
    return s.lower()

print(to_lower("S"))

d = ["abc", "def", "BCC", "EGG"]
d.sort()  # この時に中身が書き換わっている
print(d)
d.sort(key=to_lower, reverse=True)  # reverse=Trueのキーワードで反転ができる
# ソートするときにlowerが呼ばれるので小文字で比較する
print(d)

print(d.pop())  # indexで指定したものを取り出して返す。指定しなければ一番最後のものを返す

