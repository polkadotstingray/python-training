s = "snowslidesystemverticaldropbrainbuster"
if "brain" in s:
    print("brain is found!")

    rssitem = {"title": "Python",
               "link": "http://host.to/blog/entry",
               "dc:update": "2012-05-16T13:24"
               }
rssitem.update({"ds:creator": "someone"})

if "title" in rssitem:
    print("oops")  # rssitemの辞書にkeyがあるか調べる

if "http://host.to/blog/entry" in rssitem.values():
    print("valueを使って値を探した")  # 完全一致でなければいけない
obj = 1
if obj:  # 変数が空でなければTrueを返す
    print(1)

for i in range(20, 9, -1):
    print(i, end="")
else:
    print("")

counter = 0
for item in [1, 2, 3, 4, 5]:
    print(item)
    counter += 1

seq = [1, 2, 3, 4, 5]
for cnt in range(len(seq)):
    print(seq[cnt])

for cnt, item in enumerate(seq):  # enumerateでループカウンタ、シーケンスの中身を返す
    print(cnt, item)

for n, w in zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']):  # 2つのリストをそれぞれタプルにして格納
    print(n, w)

a = [1, 2, 3]
x, y, z = a  # アンパック代入の要領で同時に複数の変数に値を入れることができる
print(x, y, z)
