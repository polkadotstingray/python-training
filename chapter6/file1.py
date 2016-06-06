# Gitの練習含む

f = open("../origin.txt", "r", encoding="utf-8")  # "r"で読み込む
# file1.pyのあるディレクトリから探す。../とかでもっと漁れるかも
s = f.read()
# p = f.readline()
f.close()

f = open("../origin.txt", "r", encoding="utf-8")  # "r"で読み込む
# シーク位置が後ろまでいってるのでリセット
p = f.readline()  # ()内に数字を入れることで文字数を決められる
# d = f.readline()  # 2行目には移る
k = f.readlines()  # 複数行読んでリストにして返す
f.close()

print(s)
print("--------------")
print(p)
# print(d)

print(k)

l = open("foo.txt", "r", encoding="utf-8")
for line in l:
    print(line, end=" ")

