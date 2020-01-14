d = "blankit"
k = "kittens"
l = "barret"
n = "latter"
m = 3

p = 'abcdefg'

q = 'efgpoop'
r = 'poopgfe'
s = 'poopabc'
t = 'cbapoop'


str = ''
one = str.join([p[0:len(p)-m], q])
two = str.join([p[0:len(p)-m], r[::-1]])
three = str.join([s[0:len(s)-m], p])
four = str.join([t[::-1][0:len(s)-m], p])
print(one)
print(two)
print(three)
print(four)
