from collections import OrderedDict, defaultdict

od = OrderedDict()
od['a'] = 'A'
od['c'] = 'c'
od['b'] = 'B'
print(od)  # 追加した順番に並べる

d = {}
d['a'] = 'A'
d['c'] = 'C'
d['b'] = 'B'
print(d)  # 順番なんてなかった

animals = [('cat', 'mike'), ('dog', 'kogie'), ('cat', 'sham'), ('dog', 'dax'), ('dog', 'pug')]
d = {}
for k, v in animals:
    if k not in d:  # d 内にkがなければ新規作成
        d[k] = [v]
    else:           # あればリストに追加
        d[k].append(v)

print(d)

d = {}
for k, v in animals:
    d.setdefault(k, []).append(v)
print(d)

dd = defaultdict(list)
for k, v in animals:
    dd[k].append(v)

print(dd)

