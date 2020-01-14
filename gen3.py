import sys

def main():
    words = loadWords(sys.argv[1])

    prof = letterProfile(words)
    print(prof)


def loadWords(s):
    words = []
    with open(s, "r") as fp:
        l = fp.readline();
        while l:
            words.append(l.rstrip())
            l = fp.readline()
    return words

def letterProfile(words):
    prof = {}

    for w in words:
        for i in range(0, len(w)):
            if w[i] in prof.keys():
                prof[w[i]] += 1
            else:
                prof[w[i]] = 1
    return prof

def findInWords(words):
    w = words.pop()
    play = []
    for l in w:
        for w in words:
            

main()
