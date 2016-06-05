# ##############  set型  ############# #
# 重複できない。順番は存在しない 辞書みたいなもん
s = {1, 2, 3, 4}
s.add(5)
print(s)
print(s & {2, 3, "four"})  # sとの共通集合を表示できる。
s.remove(5)
s2 = {3, 4, 5, 6}
print(s.union(s2))  # くっつけて重複を排除する
print(s.intersection(s2))  # 共通集合を返す
print(s.difference(s2))  # s-s2の残った要素
print(s.symmetric_difference(s2))  # union-intersectionの値。片方に所属

# #############  dictionary  ########### #
rssitem = {"title": "Python",
           "link": "http://host.to/blog/entry",
           "dc:update": "2012-05-16T13:24"
           }
rssitem.update({"ds:creator": "someone"})
print(rssitem.keys())  # keyを返す
print(rssitem)

# for word in line.split():
#     if word in wordcount:  listであるwordcount内にwordがあるかチェック
#         wordcount[word] = wordcount[word]+1  あればカウントを追加
#     else:
#         wordcount[word] = 1 なければ1を追加するがappend()でリストには追加しないらしい
#     wordcount[word] = wordcount.get(word, 0) + 1
#  wordで探してあれば中身を、なければ0を返して1を追加。if より短い

rssitem["json"] = "aaa"  # これで追加できてるからOK
print(rssitem["json"])

print(rssitem.setdefault("title"))  # keyに対応したものを返す、optionでkeyがなかった時の返値を決められる
# さらにその値とkeyをセットしてくれる。入力ミスしたら無限に増える
print(rssitem.values())  # printと同じ



