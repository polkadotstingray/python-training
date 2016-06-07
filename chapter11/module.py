from math import sin, radians
import testmodule  # *は重複するモジュール名があった場合上書きするので注意

# import math   # モジュール内の関数を呼び出す時にfromを使う

print(10 * 20 * sin(radians(45)) / 2)
print(testmodule.a)
testmodule.foo()
print(testmodule.sys.argv)

