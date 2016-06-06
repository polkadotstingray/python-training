a = len("asdfghjkl")  # lenで渡せるのは数値以外->桁数を知りたかったらlen(str(nnn))でいいはず
print(a)

b = max(1, 100)
print(b)
c = max([1, 3, -7, 9])
print(c)

print(ord("A")) # 文字列を文字コードに変換している。※数値はエラー

def theuntimitanswer():
    print(42)

theuntimitanswer()

def test(arg):  # 関数を自分で定義できる
    print(arg)  # このブロックに処理を書いておく

test(123)  #作った関数を実行（引数を入れて実行）

def uranai(name, recipes):  # 複数の引数を指定
    print(name,"さんは", sep="", end="")
    print(recipes[ord(name[0]) % len(recipes)],end="")
    print("に似ています")

spam = ['spam', 'egg', 'cheese']
satou = input("name->") # nameにsatouを挿入していく

uranai(satou, spam)
# uranai(10, spam) 2番目のprintでordを使っているのでエラー