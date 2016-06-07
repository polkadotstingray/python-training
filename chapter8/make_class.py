class MyClass:
    pass

i = MyClass()

i.value = 5  # .valueは数値を代入するアトリビュート
# アトリビュートがなければ設定できないのか？
j = MyClass()
j = 5
print(i.value)
print(j)     # できたけどこれはMyClassが上書きされてるのではなかろうか

k = MyClass()
k.value = "a"  # 文字列は怒られる
# print(k)

# インスタンス化してからアトリビュート入れてくのも手間
# なのでインスタンス化するときに自動的に呼び出されるものを内部で作る
# （結局一々入れてるのと変わらないと思うが）


class MyClass2:
    def __init__(self):  # selfに値0を代入
        self.value = 0
        print("This is __init__() method")

i3 = MyClass2()  # ここでなぜかprintされる

print(i3.value)  # selfは代入先の自身の名前を指している？
# initでクラスをインスタンス化したときの引数をねじ込むっぽい

print('----------------')
class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width * self.height * self.depth

p = Prism(10, 10, 10)
print(p.content())

p2 = Prism(50, 60, 70)
print(p2.content())

print(p.depth)  # アトリビュートを呼び出すこともできちゃう。そう、クラスならね
p.depth = 50
print(p.depth, p.content())  # self便利
p.depth = "30"  # 文字列を繰り返すやばい事故がおきる
print(p.content())
print('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+')


class Prism2(object):

    def __init__(self, width, height, depth):
        self._width = width
        self._height = height
        self._depth = depth
        self.__private = None

    def content1(self):
        return self._width * self._height * self._depth

p3 = Prism2(10, 10, 10)

print(p3.content1())
# p3.depth = 40
# print(p3.depth)  # depthは書かれるけど_depthはガードされてる
# 別のものとしてセットされる
