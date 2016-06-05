# ###########  差し込み処理2  ############# #
s = "{0} {1} {0}"  # 事前に番号をつけておく
print(s.format("pan", "beacon"))  # format内部で番号を振ったものに入れてくれる。
# 何回も同じワードを入れるときにまぁ使いそう
# {}内の数字は文字列なのか数値なのか。数値なら別の関数による出力で操作できるのか

p = ""
for i in range(0, 4):
    p += "{" + str(i) + "}"
print(p.format("1", "2", "3", "4", "5"))  # できたけど別にこういうことがしたいわけじゃない
# format内部に一々記述するのは手間
# ディクショナリーを呼び出せる？

t = "{food1} {food2} {food3} {food1}"
print(t.format(food1='pan', food2='beacon', food3='lettace'))
# どちらの方法も全部羅列する必要あり

dic = {"food1": "pan", "food2": "beacon", "food3": "lettace"}
# print(t.format(dic))  # だめです

d = "{0[food1]} {0[food2]} {0[food3]} {0[food1]}"
print(d.format(dic))  # みんPyの次のページに書いてあった
# 0[key]で先に辞書から呼び出す宣言をする必要がある。できる。

# ###############  差し込み処理3  ################ #
tmpl = "{0:10}{1:>8}"  # :以降の数字と>で寄せる方向と桁合わせができる
print(tmpl.format("spam", 300))

k = 6260 / 12776
print("{:.2%}".format(k))  # 小数点2桁までの表示をしてくれる
print("{:,}".format(100000000))  # カンマで桁区切りしてくれる


