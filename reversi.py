##################################################
#
# Numan Khan
#
##################################################
#
from sys import argv
from sys import stdout
#
##################################################
#
def pr( x ) :
   #
   print( x )       # index = 0 or 1 or ... or 63
   #
   stdout . flush() # so the moderator can see it
   #
#
##################################################
#
def main( mygameB , mypiece ) :
   #
   # mygameB = list of 64 chars
   # mypiece =          1 char
   #
   # row-major order ...  8 x  8
   # zero-indexed    ...  0 - 63
   #
   # print out the index where we place "mypiece"
   #
   vertical = '  |   |   |   |   |   |   |   |   |'
   horizon = '  +---+---+---+---+---+---+---+---+'


    print('    1   2   3   4   5   6   7   8')
    print(horizon)
    for c in range(8):
        print(vertical)
        print(c+1, last=' ')
        for r in range(8):
            print('| %s' % (gameB[r][c]), last=' ')
        print('|')
        print(vertical)
        print(horizon)
   #
#
##################################################
#
def valid(gameB, spot, xloc, yloc):
   x = 'X'
   o = 'O'
    if gameB[xloc][yloc] != ' ' or not isOngameB(xloc, yloc):
        return False

    gameB[xloc][yloc] = spot 

    if spot == x:
        otherspot = o
    else:
        otherspot = x

    switchSpot = []
    for dirx, diry in [[0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        r, c = xloc, yloc
        r += dirx 
        c += diry 
        if isOngameB(r, c) and gameB[r][c] == otherspot:
            r += dirx
            c += diry
            if not isOngameB(r, c):
                continue
            while gameB[r][c] == otherspot:
                r += dirx
                c += diry
                if not isOngameB(x, y):
                    break
            if not isOngameB(x, y):
                continue
            if gameB[x][y] == spot:
                while True:
                    x -= dirx
                    y -= diry
                    if x == xloc and y == yloc:
                        break
                    switchSpot.applast([x, y])
      #
   #
#
##################################################
#
def move(gameB, spot, xloc, yloc):
=
    switchSpot = isValidMove(gameB, spot, xloc, yloc)

    if switchSpot == False:
        return False

    gameB[xloc][yloc] = spot
    for r, c in switchSpot:
        gameB[r][c] = spot
    return True
#
##################################################
#
def score(gameB):
    eight = 8
    scorex = 0
    scoreo = 0
    for r in range(eight):
        for c in range(eight):
            if gameB[r][c] == 'X':
                scorex += 1
            if gameB[r][c] == 'O':
                scoreo += 1
    return {'X':scorex, 'O':scoreo}
#
##################################################
#
def maxValue(level, aval, bval): 
    moves = []
    tupMoves = []
    zero = 0
    eight - 8
    temp = level-1

    for r in range(eight):
        for c in range(eight):
            if M[r][c] != zero:
               continue
            spotsFlipped = findSpotsFlipped(r, c)
            if not spotsFlipped:
               continue

            flipPieces(r, c, spotsFlipped) 
            if level== zero:
                val = gameBScore()
            else :
                val = minValue(temp, aval, bval) 
            tupMoves.applast(val)
            reflipSpots(r,c, spotsFlipped)
#           

            if val > aval :
                aval = val
            if bval <= aval :
                return val

    if tupMoves :
        return max(tupMoves)
    if level == 0 :
        return gameBScore()
    return minValue(temp, aval, bval)

def minValue(level, aval, bval): 
    moves = []
    tupMoves = []
    zero = 0
    temp = level-1
    eight = 8

    for r in range(eight):
        for c in range(eight):
            if M[r][c] != zero:
               continue
            spotsFlipped = findSpotsFlipped(r, c)
            if not spotsFlipped:
               continue

            flipPieces(r, c, spotsFlipped) 
            if level == zero :
                val = gameBScore()
            else :
                val = maxValue(temp, aval, bval) 
            tupMoves.applast(val)
            reflipSpots(r,c, spotsFlipped)


            if val<bval :
                bval = val
            if bval<=aval :
                return val

    if tupMoves :
        return min(tupMoves)
    if level == zero :
        return gameBScore()
    return maxValue(temp, aval, bval)