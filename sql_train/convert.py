import glob
import os

os.mkdir('converted')  # ディレクトリを作る


# ADD以降の()の数を数えて内部を区切る
def count_bracket(str, func):           # 対象文字列と対象となる関数
    cnt = 1                             # (があれば+1,)があれば-1。cnt = 0の時ADD_MONTHSは終了
    i = str.index(func) + len(func)           # 関数の開始位置
    bra = 0                             # (のindex
    cket = 0                            # )のindex
    conma = 0                           # ,のindex

    while cnt != 0:                     # ADD_MONTHS()が閉じていない限りループ
        bra = sentence.find("(", i)     # ADD_MONTHS以降で(を探す
        cket = sentence.find(")", i)    # ADD_MONTHS以降で)を探す
        if bra == -1:                   # ADD()で終わりのパターン
            i = cket + 1
            cnt -= 1
        elif bra < cket:                # ADD(())のパターン
            i = bra + 1
            cnt += 1
        elif bra > cket:                # )()のパターン※2週目以降に出てくる可能性アリ
            i = cket + 1
            cnt -= 1
        else:
            print("impossible")

        if cnt == 1:  # 第一引数と第二引数の境界条件で,を探す
            conma = sentence.index(",", i)
    else:
        converted = str[:str.index(func)] + "DATEADD ( month, " + str[conma + 2:cket] + ", " \
                    + str[str.index(func) + len(func):conma] + str[cket:]
        return converted


# print(sentence)
# print(count_bracket(sentence, "ADD_MONTHS("))
for file in glob.glob('*.sql'):  # .sqlのファイルをリストにしてfileに一個づつ入れる
    print(file + "is converting now ...")
    f = open(file, "r")
    sentence = f.read()
    f.close()

    if sentence.find("ADD_MONTHS(") == -1:  # "ADD_MONTHS(がないものは操作対象外とする
        print("file : '" + file + "' has not " + "ADD_MONTHS(")
        break
    w = open("./converted/" + file, "w")  # ./converted/に空のファイルを作成
    w.write(count_bracket(sentence, "ADD_MONTHS("))  # 内容補充
    w.close()

