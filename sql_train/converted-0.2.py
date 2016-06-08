import glob
import os

# os.mkdir('converted')  # ディレクトリを作る


# ADD以降の()の数を数えて内部を区切る
def count_bracket(str, func, arg=1):    # 対象文字列と対象となる関数
    cnt = 1                             # (があれば+1,)があれば-1。cnt = 0の時ADD_MONTHSは終了
    i = str.index(func) + len(func)     # 関数の開始位置
    bra = 0                             # (のindex
    cket = 0                            # )のindex
    conma = []                          # ,を記録。argsによって返すパターンが変わる

    while cnt != 0:                     # ADD_MONTHS()が閉じていない限りループ
        if cnt == 1:  # 第一引数と第二引数の境界条件で,を探す
            print(sentence)
            conma.append(sentence.index(",", i))
        bra = sentence.find("(", i)     # ADD_MONTHS以降で(を探す
        cket = sentence.find(")", i)    # ADD_MONTHS以降で)を探す
        if bra == -1:                   # ADD()で終わりのパターン
            i = cket + 1
            cnt -= 1
            print("p1")
        elif bra < cket:                # ADD(())のパターン
            i = bra + 1
            cnt += 1
            print("p2")
        elif bra > cket:                # )()のパターン※2週目以降に出てくる可能性アリ
            i = cket + 1
            cnt -= 1
            print("p3")
        else:
            print("impossible")


    else:
        pre = str[:str.index(func)]
        post = str[cket:]
        if arg == 1:
            return pre, str[str.index(func) + len(func):cket], post

        if arg == 2:
            return pre, str[str.index(func) + len(func):conma[0]], str[conma[0]+1:cket], post

        if arg == 3:
            return pre, str[str.index(func) + len(func):conma[0]], str[conma[0] + 1:conma[1]], \
                   str[conma[1] + 1:cket], post

functions = ["ADD_MONTHS(", "SUBSTR(", "SUBSTRING("]
# 各関数ごとにでループを回す
# print(sentence)
# print(count_bracket(sentence, "ADD_MONTHS("))
for file in glob.glob('*.sql*'):  # .sqlのファイルをリストにしてfileに一個づつ入れる
    # print(file + "is converting now ...")
    f = open(file, "r")
    sentence = f.read()
    f.close()

    for func in functions:  # 各関数ごとにループを回す
        if func == "ADD_MONTHS(":
            while sentence.find(func) != -1:
                if sentence.find(func) == -1:  # "ADD_MONTHS(がないものは操作対象外とする
                    # print("file : '" + file + "' has not " + "ADD_MONTHS(")
                    continue
                w = open("./converted/" + file, "w")  # ./converted/に空のファイルを作成
                pre, arg1, arg2, post = count_bracket(sentence, func, 2)
                sentence = pre + "DATEADD (month, " + arg2 + ", " + arg1 + post
                print("ADD")
                w.write(sentence)  # 内容補充
                w.close()

        elif func == "SUBSTR(":
            while sentence.find(func) != -1:
                if sentence.find(func) == -1:  # "ADD_MONTHS(がないものは操作対象外とする
                    # print("file : '" + file + "' has not " + "ADD_MONTHS(")
                    continue
                w = open("./converted/" + file, "w")  # ./converted/に空のファイルを作成
                pre, arg1, arg2, post = count_bracket(sentence, func, 2)
                print("SUB1")
                sentence = pre + "SUBSTRING (" + arg1 + ", 1, " + arg2 + post
                w.write(sentence)  # 内容補充
                w.close()

        elif func == "SUBSTRING(":
            while sentence.find(func) != -1:
                if sentence.find(func) == -1:  # "ADD_MONTHS(がないものは操作対象外とする
                    # print("file : '" + file + "' has not " + "ADD_MONTHS(")
                    continue
                w = open("./converted/" + file, "w")  # ./converted/に空のファイルを作成
                pre, arg1, post = count_bracket(sentence, func)
                print("SUB2")
                sentence = pre + "SUBSTRING (" + arg1 + ", 1, 4" + post  # あとで修正
                w.write(sentence)  # 内容補充
                w.close()



