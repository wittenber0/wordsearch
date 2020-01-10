words = []
board = []
n = 5;

def main():
    loadWords()
    words.sort(key = lambda s: -len(s))
    loadBoard()
    res = placeWords(words)
    print res
    print board


def loadWords():
    with open("words.txt", "r") as fp:
        l = fp.readline();
        while l:
            words.append(l.rstrip())
            l = fp.readline()

def loadBoard():
    for i in range (0, n):
        r = []
        for j in range (0, n):
            r.append(0)
        board.append(r)

def placeWord(w, r, c, v):
    print("place:")
    print w
    print(r , c)
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
            board[r-i][c+i] = w[i]
        return 8
    if v & 16:
        for i in range (0, len(w)):
            board[r+i][c+i] = w[i]
        return 16
    if v & 32:
        for i in range (0, len(w)):
            board[r-i][c+i] = w[i]
        return 32
    if v & 64:
        for i in range (0, len(w)):
            board[r+i][c-i] = w[i]
        return 64
    if v & 128:
        for i in range (0, len(w)):
            board[r-i][c-i] = w[i]
        return 128

    return 0


def placeWords(bucket):
    w = bucket.pop(0)
    for i in range (0, n):
        for j in range (0, n):
            v = fits(w, i, j)
            print("fits")
            print(w, v)

            while v > 0:
                u = placeWord(w, i, j, v)
                if len(bucket) > 0:
                    valid = placeWords(bucket)
                    if not valid:
                        v -= u
                    else:
                        return True
                else:
                    return True



    return False

def fits(w, r, c):
    l = len(w)
    v = 255;

	#	left to right 				00000001
	#	right to left 				00000010
	#	top to bottom 				00000100
	#	bottom to top 				00001000
    #	top-left to bottom-right 	00010000
	#	top-right to bottom-left 	00100000
	#	bottom-left to top-right	01000000
	#	bottom-right to top-left	10000000

    if board[r][c] != w[0] and board[r][c] != 0:
        return 0

    #fits
    if c + l > n:
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
        if v & 2 and board[r][c-i] != 0 and board[r][c+i] != w[i]:
            v -= 2
        if v & 4 and board[r+i][c] != 0 and board[r+i][c] != w[i]:
            v -= 4
        if v & 8 and board[r][c-i] != 0 and board[r][c-i] != w[i]:
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


main()
