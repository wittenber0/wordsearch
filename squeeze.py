import sys

def main():
    loadWords()
    words.sort(key = lambda s: -len(s))

def loadWords():
    with open(sys.argv[1], "r") as fp:
        l = fp.readline();
        while l:
            words.append(l.rstrip())
            stats[l.rstrip()] = 0
            l = fp.readline()

d = "arkansas"
c = "kansas"
m = 6
str = ''
s = str.join([d[0:len(d)-m], c])

print(s)
