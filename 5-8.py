def foo(a, b, *vals):  # *をつければ引数の数を上限なしにタプルとして作れる
    print(a, b, vals)

foo(1, 2, 3, 4, 5)

def bar(c, d, **valsa):  # **をつければキーワード指定が可能
    print(c, d, valsa)

bar(1, 2, e=3, f=4)

args = {"src": "srcc", "pri": "print"}
def img_tag(**arg):
    tagstr = "<img "
    for key in arg.keys():
        tagstr += "{}='{} ".format(key, arg[key])
    tagstr += "/>"
    return tagstr

imgString = img_tag(src="/path/to/img.jpg", width=100, height=100, alt="image")
print(imgString)

