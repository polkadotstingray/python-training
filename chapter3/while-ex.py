cnt = 0
while cnt < 10:
    print(cnt, end=" ")
    cnt += 1
else:  # for-exと同様に終了時にこのこを呼び出せる
    print("")

# while True: # 無限に続く
#     print("ture")
print("done")

ant = 0
while True:
    print(ant, end=" ")
    ant += 1
    if ant > 10: # ant = 10 の時printをしてからbreakに移るため10も表示される
        break
else:  # for-exと同様に終了時にこのこを呼び出せる
    print("")
