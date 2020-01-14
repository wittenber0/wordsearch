import sys

words = []

def loadWords():
    with open(sys.argv[1], "r") as fp:
        l = fp.readline();
        while l:
            words.append(l.rstrip())
            #stats[l.rstrip()] = 0
            l = fp.readline()

def groupWords():
    print("grouping...")
    switched = True
    while switched:
        max = 0
        front = 0
        back = 0
        direction = 0
        for i in range (0, len(words)):
            for j in range (0, len(words)):
                if i == j:
                    continue

                wi = words[i]
                wj = words[j]
                lwi = len(wi)
                lwj = len(wj)
                lmin = lwi if lwi < lwj else lwj

                # i     j
                #last first         0001    1
                #last last          0010    2
                #first last         0100    4
                #first first        1000    8
                remainingTries = 15
                localMax = 0
                localDirection = 0
                #print('%s , %s' % (wi, wj))
                for k in range (1, lmin):
                    ilast = wi[lwi-k:lwi]
                    ifirst = wi[0:k]
                    jlast = wj[lwj-k:lwj]
                    jfirst = wj[0:k]
                    print(wi, ilast, ifirst, wj, jlast, jfirst)

                    if remainingTries & 1 and ilast != jfirst :
                        remainingTries -= 1
                    if remainingTries & 2 and ilast != jlast[::-1] :
                        remainingTries -= 2
                    if remainingTries & 4 and ifirst != jlast :
                        remainingTries -= 4
                    if remainingTries & 8 and ifirst != jfirst[::-1] :
                        remainingTries -= 8


                    print(remainingTries, k)
                    if remainingTries == 0:
                        break

                    if remainingTries > 0 and k > max:
                        print("new max:%s with %s" %(k, remainingTries))
                        print("%s: %s, %s" %(wi, ilast, ifirst))
                        print("%s: %s, %s" %(wj, jlast, jfirst))
                        max = k
                        front = i
                        back = j
                        direction = remainingTries

        if max > 0:
            w = clumpWords(words[front], words[back], max, direction)
            print("%s from %s and %s" % (w, words[front], words[back]))
            if front > back:
                words.pop(front)
                words.pop(back)
            else:
                words.pop(back)
                words.pop(front)
            words.append(w)
            switched = False
        else:
            switched = False

def clumpWords(f, b, m, d):
    if d & 1 :
        str = ''
        o = str.join([f[0:len(f)-m], b])
        return o
    if d & 2 :
        str = ''
        o = str.join([f[0:len(f)-m], b[::-1]])
        return o
    if d & 4 :
        str = ''
        o = sstr.join([b[0:len(b)-m], f])
        return o
    if d & 8 :
        str = ''
        o = str.join([b[::-1][0:len(b)-m], f])
        return o

def printWords():
    for i in words:
        print(i)

def main():
    loadWords()
    groupWords()

main()
