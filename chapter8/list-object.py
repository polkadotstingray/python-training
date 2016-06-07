from decimal import Decimal

l = ["java", 'perl', 'PHP', 'Python', 'Ruby']
print(l)

l.remove('java')
print(l)

s = {"Java", 'Perl', 'PHP', 'Python', 'Ruby'}
print(s)
s.remove('Java')
print(s)

# #########  クラスを使ってみる  ########### #
d = Decimal(10)
print(d + 20)

if Decimal('0.1') * 3 == Decimal('0.3'):
    print('True')

if 0.1 * 3 == 0.3:
    print('True')
else:
    print('False')

print(d.sqrt())
