# f = open("sql.sql", "r")
# temp = f.read()
# f.close()
# print(temp)

sentence = "TR2SR001.DMMN_KIJUN_YMD = CAST(ADD_MONTHS(CAST($[CURRENT_DATE_SYORI] AS DATE), -1) AS INTEGER) / 100"
# ===========================
# ADDと以降の最初の,次の）で検索して区切る方法（ボツ）
# ===========================
# a = sentence.index("ADD_MONTHS(")
# b = sentence.index(",", a)
# print(sentence[a + 11:b])
#
# c = sentence.index(")", b)
# print(sentence[b + 2:c])
# print(sentence[0:a] + "month, " + sentence[b + 2:c] + ", " + sentence[a + 11:b] + ")" + sentence[c + 1:])


# ADD以降の()の数を数えて内部を区切る
def count_bracket(str, func):           # 対象文字列と対象となる関数
    cnt = 1                             # (があれば+1,)があれば-1。cnt = 0の時ADD_MONTHSは終了
    i = str.rindex(func) + 11           # 関数の開始位置
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
                    + str[str.index(func) + 11:conma] + str[cket:]
        return converted

# print(sentence)
print(count_bracket(sentence, "ADD_MONTHS("))

