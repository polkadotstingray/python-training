import sys

f = open("newfile.txt", "w", encoding="utf-8")
f.write("i wrote down to this file")
f.close()

print(sys.getfilesystemencoding())

p = open("6-2.txt", "a")

for i in range(1, 101):
    if i % 3 == 0:
        p.write("spam\n")
    else:
        p.write("{}\n".format(i))

p.close()


