clist = [ord(s) for s in "Python"]

alist = []                 # 上の1行をめんどくさく書くと
for s in "Python":         # これになる
    alist.append(ord(s))   # 上の表記を内包表記と呼ぶ

print(clist)
print(alist)
# forの前に式を置いてシーケンスを式に投げて結果をリストに入れられる

sq = [x ** 2 for x in range(10)]
print(sq)

sq2 = [(y, y ** 2) for y in range(10)]
print(sq2)

s = "あいうえお"
rs = "".join([s[-x - 1] for x in range(len(s))])
print(rs)
p = "nisioisin"
if p == "".join(reversed(p)):
    print("reversed")

val = 10
print([x for x in range(1, val) if val % x == 0])
# if (True) の時にxがリストに入れられる

lines = open('test.txt')
print(len([l for l in lines if l.strip() == ""]))

li = [x+y for x in (1, 2, 3) for y in (100, 200, 300)]  # 総当たりを行う
# この時のあたり順は左を固定して右のforを終わらせてからっぽい
print(li)

lis = []  # 上の作業を別表記にするとこうなる。
for x in (1, 2, 3):
    for y in (100, 200, 300):
        lis.append(x + y)
print(lis)

tz = {"GMT": "+000", "BST": "+100",
      "EET": "+200", "JST": "+900"
}
revtz = {value:name for name, value in tz.items()}
print(revtz)  # valueとnameを逆転させて表示している

names = ['BOB', 'Burton', 'dave', 'bob']
unames = {x.title() for x in names}  # namesのsetを区切ってxに投げる->x.titleで加工
print(unames)
