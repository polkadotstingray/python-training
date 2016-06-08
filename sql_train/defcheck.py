cnt = 1  # (があれば+1,)があれば-1。cnt = 0の時ADD_MONTHSは終了

bra = 0  # (のindex
cket = 0  # )のindex
conma = []
arg = 2
func = "SUBSTRING("
sentence = "WHERE SUBSTRING(IH1IH001.CASH_RECORD_ID FROM 1 FOR 8) >= '20121229'"
print()
i = sentence.index(func) + len(func)  # 関数の開始位置
str = sentence

while cnt != 0:  # ADD_MONTHS()が閉じていない限りループ
    if cnt == 1:  # 第一引数と第二引数の境界条件で,を探す
        print(sentence)
        conma.append(sentence.find(",", i))
    bra = sentence.find("(", i)  # ADD_MONTHS以降で(を探す
    cket = sentence.find(")", i)  # ADD_MONTHS以降で)を探す
    if bra == -1:  # ADD()で終わりのパターン
        i = cket + 1
        cnt -= 1
        print("p1")
    elif bra < cket:  # ADD(())のパターン
        i = bra + 1
        cnt += 1
        print("p2")
    elif bra > cket:  # )()のパターン※2週目以降に出てくる可能性アリ
        i = cket + 1
        cnt -= 1
        print("p3")
    else:
        print("impossible")

else:
    pre = str[:str.index(func)]
    post = str[cket:]
    if arg == 1:
        # return pre, str[str.index(func) + len(func):cket], post
        print(pre, str[str.index(func) + len(func):cket], post)
    elif arg == 2:
        # return pre, str[str.index(func) + len(func):conma[0]], str[conma[0] + 1:cket], post
        print(pre, str[str.index(func) + len(func):conma[0]], str[conma[0] + 1:cket], post)
    elif arg == 3:
        # return pre, str[str.index(func) + len(func):conma[0]], str[conma[0] + 1:conma[1]], \
              # str[conma[1] + 1:cket], post
        print(pre, str[str.index(func) + len(func):conma[0]], str[conma[0] + 1:conma[1]], \
               str[conma[1] + 1:cket], post)
