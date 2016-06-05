s = "iron"
p = "HYDROGEN"

print(s, end=" ")
print(s.upper())

print(p, end=" ")
print(p.lower())

print(s.ljust(10, "*"))
print(s.center(10, "*"))
print(s.rjust(10, "*"))

# #############  差し込み処理  ################# #

t = "{} had a pen."
print(t)  # {}で表示される。
print(t.format("asap"))  # ｛｝がformat()の文字列に置換される。
# 似たような文章の一部変更時に便利

linkstr = '<a href="{}">{}</a>'
for i in [
    'http://python.org',
    'http://pypy.org',
    'http://jython.org'
]:
    print(linkstr.format(i, i.replace('http://', '')))
    # 1つの文字列の中に複数の差し込み処理をするときに,で区切る必要がある？
    print(linkstr.format(i, i))  # 2か所指定しないといけない


