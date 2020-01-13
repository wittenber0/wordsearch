import time
import sys

stats = {}
words = []
board = []
answers = []
wordKey = []
n = 5
m = 73
t = 0

def main():

    loadWords()
    loadWordKey()
    words.sort(key = lambda s: -len(s))
    loadBoard()
    start = time.time()
    res = placeWords(words[:])
    stop = time.time()
    t = stop - start
    print(res)
    printBoard(board)
    printAnswers(answers)
    print("Time to generate: %s" %(t))
    print(stats)
    print("solving...")
    s = solve()
    print("Found:")
    printAnswers(s[0])
    print('Not Found:')
    print(s[1])
    if len(s[1]) == 0 :
        writeWordSearch()



def loadWords():
    with open(sys.argv[1], "r") as fp:
        l = fp.readline();
        while l:
            words.append(l.rstrip())
            stats[l.rstrip()] = 0
            l = fp.readline()

def loadWordKey():
    with open(sys.argv[2], "r") as fp:
        l = fp.readline();
        while l:
            wordKey.append(l.rstrip())
            stats[l.rstrip()] = 0
            l = fp.readline()

def loadBoard():
    for i in range (0, n):
        r = []
        for j in range (0, m):
            r.append(0)
        board.append(r)

def placeWord(w, r, c, v):
    #print("placing word %s: at(%s, %s) from v=%s with length=%s" % (w, r, c, v, len(w)))
    #printBoard()
    stats[w] += 1
    if v & 1:
        for i in range (0, len(w)):
            board[r][c+i] = w[i]
        return 1
    if v & 2:
        for i in range (0, len(w)):
            board[r][c-i] = w[i]
        return 2
    if v & 4:
        for i in range (0, len(w)):
            board[r+i][c] = w[i]
        return 4
    if v & 8:
        for i in range (0, len(w)):
            board[r-i][c] = w[i]
        return 8
    if v & 16:
        for i in range (0, len(w)):
            board[r+i][c+i] = w[i]
        return 16
    if v & 32:
        for i in range (0, len(w)):
            board[r+i][c-i] = w[i]
        return 32
    if v & 64:
        for i in range (0, len(w)):
            board[r-i][c+i] = w[i]
        return 64
    if v & 128:
        for i in range (0, len(w)):
            board[r-i][c-i] = w[i]
        return 128

    return 0

def placeWords(bucket):
    global board
    prev = copyBoard(board)

    w = bucket.pop(0)

    for i in range (0, n):
        for j in range (0, m):
            v = fits(w, i, j)
            while v > 0:
                u = placeWord(w, i, j, v)
                answers.append([w, i, j])
                if len(bucket) > 0:
                    valid = placeWords(bucket)
                    if not valid:
                        #print("upchain failed, need to replace %s" % (w))
                        board = copyBoard(prev)
                        v -= u
                    else:
                        return True
                else:
                    return True
    if(len(answers) > 0):
        answers.pop()
    bucket.insert(0, w)
    return False

def countMoves(v):
    moves = 0;
    if v & 1:
        moves += 1
    if v & 2:
        moves += 1
    if v & 4:
        moves += 1
    if v & 8:
        moves += 1
    if v & 16:
        moves += 1
    if v & 32:
        moves += 1
    if v & 64:
        moves += 1
    if v & 128:
        moves += 1
    return moves


def fits(w, r, c):
    l = len(w)
    v = 255;

	#	left to right 				00000001   1
	#	right to left 				00000010   2
	#	top to bottom 				00000100   4
	#	bottom to top 				00001000   8
    #	top-left to bottom-right 	00010000   16
	#	top-right to bottom-left 	00100000   32
	#	bottom-left to top-right	01000000   64
	#	bottom-right to top-left	10000000   128

    if board[r][c] != w[0] and board[r][c] != 0:
        return 0

    #fits
    if c + l > m:
        v -= 1
    if c - l < -1:
        v -= 2
    if r + l > n:
        v -= 4
    if r - l < -1:
        v -= 8
    if not(v & 1 and v & 4):
        v -= 16
    if not(v & 2 and v & 4):
        v -= 32
    if not(v & 1 and v & 8):
        v -= 64
    if not(v & 2 and v & 8):
        v -= 128

    for i in range (1, l):
        if v & 1 and board[r][c+i] != 0 and board[r][c+i] != w[i]:
            v -= 1
        if v & 2 and board[r][c-i] != 0 and board[r][c-i] != w[i]:
            v -= 2
        if v & 4 and board[r+i][c] != 0 and board[r+i][c] != w[i]:
            v -= 4
        if v & 8 and board[r-i][c] != 0 and board[r-i][c] != w[i]:
            v -= 8
        if v & 16 and board[r+i][c+i] != 0 and board[r+i][c+i] != w[i]:
            v -= 16
        if v & 32 and board[r+i][c-i] != 0 and board[r+i][c-i] != w[i]:
            v -= 32
        if v & 64 and board[r-i][c+i] != 0 and board[r-i][c+i] != w[i]:
            v -= 64
        if v & 128 and board[r-i][c-i] != 0 and board[r-i][c-i] != w[i]:
            v -= 128
        if v == 0 :
            break
    return v

def printBoard(b):
    for i in range (0, n):
        print("|", end=' ')
        for j in range (0, m):
            print(b[i][j], end=' ')
        print("|")

def printAnswers(a):
    for i in range(0, len(a)):
        print("%s: %s at (%s, %s)" % (i+1, a[i][0], a[i][1], a[i][2]))

def copyBoard(b):
    out = []
    for i in range (0, n):
        r = []
        for j in range (0, m):
            r.append(b[i][j])
        out.append(r)
    return out

def solve():
    found = []
    notFound = []
    for w in wordKey:
        f = findWord(w)
        if len(f) >1:
            found.append(f)
        else:
            notFound.append(f)
    return([found, notFound])


def findWord(w):
    for i in range(0, n):
        for j in range(0, m):
            if fits(w, i, j) > 0:
                return([w, i, j])
    return([w])

def setBoard():
    global board
    board = [['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], [0, 0, 0, 0, 0], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']]
    printBoard(board)

def testFits():
    global n
    global m
    n = 5
    m = 5
    setBoard()
    loadWords()
    print(stats)
    #r = fits('dog', 2, 2)
    #print(countMoves(r))

def writeWordSearch():
    global board
    f = open("results.txt", "w+")

    for i in range (0, n):

        for j in range (0, m):
            f.write(str(board[i][j]))
            f.write(" ")
        f.write('\n')

    f.write('\n')
    for i in answers:
        seperator = ", "
        e = seperator.join([str(i[1]), str(i[2])])
        seperator = ''
        e2 = seperator.join([i[0], ': ', '(', e, ')'])
        f.write(e2)
        f.write('\n')
    f.close()

#testFits()
main()
