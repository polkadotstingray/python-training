import sys

for fn in sys.argv[1:]:
    try:
        f = open(fn)
    except FileNotFoundError:
        print("{}はないんよ".format(fn))
    else:
        try:
            print(fn, len(f.read()))
        finally:
            f.close()

# error の中身と対応については作りつつの方が身に付きそう。
# というか例文がない・・・
