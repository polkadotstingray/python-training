class StrDict(dict):
    def __init__(self):
        pass

    def __setitem__(self, key, value):  # 既存の__setitem__をオーバーライド
        if not isinstance(key, str):
            raise ValueError("Key must be str or unicode")
        dict.__setitem__(self, key, value)


d = StrDict()
d["spam"] = 1
print(d["spam"])
