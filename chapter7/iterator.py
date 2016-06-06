import os

i = iter([1, 2, 3])
# 次の要素を取り出すことと次があるかチェックするだけなので、早い
print(next(i))
print(next(i))
print(next(i))
# print(next(i))  # 3の次が存在しないのでアラート

dic = {1: 1, 2: 2, 3: 3}
for key in dic:
    print(key, end=" ")

for line in open("test.txt"):  # tst.txtを行ごとに処理
    # なにかしらの作業 完全にデータがそろっていなくてもやってくれるので計算が早い
    print(line, end=" ")

# #########  generator  ########## #
# 今までreturnで処理後に反していたものをyieldを使って途中からバンバン返す

def get_primes(x=2):
    while True:
        for i in range(2, x):
            if x % i == 0:  # 約数を発見
                break       # 終了
        else:               # x-1の値までしか調べられないので素数はelseに来る
            yield x         # 素数xを返す
        x += 1              # xに1を追加して続ける

i = get_primes()
for c in range(10):
    print(next(i))

# ============================================== #
#                  これがおしゃれ                  #
# ============================================== #

for dpath, dnames, fnames in os.walk("../"):
    for fname in fnames:              # os.walkで取ってきたfnamesから順番に探していく
        if fname.endswith(".py"):     # .pyで終わってるファイル名の物があればTrue
            print(dpath, ":", fname)  #

"""
ディレクトリツリー以下のファイル名を、ツリーをトップダウンもしくはボトムアップに走査することで作成します。ディレクトリ top
を根に持つディレクトリツリーに含まれる、各ディレクトリ (top 自身を含む ) ごとに、
タプル (dirpath, dirnames, filenames) を yield します。
"""
# アンパックを使ってる。walkで調べるディレクトリを指定
