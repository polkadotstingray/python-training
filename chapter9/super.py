class Prism:
    def __init__(self, width, height, depth, unit='cm'):
        self.width = width
        self.height = height
        self.depth = depth
        self.unit = unit

    def content(self):
        return self.width * self.height * self.depth

    def unit_content(self):
        return str(self.content()) + self.unit + "^3"


class Cube(Prism):
    def __init__(self, length):
        super().__init__(length, length, length)  # 継承先のinitを呼び出している
# classのinit内でもう一回initを行っているイメージ

c = Cube(20)
print(c.unit_content())

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


class Klass:
    __slots__ = ['a', 'b']

    def __init__(self):
        self.a = 1

i = Klass()
print(i.a)
i.b = 2
print(i.b)
# i.c = 2  # slotsでa,bを指定しているのでcは入れられない
print("------------")


class Prop(object):
    def __init__(self):
        self.__x = 0

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

i = Prop()  # 今までgetter,setterを使わずに呼び出すと、i.__xではなくi.xを勝手に作ってしまっていた
print(i.x)  # ここでx = getxを呼び出すので__xに値が入る（見かけ上はi.x）

i.x = 10    # setxをここで呼び出す。
print(i.x)
print(i._Prop__x)  # 強引に中身を見ているらしい

