from calendar import TUESDAY
from http.client import UNPROCESSABLE_ENTITY
from pickle import FALSE
from re import M
from types import TracebackType
from urllib.parse import non_hierarchical
from cmu_graphics import *

app.rows = 8
app.cols = 8
board = makeList(app.rows, app.cols)

boardHorizPos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
boardVertPos = ['8', '7', '6', '5', '4', '3', '2', '1']

pROpacity = 0

def drawLabel(value, x, y):
    Label(value, x, y, size = 20)

def drawBoard():
    for row in range(app.rows):

        for col in range(app.cols):
            if col % 2 == 0 and row % 2 == 1 or col % 2 == 1 and row % 2 == 0:
                color = "maroon"
            else:
                color = "navajoWhite"

            r = Rect(40 + col * 40, 40 + row * 40, 40, 40, fill = color, opacity = 80)
            r.vert = boardVertPos[row]
            r.horiz = boardHorizPos[col]
            board[row][col] = r
            if row == 0:
                lblValue = boardHorizPos[col]
                lblX = 60 + col * 40
                lblY = 20
                drawLabel(lblValue, lblX, lblY)
                lblY = 380
                drawLabel(lblValue, lblX, lblY)

        lblValue = boardVertPos[row]
        lblY = 60 + row * 40
        lblX = 20
        drawLabel(lblValue, lblX, lblY)
        lblX = 380
        drawLabel(lblValue, lblX, lblY)

drawBoard()

whiteQueens = []

blackQueens = []

whiteKing = Group()
whiteKing.name = 'White King'

blackKing = Group()
blackKing.name = 'Black King'

whiteRooks = []
blackRooks = []

whiteKnights = []
blackKnights = []

whiteBishops = []
blackBishops = []

whitePawns = []
blackPawns = []

app.pcsSqrOffset = 19
app.pcsSqrSize = 38

def drawQueen(fill, x, y):
    spikeX = x
    spikeX -= 30
    spikeRotateAngle = -45

    queen = Group()

    for i in range(5):
   
        
        spikeX += 10
        spikeRotateAngle += 15
       
        queen.add(Polygon(spikeX, y-2, spikeX+5, y+50-2, spikeX-5, y+50-2, fill = fill, rotateAngle = spikeRotateAngle, border = 'black', borderWidth = 1))
        
    for i in range(3):
 
        queen.add(Oval(x, y+50 + 5 * i, 35, 20, fill = fill, border = 'black', borderWidth = 1))
    
    
    queen.height = 35
    queen.width = 35
    queen.centerX = x
    queen.centerY = y

    queen.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))

    if fill == 'navajoWhite':
        queen.name = 'White Queen'
        whiteQueens.append(queen)

    else:
        queen.name = 'Black Queen'
        blackQueens.append(queen)
    
def drawKing(fill, x, y):
    
    if fill == 'navajoWhite':
        whiteKing.add(Oval(x, y, 70, 40, fill = fill, border = 'black', borderWidth = 1),
        Polygon(x, y - 25, x-10, y+ 20, x+10, y+20, fill = fill, border = 'black', borderWidth = 1),
        Circle(x, y - 20, 8, fill = fill, border = 'black', borderWidth = 1),)
        for i in range(3):
            whiteKing.add(Oval(x, y+18 +5*i, 50, 20, fill = fill, border = 'black', borderWidth = 1))
        whiteKing.height = 35
        whiteKing.width = 35
        whiteKing.centerX = x
        whiteKing.centerY = y
        whiteKing.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))
        
    else:
        blackKing.add(Oval(x, y, 70, 40, fill = fill, border = 'black', borderWidth = 1),
        Polygon(x, y - 25, x-10, y+ 20, x+10, y+20, fill = fill, border = 'black', borderWidth = 1),
        Circle(x, y - 20, 8, fill = fill, border = 'black', borderWidth = 1),)
        for i in range(3):
            blackKing.add(Oval(x, y+18 +5*i, 50, 20, fill = fill, border = 'black', borderWidth = 1))
        blackKing.height = 35
        blackKing.width = 35
        blackKing.centerX = x
        blackKing.centerY = y
        blackKing.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))

def drawRook(fill, x, y):
    
    rook = Group()
    rook.add(Polygon(x, y+30, x, y, x+10, y, x+10,
    y+10, x+20, y+10, x+20, y, x+30, y, x+30,
    y+10, x+40, y+10, x+40, y, x+50, y, x+50,
    y+30, fill = fill, border = 'black', borderWidth = 1))

    rook.add(Oval(x+25, y+50, 50, 20, fill = fill, border = 'black', borderWidth = 1))
    rook.add(Oval(x+25, y+47, 40, 15, fill = fill, border = 'black', borderWidth = 1))
    rook.add(Rect(x+10, y+29, 30, 21, fill = fill, border = 'black', borderWidth = 1))

    rook.add(Rect(x+10, y+49, 30, 1, fill= fill))
    
    rook.width = 29
    rook.height = 35
    rook.centerX = x
    rook.centerY = y

    rook.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))

    
    if fill == 'navajoWhite':
        rook.name = 'White Rook'
        whiteRooks.append(rook)
    else:
        rook.name = 'Black Rook'
        blackRooks.append(rook)
    
def drawKnight(fill, x, y):
    knight = Group()
    
    knight.add(Oval(x+16, y+26.5, 35, 13, fill = fill, border = 'black', borderWidth = 1))
    
    knight.add(Polygon(x, y, x+10, y-10, x+10, y -12, x+15, y-17, x+15,
    y-25, x+20, y-17, x+25, y-12, x+30, y-3, x+30, y+8, x+25,
    y+18, x+25, y+25, x+8, y+25, x+8, y+15, x+12, y+8,
    x+12, y+4, x+8, y+2, x+1, y+4, fill = fill, border = 'black', borderWidth = 1))
    
    knight.add(Oval(x+16, y+25, 25, 8, fill = fill, border = 'black', borderWidth = 1))
    
    knight.add(Rect(x+9, y+18, 15, 5, fill = fill))
    
    knight.width = 21
    knight.height = 35
    knight.centerX = x
    knight.centerY = y

    knight.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))
    
    if fill == 'navajoWhite':
        knight.name = 'White Knight'
        whiteKnights.append(knight)
    else:
        knight.name = 'Black Knight'
        blackKnights.append(knight)

def drawBishop(fill, x, y):
    bishop = Group()
    
    bishop.add(Oval(x, y+43, 50, 25, fill = fill, border = 'black', borderWidth = 1))
    bishop.add(Oval(x, y+40, 40, 15, fill = fill, border = 'black', borderWidth = 1))
    bishop.add(Polygon(x-10, y+10, x+10, y+10, x+15, y+40, x-15, y+40, fill = fill, border = 'black', borderWidth = 1))
    
    head = Group(Arc(x, y, 30, 35, -10, 250, fill = fill, border = 'black', borderWidth = 1),
    Arc(x-5, y+1, 30, 35, 100, 245, fill = fill, border = 'black', borderWidth = 1),
    Arc(x-2, y+3, 30, 26, 70, 180, fill = fill))
    head.rotateAngle -= 30
    head.centerX = x
    
    bishop.add(head)
    
    bishop.add(Circle(x, y-23, 8, fill = fill, border = 'black', borderWidth = 1))
    bishop.add(Rect(x-13, y+36, 26, 5, fill = fill))
    
    bishop.width = 20
    bishop.height = 35
    
    bishop.centerX = x
    bishop.centerY = y

    bishop.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))
    
    if fill == 'navajoWhite':
        bishop.name = 'White Bishop'
        whiteBishops.append(bishop)
    else:
        bishop.name = 'Black Bishop'
        blackBishops.append(bishop)

def drawPawn(fill, x, y):
    pawn = Group(
    
    Oval(x, y+37, 40, 15, fill = fill, border = 'black', borderWidth = 1),
    Oval(x, y+35, 35, 12, fill = fill, border = 'black', borderWidth = 1),
    Polygon(x-5, y+10, x+5, y+10, x+10, y+25, x+15, y+35, x-15, y+35, x-10, y+25, fill = fill, border = 'black', borderWidth = 1),
    Oval(x, y+10, 20, 10, fill = fill, border = 'black', borderWidth = 1),
    Circle(x, y, 10, fill = fill, border = 'black', borderWidth = 1),
    Rect(x-13, y+34, 26, 2, fill = fill))
    
    pawn.width = 18.3
    pawn.height = 25
    pawn.centerX = x
    pawn.centerY = y

    pawn.add(Rect(x - app.pcsSqrOffset, y - app.pcsSqrOffset, app.pcsSqrSize, app.pcsSqrSize, opacity = pROpacity))

    if fill == 'navajoWhite':
        pawn.name = 'White Pawn'
        whitePawns.append(pawn)
    else:
        pawn.name = 'Black Pawn'
        blackPawns.append(pawn)

for i in range(2):
    y = 60 + 280 * i
    
    if i == 0:
        fill = 'maroon'
    
    else:
        fill = 'navajoWhite'

    x = 180
    drawQueen(fill, x, y)

    x = 220
    drawKing(fill, x, y)

for i in range(2):
    d = 40
    dBish = 3*d
    dKni = 5*d
    dRoo = 7*d

    

    x = 140 + dBish * i

    y1 = 340
    fill1 = 'navajoWhite'
    y2 = 60
    fill2 = 'maroon'

    drawBishop(fill1, x, y1)
    drawBishop(fill2, x, y2)

    x = 100 + dKni * i

    drawKnight(fill1, x, y1)
    drawKnight(fill2, x, y2)

    x = 60 + dRoo * i

    drawRook(fill1, x, y1)
    drawRook(fill2, x, y2)

for i in range(8):
    x = 60 + 40 * i
    y = 300
    # if i < 7:
    drawPawn('navajoWhite', x, y)
    y = 100
    drawPawn('maroon', x, y)

whitePieces = []
blackPieces = []

whitePieces.append(whiteKing)
whitePieces.append(whiteQueens[0])

blackPieces.append(blackKing)
blackPieces.append(blackQueens[0])

for i in range(2):
    whitePieces.append(whiteBishops[i])
    whitePieces.append(whiteKnights[i])
    whitePieces.append(whiteRooks[i])
    blackPieces.append(blackBishops[i])
    blackPieces.append(blackKnights[i])
    blackPieces.append(blackRooks[i])

for i in range(8):
    # if i < 7:
    whitePieces.append(whitePawns[i])
    blackPieces.append(blackPawns[i])

selectedMarkers = Group()
moveMarkers = Group()

def selectPiece(playerMove, mouseX, mouseY):
    piece = None
    pieceSelected = False
    if playerMove == 'white':
        for i in range(len(whitePieces)):
            if pieceSelected == False:
                if whitePieces[i].hits(mouseX, mouseY):
                    x = whitePieces[i].centerX
                    y = whitePieces[i].centerY
                    pieceSelected = True
                    selectedMarkers.add(Circle(x, y, 15, fill = 'lime', opacity = 50))
                    piece = whitePieces[i]
    elif playerMove == 'black':
        for i in range(len(blackPieces)):
            if pieceSelected == False:
                if blackPieces[i].hits(mouseX, mouseY):
                    x = blackPieces[i].centerX
                    y = blackPieces[i].centerY
                    pieceSelected = True
                    selectedMarkers.add(Circle(x, y, 15, fill = 'lime', opacity = 50))
                    piece = blackPieces[i]
    selectedMarkers.toFront()
    return piece

def checkPawnMoves(playerMove, x, y):

    if playerMove == 'white':

        for row in range(app.rows):

            for col in range(app.cols):

                if board[row][col].hits(x, y):
                    ### check move in front
                    moveFront = True
                    moveFrontLeft = False
                    moveFrontRight = False
                    moveTwoFront = True

                    for i in range(len(blackPieces)):
                        targetX = blackPieces[i].centerX
                        targetY = blackPieces[i].centerY

                        if moveFront == True:

                            if board[row-1][col].hits(targetX, targetY):
                                moveFront = False
                            if row-2 != -1:
                                if board[row-2][col].hits(targetX, targetY):
                                    moveTwoFront = False
                            else:
                                moveTwoFront = False

                        if moveFrontLeft == False:

                            if board[row][col].horiz != 'A':

                                if board[row-1][col-1].hits(targetX, targetY):
                                    moveFrontLeft = True

                                elif app.blackLastMove[0] == 'Black Pawn' and app.blackLastMove[1] == 'TwoFront':
                                    if board[row][col-1].hits(app.blackLastMove[2], app.blackLastMove[3]):
                                        moveFrontLeft = True

                        if moveFrontRight == False:

                            if board[row][col].horiz != 'H':

                                if board[row-1][col+1].hits(targetX, targetY):
                                    moveFrontRight = True

                                elif app.blackLastMove[0] == 'Black Pawn' and app.blackLastMove[1] == 'TwoFront':
                                    if board[row][col+1].hits(app.blackLastMove[2], app.blackLastMove[3]):
                                        moveFrontRight = True



                    for i in range(len(whitePieces)):
                        if moveFront == True:
                            targetX = whitePieces[i].centerX
                            targetY = whitePieces[i].centerY
                            if board[row-1][col].hits(targetX, targetY):
                                moveFront = False
                            if board[row-2][col].hits(targetX, targetY):
                                moveTwoFront = False
                    if board[row][col].vert != '2':
                        moveTwoFront = False

                    if moveFront == True:
                        addMoveMarker(row-1, col)

                    if moveTwoFront == True:
                        addMoveMarker(row-2, col)

                    if moveFrontLeft == True:
                        addMoveMarker(row-1, col-1)
                    if moveFrontRight == True:

                        addMoveMarker(row-1, col+1)

    elif playerMove == 'black':
        for row in range(app.rows):
            for col in range(app.cols):
                if board[row][col].hits(x, y):
                    ### check move in front
                    moveFront = True
                    moveFrontLeft = False
                    moveFrontRight = False
                    moveTwoFront = True
                    for i in range(len(whitePieces)):
                        targetX = whitePieces[i].centerX
                        targetY = whitePieces[i].centerY
                        if moveFront == True:
                            if board[row+1][col].hits(targetX, targetY):
                                moveFront = False
                            if row+2 != 8:
                                if board[row+2][col].hits(targetX, targetY):
                                    moveTwoFront = False
                            else:
                                moveTwoFront = False
                        if moveFrontLeft == False:

                            if board[row][col].horiz != 'A':

                                if board[row+1][col-1].hits(targetX, targetY):

                                    moveFrontLeft = True
                                
                                elif app.whiteLastMove[0] == 'White Pawn' and app.whiteLastMove[1] == 'TwoFront':

                                    if board[row][col-1].hits(app.whiteLastMove[2], app.whiteLastMove[3]):

                                        moveFrontLeft = True

                        if moveFrontRight == False:
                            if board[row][col].horiz != 'H':

                                if board[row+1][col+1].hits(targetX, targetY):

                                    moveFrontRight = True

                                elif app.whiteLastMove[0] == 'White Pawn' and app.whiteLastMove[1] == 'TwoFront':

                                    if board[row][col+1].hits(app.whiteLastMove[2], app.whiteLastMove[3]):

                                        moveFrontRight = True

                    for i in range(len(blackPieces)):
                        if moveFront == True:
                            targetX = blackPieces[i].centerX
                            targetY = blackPieces[i].centerY

                            if board[row+1][col].hits(targetX, targetY):
                                moveFront = False

                            if board[row+2][col].hits(targetX, targetY):
                                moveTwoFront = False
                                
                    if board[row][col].vert != '7':
                        moveTwoFront = False

                    if moveFront == True:
                        addMoveMarker(row+1, col)

                    if moveTwoFront == True:
                        addMoveMarker(row+2, col)

                    if moveFrontLeft == True:
                        addMoveMarker(row+1, col-1)

                    if moveFrontRight == True:
                        addMoveMarker(row+1, col+1)

def checkKnightMoves(playerMove, x, y):

    for row in range(app.rows):

        for col in range(app.cols):

            if board[row][col].hits(x, y):

                vert = board[row][col].vert
                horiz = board[row][col].horiz

                moveUpL = True
                moveUpR = True
                moveRUp = True
                moveRDown = True
                moveDownR = True
                moveDownL = True
                moveLDown = True
                moveLUp = True

                if vert == '1':
                    moveRDown = False
                    moveDownR = False
                    moveDownL = False
                    moveLDown = False

                elif vert == '2':
                    moveDownR = False
                    moveDownL = False
                
                elif vert == '8':
                    moveUpL = False
                    moveUpR = False
                    moveRUp = False
                    moveLUp = False

                elif vert == '7':
                    moveUpL = False
                    moveUpR = False
                
                if horiz == 'A':
                    moveUpL = False
                    moveDownL = False
                    moveLDown = False
                    moveLUp = False
                
                elif horiz == 'B':
                    moveLDown = False
                    moveLUp = False

                elif horiz == 'H':    
                    moveUpR = False
                    moveRUp = False
                    moveRDown = False
                    moveDownR = False

                elif horiz == 'G':
                    moveRDown = False
                    moveRUp = False

                if playerMove == 'white':

                    for i in range(len(whitePieces)):

                        targetX = whitePieces[i].centerX
                        targetY = whitePieces[i].centerY

                        if moveUpL == True:

                            if board[row-2][col-1].hits(targetX, targetY):
                                moveUpL = False
                        
                        if moveUpR == True:

                            if board[row-2][col+1].hits(targetX, targetY):
                                moveUpR = False
                        
                        if moveRUp == True:

                            if board[row-1][col+2].hits(targetX, targetY):
                                moveRUp = False

                        if moveRDown == True:

                            if board[row+1][col+2].hits(targetX, targetY):
                                moveRDown = False

                        if moveDownR == True:

                            if board[row+2][col+1].hits(targetX, targetY):
                                moveDownR = False

                        if moveDownL == True:

                            if board[row+2][col-1].hits(targetX, targetY):
                                moveDownL = False

                        if moveLDown == True:

                            if board[row+1][col-2].hits(targetX, targetY):
                                moveLDown = False

                        if moveLUp == True:

                            if board[row-1][col-2].hits(targetX, targetY):
                                moveLUp = False
                
                elif playerMove == 'black':

                    for i in range(len(blackPieces)):

                        targetX = blackPieces[i].centerX
                        targetY = blackPieces[i].centerY

                        if moveUpL == True:

                            if board[row-2][col-1].hits(targetX, targetY):
                                moveUpL = False
                        
                        if moveUpR == True:

                            if board[row-2][col+1].hits(targetX, targetY):
                                moveUpR = False
                        
                        if moveRUp == True:

                            if board[row-1][col+2].hits(targetX, targetY):
                                moveRUp = False

                        if moveRDown == True:

                            if board[row+1][col+2].hits(targetX, targetY):
                                moveRDown = False

                        if moveDownR == True:

                            if board[row+2][col+1].hits(targetX, targetY):
                                moveDownR = False

                        if moveDownL == True:

                            if board[row+2][col-1].hits(targetX, targetY):
                                moveDownL = False

                        if moveLDown == True:

                            if board[row+1][col-2].hits(targetX, targetY):
                                moveLDown = False

                        if moveLUp == True:

                            if board[row-1][col-2].hits(targetX, targetY):
                                moveLUp = False

                if moveUpL == True:

                    addMoveMarker(row-2, col-1)

                if moveUpR == True:

                    addMoveMarker(row-2, col+1)

                if moveRUp == True:

                    addMoveMarker(row-1, col+2)

                if moveRDown == True:

                    addMoveMarker(row+1, col+2)

                if moveDownR == True:

                    addMoveMarker(row+2, col+1)

                if moveDownL == True:

                    addMoveMarker(row+2, col-1)

                if moveLDown == True:

                    addMoveMarker(row+1, col-2)

                if moveLUp == True:

                    addMoveMarker(row-1, col-2)

def checkRookMoves(playerMove, x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            if board[row][col].hits(x, y):
                
                vert = board[row][col].vert
                horiz = board[row][col].horiz

                moveUp = True
                nextUp = False
                moveDown = True
                nextDown = False
                moveR = True
                nextR = False
                moveL = True
                nextL = False

                if vert == '8':
                    moveUp = False
                elif vert == '1':
                    moveDown = False

                if horiz == 'A':
                    moveL = False
                elif horiz == 'H':
                    moveR = False

                countUp = 1
                while moveUp == True:
                    if row-countUp == -1:
                        moveUp = False
                    
                    if moveUp == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    nextUp = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    nextUp = True

                    if moveUp == True:
                        addMoveMarker(row-countUp, col)
                        
                    if nextUp == True:
                        addMoveMarker(row-countUp, col)
                        
                    countUp += 1

                countDown = 1

                while moveDown == True:
                    
                    if row+countDown == 8:
                        moveDown = False

                    if moveDown == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                    nextDown = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                    nextDown = True
                
                    if moveDown == True:
                        addMoveMarker(row+countDown, col)
                        
                    if nextDown == True:
                        addMoveMarker(row+countDown, col)
                        
                    countDown += 1

                countR = 1
                while moveR == True:
                    if col+countR == 8:
                        moveR = False

                    if moveR == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    nextR = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    nextR = True

                    if moveR == True:
                        addMoveMarker(row, col+countR)

                    if nextR == True:
                        addMoveMarker(row, col+countR)

                    countR += 1
                    

                countL = 1
                while moveL == True:
                    if col-countL == -1:
                        moveL = False

                    if moveL == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                    nextL = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                    nextL = True

                    if moveL == True:
                        addMoveMarker(row, col-countL)
                    if nextL == True:
                        addMoveMarker(row, col-countL)
                    countL += 1
                    
def checkBishopMoves(playerMove, x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            if board[row][col].hits(x, y):
                vert = board[row][col].vert
                horiz = board[row][col].horiz

                moveUpL = True
                nextUpL = False
                moveUpR = True
                nextUpR = False
                moveDownL = True
                nextDownL = False
                moveDownR = True
                nextDownR = False

                if vert == '8':
                    moveUpL = False
                    moveUpR = False
                elif vert == '1':
                    moveDownL = False
                    moveDownR = False

                if horiz == 'H':
                    moveUpR = False
                    moveDownR = False
                elif horiz == 'A':
                    moveUpL = False
                    moveDownL = False

                countUpL = 1
                while moveUpL == True:
                    if col-countUpL == -1:
                        moveUpL = False
                    elif row-countUpL == -1:
                        moveUpL = False
                    
                    if moveUpL == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    nextUpL = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    nextUpL = True
                                    
                    if moveUpL == True:
                        addMoveMarker(row-countUpL, col-countUpL)
                    elif nextUpL == True:
                        addMoveMarker(row-countUpL, col-countUpL)
                    countUpL += 1
                
                countUpR = 1
                while moveUpR == True:
                    if col+countUpR == 8:
                        moveUpR = False
                    elif row-countUpR == -1:
                        moveUpR = False
                    
                    if moveUpR == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    nextUpR = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    nextUpR = True
                                    
                    if moveUpR == True:
                        addMoveMarker(row-countUpR, col+countUpR)
                    elif nextUpR == True:
                        addMoveMarker(row-countUpR, col+countUpR)
                    countUpR += 1

                countDownL = 1
                while moveDownL == True:
                    if col-countDownL == -1:
                        moveDownL = False
                    elif row+countDownL == 8:
                        moveDownL = False
                    
                    if moveDownL == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    nextDownL = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    nextDownL = True

                    if moveDownL == True:
                        addMoveMarker(row+countDownL, col-countDownL)
                    elif nextDownL == True:
                        addMoveMarker(row+countDownL, col-countDownL)
                    countDownL += 1
                    
                countDownR = 1
                while moveDownR == True:
                    if col+countDownR == 8:
                        moveDownR = False
                    elif row+countDownR == 8:
                        moveDownR = False
                    
                    if moveDownR == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    nextDownR = True

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    nextDownR = True
                                    
                    if moveDownR == True:
                        addMoveMarker(row+countDownR, col+countDownR)
                    elif nextDownR == True:
                        addMoveMarker(row+countDownR, col+countDownR)
                    countDownR += 1

def checkKingMoves(playerMove, x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            if board[row][col].hits(x, y):
                vert = board[row][col].vert
                horiz = board[row][col].horiz

                moveUpL = True
                UpLX = x-40
                UpLY = y-40

                moveUp = True
                UpX = x
                UpY = y-40

                moveUpR = True
                UpRX = x+40
                UpRY = y-40

                moveR = True
                RX = x+40
                RY = y

                moveDownR = True
                DownRX = x+40
                DownRY = y+40

                moveDown = True
                DownX = x
                DownY = y+40

                moveDownL = True
                DownLX = x-40
                DownLY = y+40

                moveL = True
                LX = x-40
                LY = y

                if playerMove == 'white':
                    for i in range(len(whitePieces)):
                        if moveUpL == True:
                            if whitePieces[i].hits(UpLX, UpLY):
                                moveUpL = False

                        if moveUp == True:
                            if whitePieces[i].hits(UpX, UpY):
                                moveUp = False

                        if moveUpR == True:
                            if whitePieces[i].hits(UpRX, UpRY):
                                moveUpR = False

                        if moveR == True:
                            if whitePieces[i].hits(RX, RY):
                                moveR = False

                        if moveDownR == True:
                            if whitePieces[i].hits(DownRX, DownRY):
                                moveDownR = False

                        if moveDown == True:
                            if whitePieces[i].hits(DownX, DownY):
                                moveDown = False

                        if moveDownL == True:
                            if whitePieces[i].hits(DownLX, DownLY):
                                moveDownL = False

                        if moveL == True:
                            if whitePieces[i].hits(LX, LY):
                                moveL = False

                elif playerMove == 'black':
                    for i in range(len(blackPieces)):
                        if moveUpL == True:
                            if blackPieces[i].hits(UpLX, UpLY):
                                moveUpL = False

                        if moveUp == True:
                            if blackPieces[i].hits(UpX, UpY):
                                moveUp = False

                        if moveUpR == True:
                            if blackPieces[i].hits(UpRX, UpRY):
                                moveUpR = False

                        if moveR == True:
                            if blackPieces[i].hits(RX, RY):
                                moveR = False

                        if moveDownR == True:
                            if blackPieces[i].hits(DownRX, DownRY):
                                moveDownR = False

                        if moveDown == True:
                            if blackPieces[i].hits(DownX, DownY):
                                moveDown = False

                        if moveDownL == True:
                            if blackPieces[i].hits(DownLX, DownLY):
                                moveDownL = False

                        if moveL == True:
                            if blackPieces[i].hits(LX, LY):
                                moveL = False

                if vert == '1':
                    moveDownR = False
                    moveDown = False
                    moveDownL = False
                elif vert == '8':
                    moveUpR = False
                    moveUp = False
                    moveUpL = False

                if horiz == 'H':
                    moveUpR = False
                    moveR = False
                    moveDownR = False
                elif horiz == 'A':
                    moveUpL = False
                    moveL = False
                    moveDownL = False

                if moveUpL == True:
                    addMoveMarker(row-1, col-1)

                if moveUp == True:
                    addMoveMarker(row-1, col)
                
                if moveUpR == True:
                    addMoveMarker(row-1, col+1)

                if moveR == True:
                    addMoveMarker(row, col+1)

                if moveDownR == True:
                    addMoveMarker(row+1, col+1)
                
                if moveDown == True:
                    addMoveMarker(row+1, col)

                if moveDownL == True:
                    addMoveMarker(row+1, col-1)

                if moveL == True:
                    addMoveMarker(row, col-1)
 
def checkWhiteRocked():
    if app.whiteRookLStart == True:
        lRocked = True
        for i in range(len(whitePieces)):
            if whitePieces[i].hits(180, 340) or whitePieces[i].hits(140, 340) or whitePieces[i].hits(100, 340):
                lRocked = False
        if lRocked == True:
            for i in range(len(blackPieces)):
                if blackPieces[i].hits(180, 340) or blackPieces[i].hits(140, 340) or blackPieces[i].hits(100, 340):
                    lRocked = False
        if lRocked == True:
            addMoveMarker(7, 2)

    if app.whiteRookRStart == True:
        rRocked = True
        for i in range(len(whitePieces)):
            if whitePieces[i].hits(260, 340) or whitePieces[i].hits(300, 340):
                rRocked = False
        if rRocked == True:
            for i in range(len(blackPieces)):
                if blackPieces[i].hits(260, 340) or blackPieces[i].hits(300, 340):
                    rRocked = False
        if rRocked == True:
            addMoveMarker(7, 6)
        
def checkBlackRocked():
    if app.blackRookLStart == True:
        lRocked = True
        for i in range(len(whitePieces)):
            if whitePieces[i].hits(180, 60) or whitePieces[i].hits(140, 60) or whitePieces[i].hits(100, 60):
                lRocked = False
        if lRocked == True:
            for i in range(len(blackPieces)):
                if blackPieces[i].hits(180, 60) or blackPieces[i].hits(140, 60) or blackPieces[i].hits(100, 60):
                    lRocked = False
        if lRocked == True:
            addMoveMarker(0, 2)

    if app.blackRookRStart == True:
        rRocked = True
        for i in range(len(whitePieces)):
            if whitePieces[i].hits(260, 60) or whitePieces[i].hits(300, 60):
                rRocked = False
        if rRocked == True:
            for i in range(len(blackPieces)):
                if blackPieces[i].hits(260, 60) or blackPieces[i].hits(300, 60):
                    rRocked = False
        if rRocked == True:
            addMoveMarker(0, 6)

def addMoveMarker(row, col):
    moveMarkers.add(Circle(board[row][col].centerX, board[row][col].centerY, 15, fill = 'red', opacity = 50))
    moveMarkers.toFront()

def movePiece(targetX, targetY):

    pos = None

    for marker in moveMarkers.children:

        if pos == None:

            if marker.hits(targetX, targetY):

                pos = [marker.centerX, marker.centerY]

    return pos

def newTurn():
    if app.playerMove == 'white':
        app.playerMove = 'black'
    elif app.playerMove == 'black':
        app.playerMove = 'white'           
    print('newTurn was called and next player is', app.playerMove)         

def posPiece(pos, oldPos):
    
    dx = pos[0]-oldPos[0]
    dy = pos[1]-oldPos[1]

    if app.playerMove == 'white':
        
        if app.whiteLastMove[0] == 'White Pawn' and (app.whiteLastMove[1] == 'FrontLeft' or app.whiteLastMove[1] == 'FrontRight'):
            passantWipe()
        elif app.whiteLastMove[0] == 'White Rook':
            if oldPos[0] == 60:
                app.whiteRookLStart = False
            elif oldPos[0] == 340:
                app.whiteRookRStart = False
        elif app.whiteLastMove[0] == 'White King':
            if dx == 80:
                x = 340
                y = 340
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                ### check if king is threatened
                x = 220
                
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                if app.legalMove == True:        
                    posRocked('right', app.playerMove)
                
            elif dx == -80:
                ### check if rook is threatened
                x = 60
                y = 340
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                ### check if king is threatened

                x = 220
                
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                if app.legalMove == True:        
                    posRocked('left', app.playerMove)

            if app.legalMove == True:

                app.whiteKingStart = False

    elif app.playerMove == 'black':
        
        if app.blackLastMove[0] == 'Black Pawn' and (app.blackLastMove[1] == 'FrontLeft' or app.blackLastMove[1] == 'FrontRight'):
            passantWipe()
        elif app.blackLastMove[0] == 'Black Rook':
            if oldPos[0] == 60:
                app.blackRookLStart = False
            elif oldPos[0] == 340:
                app.blackRookRStart = False
        elif app.blackLastMove[0] == 'Black King':
            if dx == 80:
                ### check if rook is threatened
                x = 340
                y = 60
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                ### check if king is threatened
                x = 220
                
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)


                if app.legalMove == True:        
                    posRocked('right', app.playerMove)


                    
            elif dx == -80:
                ### check if rook is threatened
                x = 60
                y = 60
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                x = 220
                
                if app.legalMove == True:
                    checkIfPosIsThreatened(app.playerMove, x, y)

                if app.legalMove == True:        
                    posRocked('left', app.playerMove)
            
            if app.legalMove == True:

                app.blackKingStart = False

    if app.legalMove == True:
        app.piece.centerX = pos[0]
        app.piece.centerY = pos[1]

        if app.playerMove == 'white':
            if app.whiteLastMove[0] == 'White Pawn' and pos[1] == 60:
                switchPawn(app.playerMove, pos[0], pos[1])
        elif app.playerMove == 'black':
            if app.blackLastMove[0] == 'Black Pawn' and pos[1] == 340:
                switchPawn(app.playerMove, pos[0], pos[1])
            
def checkIfPosIsThreatened(playerMove, x, y):
    for i in range(4):
        angle = 45 + 90 * i
        if app.legalMove == True:
            app.legalMove = threatCheckDiagonal(playerMove, angle, x, y, x, y, x, y)

    for i in range(4):
        angle = 90 * i
        if app.legalMove == True:
            app.legalMove = threatCheckVertHoriz(playerMove, angle, x, y, x, y, x, y)

    if app.legalMove == True:
        app.legalMove = threatCheckKnights(playerMove, x, y, x, y)

def passantWipe():
    if app.playerMove == 'white':
        x = app.whiteLastMove[2]
        y = app.whiteLastMove[3] + 40

        for i in range(len(blackPieces)):
            if blackPieces[i].hits(x, y):
                if app.blackLastMove[1] == 'TwoFront' and app.blackLastMove[2] == x and app.blackLastMove[3] == y:
                    delPiece = blackPieces.pop(i)
                    for j in range(len(blackPawns)):
                        if delPiece.hitsShape(blackPawns[j]):
                            blackPawns.pop(j)
                            break
                    delPiece.visible = False
                    break
    elif app.playerMove == 'black':
        x = app.blackLastMove[2]
        y = app.blackLastMove[3] - 40
        for i in range(len(whitePieces)):
            if whitePieces[i].hits(x, y):
                if app.whiteLastMove[1] == 'TwoFront' and app.whiteLastMove[2] == x and app.whiteLastMove[3] == y:
                    delPiece = whitePieces.pop(i)
                    for j in range(len(whitePawns)):
                        if delPiece.hitsShape(whitePawns[j]):
                            whitePawns.pop(j)
                            break
                    delPiece.visible = False
                    break

def posRocked(dir, playerMove):
    if playerMove == 'white':
        if dir == 'right':
            for i in range(len(whiteRooks)):
                if whiteRooks[i].hits(340, 340):
                    whiteRooks[i].centerX = 260
        elif dir == 'left':
            for i in range(len(whiteRooks)):
                if whiteRooks[i].hits(60, 340):
                    whiteRooks[i].centerX = 180
    
    elif playerMove == 'black':
        if dir == 'right':
            for i in range(len(blackRooks)):
                if blackRooks[i].hits(340, 60):
                    blackRooks[i].centerX = 260
        elif dir == 'left':
            for i in range(len(blackRooks)):
                if blackRooks[i].hits(60, 60):
                    blackRooks[i].centerX = 180

def wipePiece():
    if app.playerMove == 'white':
        listLen = len(blackPieces)
        for i in range(len(blackPieces)):
            if len(blackPieces) == listLen:
                if app.piece.hitsShape(blackPieces[i]):
                    
                    if blackPieces[i].name == 'Black Pawn':
                        for j in range(len(blackPawns)):
                            if app.piece.hitsShape(blackPawns[j]):
                                blackPawns.pop(j)
                                
                                break

                    elif blackPieces[i].name == 'Black Rook':
                        for j in range(len(blackRooks)):
                            if app.piece.hitsShape(blackRooks[j]):
                                blackRooks.pop(j)
                                break

                    elif blackPieces[i].name == 'Black Bishop':
                        for j in range(len(blackBishops)):
                            if app.piece.hitsShape(blackBishops[j]):
                                blackBishops.pop(j)
                                break

                    elif blackPieces[i].name == 'Black Knight':
                        for j in range(len(blackKnights)):
                            if app.piece.hitsShape(blackKnights[j]):
                                blackKnights.pop(j)
                                break

                    elif blackPieces[i].name == 'Black Queen':
                        for j in range(len(blackQueens)):
                            if app.piece.hitsShape(blackQueens[j]):
                                blackQueens.pop(j)
                                break

                    delPiece = blackPieces.pop(i)
                    delPiece.visible = False
        newTurn()

    elif app.playerMove == 'black':
        listLen = len(whitePieces)
        for i in range(len(whitePieces)):
            if len(whitePieces) == listLen:
                if app.piece.hitsShape(whitePieces[i]):

                    if whitePieces[i].name == 'White Pawn':
                        for j in range(len(whitePawns)):
                            if app.piece.hitsShape(whitePawns[j]):
                                whitePawns.pop(j)
                                break

                    elif whitePieces[i].name == 'White Rook':
                        for j in range(len(whiteRooks)):
                            if app.piece.hitsShape(whiteRooks[j]):
                                whiteRooks.pop(j)
                                break

                    elif whitePieces[i].name == 'White Bishop':
                        for j in range(len(whiteBishops)):
                            if app.piece.hitsShape(whiteBishops[j]):
                                whiteBishops.pop(j)
                                break

                    elif whitePieces[i].name == 'White Knight':
                        for j in range(len(whiteKnights)):
                            if app.piece.hitsShape(whiteKnights[j]):
                                whiteKnights.pop(j)
                                break

                    elif whitePieces[i].name == 'White Queen':
                        for j in range(len(whiteQueens)):
                            if app.piece.hitsShape(whiteQueens[j]):
                                whiteQueens.pop(j)
                                break
                   
                    delPiece = whitePieces.pop(i)
                    delPiece.visible = False
        newTurn()

def getLastMove(piece, oldX, oldY, newX, newY):
    lastMove = [piece.name]
    dy = newY - oldY
    dx = newX - oldX
    if app.playerMove == 'white':
        if piece.name == 'White Pawn':
            if dy == -80:
                moveType = 'TwoFront'
            elif dx == 40:
                moveType = 'FrontRight'
            elif dx == -40:
                moveType = 'FrontLeft'
            else:
                moveType = 'Front'

        elif piece.name == 'White Knight':
            moveType = 'KnightMove'

        elif piece.name == 'White Rook':
            moveType = 'RookMove'

        elif piece.name == 'White Bishop':
            moveType = 'BishopMove'

        elif piece.name == 'White Queen':
            moveType = 'QueenMove'

        elif piece.name == 'White King':
            if dx == -80:
                moveType = 'LeftRocked'
            elif dx == 80:
                moveType = 'RightRocked'
            else:
                moveType = 'KingMove'

    elif app.playerMove == 'black':
        if piece.name == 'Black Pawn':
            if dy == 80:
                moveType = 'TwoFront'
            elif dx == 40:
                moveType = 'FrontRight'
            elif dx == -40:
                moveType = 'FrontLeft'
            else:
                moveType = 'Front'

        elif piece.name == 'Black Knight':
            moveType = 'KnightMove'

        elif piece.name == 'Black Rook':
            moveType = 'RookMove'

        elif piece.name == 'Black Bishop':
            moveType = 'BishopMove'

        elif piece.name == 'Black Queen':
            moveType = 'QueenMove'

        elif piece.name == 'Black King':
            if dx == -80:
                moveType = 'LeftRocked'
            elif dx == 80:
                moveType = 'RightRocked'
            else:
                moveType = 'KingMove'

    lastMove.append(moveType)
    lastMove.append(newX)
    lastMove.append(newY)
    
    return lastMove

### Functions for checking if a move puts, or leaves, the player's king in danger

def checkKingThreat(playerMove, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True

    lastMoveIsKing = False

    if playerMove == 'white':
        if app.whiteLastMove[0] == 'White King':
            lastMoveIsKing = True
        
    elif playerMove == 'black':
        if app.blackLastMove[0] == 'Black King':
            lastMoveIsKing = True

    if lastMoveIsKing == False:
        angle = angleTo(oldPieceX, oldPieceY, kingX, kingY)
        
        ### Check angles related to bishops and queens
        if isSafe == True and (angle == 45 or angle == 135 or angle == 225 or angle == 315):
            isSafe = threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
        
        if isSafe == True and (angle == 0 or angle == 90 or angle == 180 or angle == 270):
            isSafe = threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)

        if isSafe == True:
            for i in range(4):
                tempAngle = 45 + 90 * i
                isSafe = threatCheckDiagonal(playerMove, tempAngle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            for i in range(4):
                tempAngle = 90 * i
                isSafe = threatCheckVertHoriz(playerMove, tempAngle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            isSafe = threatCheckKnights(playerMove, kingX, kingY, newPieceX, newPieceY)

        if isSafe == True:
            isSafe = threatCheckPawns(playerMove, kingX, kingY, newPieceX, newPieceY)

    elif lastMoveIsKing == True:
        if isSafe == True:
            for i in range(4):
                angle = 90 * i
                
                isSafe = threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            for i in range(4):
                angle = 45 + 90 * i
                
                isSafe = threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            isSafe = threatCheckKnights(playerMove, newPieceX, newPieceY, newPieceX, newPieceY)

        if isSafe == True:
            isSafe = threatCheckPawns(playerMove, newPieceX, newPieceY, newPieceX, newPieceY)

        if isSafe == True:
            isSafe = threatCheckByKing(playerMove, newPieceX, newPieceY)

    return isSafe

def threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True
    whitePos = [None, None]
    blackPos = [None, None]
    hitWhite = False
    hitBlack = False

    if oldPieceX == kingX and oldPieceY == kingY:
        kingX = newPieceX
        kingY = newPieceY
        
    for i in range(7):
        x = threatGetX(kingX, i, angle)
        y = threatGetY(kingY, i, angle)
        if x > 60 and y > 60 and x < 340 and y < 340:
            if playerMove == 'white':
                for j in range(len(whitePieces)):
                    if hitWhite == False:
                        if oldPieceX == x and oldPieceY == y:
                            hitOldPos = True
                        else:
                            hitOldPos = False
                        if whitePieces[j].hits(x, y) and whitePieces[j].name != 'White King' and hitOldPos == False:
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                if newPieceX == x and newPieceY == y:
                    
                    hitWhite = True
                    whitePos[0] = x
                    whitePos[1] = y

                for j in range(len(blackPieces)):
                    if hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

            elif playerMove == 'black':
                for j in range(len(blackPieces)):
                    if hitBlack == False:
                        if oldPieceX == x and oldPieceY == y:
                            hitOldPos = True

                        else:
                            hitOldPos = False

                        if blackPieces[j].hits(x, y) and blackPieces[j].name != 'Black King' and hitOldPos == False:
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

                if newPieceX == x and newPieceY == y:

                    hitBlack = True
                    blackPos[0] = x
                    blackPos[1] = y

                for j in range(len(whitePieces)):
                    if hitWhite == False:
                        if whitePieces[j].hits(x, y):
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                

        if x <= 60 or y <= 60 or x >= 340 or y >= 340:
            break

    if whitePos[0] != None and blackPos[0] != None:
        if playerMove == 'white':
            if angle == 135 or angle == 45:
                if whitePos[0] > blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        
            elif angle == 225 or angle == 315:
                if whitePos[0] < blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                    
        elif playerMove == 'black':
            if angle == 135 or angle == 45:
                if blackPos[0] > whitePos[0]:
                    if isSafe == False:
                        isSafe = True

            elif angle == 225 or angle == 315:
                if blackPos[0] < whitePos[0]:
                    if isSafe == False:
                        isSafe = True

    if playerMove == 'white':
        if blackPos[0] == None:
            isSafe = True

        elif whitePos[0] == None:
            isSafe = False

        if isSafe == False:
            if blackPos[0] != None:
                isSafe = True
                
                for i in range(len(blackBishops)):
                    if blackBishops[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False
                
                for i in range(len(blackQueens)):
                    if blackQueens[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False

    elif playerMove == 'black':
        if whitePos[0] == None:
            isSafe = True
        
        elif blackPos[0] == None:
            isSafe = False

        if isSafe == False:
            if whitePos[0] != None:
                isSafe = True
                
                for i in range(len(whiteBishops)):
                    if whiteBishops[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        
                for i in range(len(whiteQueens)):
                    if whiteQueens[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        
    return isSafe

def threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True
    whitePos = [None, None]
    blackPos = [None, None]
    hitWhite = False
    hitBlack = False

    ### Do smth to check x when king is moved

    if oldPieceX == kingX and oldPieceY == kingY:
        kingX = newPieceX
        kingY = newPieceY

    for i in range(7):
        x = threatGetX(kingX, i, angle)
        y = threatGetY(kingY, i, angle)
        
        if x >= 60 and y >= 60 and x <= 340 and y <= 340:
            if playerMove == 'white':
                for j in range(len(whitePieces)):
                    if hitWhite == False:
                        if oldPieceX == x and oldPieceY == y:
                            hitOldPos = True

                        else:
                            hitOldPos = False

                        if whitePieces[j].hits(x, y) and hitOldPos == False:
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                if newPieceX == x and newPieceY == y and hitWhite == False:
                    
                    hitWhite = True
                    whitePos[0] = x
                    whitePos[1] = y

                for j in range(len(blackPieces)):
                    if hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

            elif playerMove == 'black':
                for j in range(len(blackPieces)):
                    if hitBlack == False:
                        if x == oldPieceX and y == oldPieceY:
                            hitOldPos = True

                        else:
                            hitOldPos = False
                            
                        if blackPieces[j].hits(x, y) and hitOldPos == False:
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

                if newPieceX == x and newPieceY == y and hitBlack == False:

                    hitBlack = True
                    blackPos[0] = x
                    blackPos[1] = y

                for j in range(len(whitePieces)):
                    if hitWhite == False:
                        if whitePieces[j].hits(x, y):
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

        if angle == 90 or angle == 270:
            if x <= 60 or x >= 340:
                break

        elif angle == 0 or angle == 180:
            if y <= 60 or y >= 340:
                break

    if whitePos[0] != None and blackPos[0] != None:
        isSafe = False
        
        if angle == 270:
            if playerMove == 'white':
                if whitePos[0] < blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        
            elif playerMove == 'black':
                if blackPos[0] < whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        

        elif angle == 90:
            if playerMove == 'white':
                if whitePos[0] > blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                
            elif playerMove == 'black':
                if blackPos[0] > whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        
        elif angle == 180:
            if playerMove == 'white':
                if whitePos[1] > blackPos[1]:
                    if isSafe == False:
                        isSafe = True
                        
            elif playerMove == 'black':
                if blackPos[1] > whitePos[1]:
                    if isSafe == False:
                        isSafe = True
                    
        elif angle == 0:
            if playerMove == 'white':
                if whitePos[1] < blackPos[1]:
                    if isSafe == False:
                        isSafe = True

            elif playerMove == 'black':
                if blackPos[1] < whitePos[1]:
                    if isSafe == False:
                        isSafe = True
                        
        if playerMove == 'white':
            if whitePos == blackPos:
                isSafe = True
        
        elif playerMove == 'black':
            if whitePos == blackPos:
                isSafe = True

    if playerMove == 'white':
        if blackPos[0] == None:
            isSafe = True

        elif whitePos[0] == None:
            isSafe = False

        if isSafe == False:
            if blackPos[0] != None:
                isSafe = True
                
                for i in range(len(blackRooks)):
                    if blackRooks[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False

                for i in range(len(blackQueens)):
                    if blackQueens[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False
                        
    elif playerMove == 'black':
        if whitePos[0] == None:
            isSafe = True
            
        elif blackPos[0] == None:
            isSafe = False
            
        if isSafe == False:
            if whitePos[0] != None:
                isSafe = True
                
                for i in range(len(whiteRooks)):
                    if whiteRooks[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        
                for i in range(len(whiteQueens)):
                    if whiteQueens[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        
    return isSafe

def threatCheckKnights(playerMove, kingX, kingY, newPieceX, newPieceY):
    
    isSafe = True

    checkUL = True
    checkUR = True
    checkRU = True
    checkRD = True
    checkDR = True
    checkDL = True
    checkLD = True
    checkLU = True
    
    x1R = kingX + 40
    x2R = kingX + 80
    x1L = kingX - 40
    x2L = kingX - 80

    y1D = kingY + 40
    y2D = kingY + 80
    y1U = kingY - 40
    y2U = kingY - 80

    enemyPos = [None, None]

    if kingX <= 100:
        checkLD = False
        checkLU = False
        if kingX == 60:
            checkUL = False
            checkDL = False
    elif kingX >= 300:
        checkRU = False
        checkRD = False
        if kingX == 340:
            checkUR = False
            checkDR = False

    if kingY <= 100:
        checkUL = False
        checkUR = False
        if kingY == 60:
            checkRU = False
            checkLU = False
    elif kingY >= 300:
        checkDR = False
        checkDL = False
        if kingY == 340:
            checkRD = False
            checkLD = False

    if playerMove == 'white':
        if len(blackKnights) != 0:

            if checkUL == True and isSafe == True:
                x = x1L
                y = y2U
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkUR == True and isSafe == True:
                x = x1R
                y = y2U
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y     

            if checkRU == True and isSafe == True:
                x = x2R
                y = y1U
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkRD == True and isSafe == True:
                x = x2R
                y = y1D
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y

            if checkDL == True and isSafe == True:
                x = x1L
                y = y2D
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkDR == True and isSafe == True:
                x = x1R
                y = y2D
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkLU == True and isSafe == True:
                x = x2L
                y = y1U
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkLD == True and isSafe == True:
                x = x2L
                y = y1D
                for i in range(len(blackKnights)):
                    if blackKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
   
    elif playerMove == 'black':
        if len(whiteKnights) != 0:

            if checkUL == True and isSafe == True:
                x = x1L
                y = y2U
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkUR == True and isSafe == True:
                x = x1R
                y = y2U
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkRU == True and isSafe == True:
                x = x2R
                y = y1U
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkRD == True and isSafe == True:
                x = x2R
                y = y1D
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkDL == True and isSafe == True:
                x = x1L
                y = y2D
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkDR == True and isSafe == True:
                x = x1R
                y = y2D
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkLU == True and isSafe == True:
                x = x2L
                y = y1U
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
            if checkLD == True and isSafe == True:
                x = x2L
                y = y1D
                for i in range(len(whiteKnights)):
                    if whiteKnights[i].hits(x, y) and isSafe == True:
                        isSafe = False
                        enemyPos[0] = x
                        enemyPos[1] = y
                        
    if enemyPos[0] == None:
        isSafe = True
    
    if newPieceX == enemyPos[0] and newPieceY == enemyPos[1]:
        isSafe = True

    return isSafe

def threatCheckPawns(playerMove, kingX, kingY, newPieceX, newPieceY):
    isSafe = True

    enemyPos = [None, None]

    if playerMove == 'white':
        y = kingY - 40
        xL = kingX - 40
        xR = kingX + 40
        if len(blackPawns) != 0:
            if kingY != 60:
                if kingX != 60:
                    for i in range(len(blackPawns)):
                        if blackPawns[i].hits(xL, y) and isSafe == True:
                            isSafe = False
                            enemyPos = [xL, y]
                            
                            break
                if kingX != 340:
                    for i in range(len(blackPawns)):
                        if blackPawns[i].hits(xR, y) and isSafe == True:
                            isSafe = False
                            enemyPos = [xR, y]
                            
                            break
    elif playerMove == 'black':
        y = kingY + 40
        xL = kingX - 40
        xR = kingX + 40
        if len(whitePawns) != 0:
            if kingY != 60:
                if kingX != 60:
                    for i in range(len(whitePawns)):
                        if whitePawns[i].hits(xL, y) and isSafe == True:
                            isSafe = False
                            enemyPos = [xL, y]
                            
                            break
                if kingX != 340:
                    for i in range(len(whitePawns)):
                        if whitePawns[i].hits(xR, y) and isSafe == True:
                            isSafe = False
                            enemyPos = [xR, y]
                            
                            break
    if enemyPos[0] == None:
        isSafe = True
        
    if enemyPos[0] == newPieceX and enemyPos[1] == newPieceY:
        isSafe = True

    return isSafe

def threatCheckByKing(playerMove, kingX, kingY):
    isSafe = True
    positions = makeList(2, 8)

    positions[0] = [kingX - 40, kingX, kingX + 40, kingX + 40, kingX + 40, kingX, kingX - 40, kingX - 40]
    positions[1] = [kingY - 40, kingY - 40, kingY - 40, kingY, kingY + 40, kingY + 40, kingY + 40, kingY]
    for i in range(8):
        if playerMove == 'white':
            if blackKing.hits(positions[0][i], positions[1][i]):
                isSafe = False
                
                break
        elif playerMove == 'black':
            if whiteKing.hits(positions[0][i], positions[1][i]):
                isSafe = False
                
                break
            
    return isSafe

def threatGetX(kingX, i, angle):
    if angle == 180 or angle == 0:
        x = kingX
    elif angle < 180:
        x = kingX - 40 * (i + 1)
    elif angle > 180:
        x = kingX + 40 * (i + 1)

    
    return x

def threatGetY(kingY, i, angle):
    if angle == 90 or angle == 270:
        y = kingY
    elif angle > 90 and angle < 270:
        y = kingY - 40 * (i + 1)

    elif angle < 90 or angle > 270:
        y = kingY + 40 * (i + 1)
    return y

### Function to switch a pawn for another piece when reaching the end of the board

def switchPawn(playerMove, x, y):
    proceed = False
    piece = None

    if playerMove == 'white' and y == 60:
        proceed = True
        fill = 'navajoWhite'

    elif playerMove == 'black' and y == 340:
        proceed = True
        fill = 'maroon'

    if proceed == True:

        if playerMove == 'white':
            for i in range(len(whitePawns)):
                
                if whitePawns[i].hits(x, y):
                    whitePawns.pop(i)
                    
                    break
            
            for i in range(len(whitePieces)):
                
                if whitePieces[i].hits(x, y) and whitePieces[i].name == 'White Pawn':
                    delPiece = whitePieces.pop(i)
                    
                    delPiece.visible = False
                    
                    break
        
        elif playerMove == 'black':
            for i in range(len(blackPawns)):
                if blackPawns[i].hits(x, y):
                    blackPawns.pop(i)
                    break
            
            for i in range(len(blackPieces)):
                if blackPieces[i].hits(x, y) and blackPieces[i].name == 'Black Pawn':
                    delPiece = blackPieces.pop(i)
                    delPiece.visible = False
                    break
        while piece == None:
            piece = app.getTextInput('What do you want to replace your pawn with? Queen (Q), Bishop (B), Knight (K), Rook (R)')

            if piece.islower() == True:
                piece = piece.upper()

            if piece != 'Q' and piece != 'B' and piece != 'K' and piece != 'R':
                piece = None

        if piece == 'Q':
            drawQueen(fill, x, y)

            if playerMove == 'white':
                whitePieces.append(whiteQueens[len(whiteQueens)-1])

            elif playerMove == 'black':
                blackPieces.append(blackQueens[len(blackQueens)-1])
            
        elif piece == 'B':
            drawBishop(fill, x, y)

            if playerMove == 'white':
                whitePieces.append(whiteBishops[len(whiteBishops)-1])

            elif playerMove == 'black':
                blackPieces.append(blackBishops[len(blackBishops)-1])

        elif piece == 'K':
            drawKnight(fill, x, y)

            if playerMove == 'white':
                whitePieces.append(whiteKnights[len(whiteKnights)-1])

            elif playerMove == 'black':
                blackPieces.append(blackKnights[len(blackKnights)-1])

        elif piece == 'R':
            drawRook(fill, x, y)

            if playerMove == 'white':
                whitePieces.append(whiteRooks[len(whiteRooks)-1])

            elif playerMove == 'black':
                blackPieces.append(blackRooks[len(blackRooks)-1])

app.phase = 1
app.piece = None
app.playerMove = 'white'
app.whiteLastMove = [None, None, None, None]
app.blackLastMove = [None, None, None, None]

app.whiteKingStart = True
app.blackKingStart = True

app.whiteRookLStart = True
app.whiteRookRStart = True

app.blackRookLStart = True
app.blackRookRStart = True

app.legalMove = False

def onMousePress(mouseX, mouseY):
  
    ### Selects piece
    if app.phase == 1:
        print('---------------------------------')
        piece = selectPiece(app.playerMove, mouseX, mouseY)
        ### Checks what moves are available
        if piece != None:
            if piece.name == 'White Pawn' or piece.name == 'Black Pawn':
                checkPawnMoves(app.playerMove, piece.centerX, piece.centerY)
                app.piece = piece
                app.phase = 2
            elif piece.name == 'White Knight' or piece.name == 'Black Knight':
                checkKnightMoves(app.playerMove, piece.centerX, piece.centerY)
                app.piece = piece
                app.phase = 2
            elif piece.name == 'White Rook' or piece.name == 'Black Rook':
                checkRookMoves(app.playerMove, piece.centerX, piece.centerY)
                app.piece = piece
                app.phase = 2
            elif piece.name == 'White Bishop' or piece.name == 'Black Bishop':
                checkBishopMoves(app.playerMove, piece.centerX, piece.centerY)
                app.piece = piece
                app.phase = 2
            elif piece.name == 'White Queen' or piece.name == 'Black Queen':
                checkRookMoves(app.playerMove, piece.centerX, piece.centerY)
                checkBishopMoves(app.playerMove, piece.centerX, piece.centerY)
                app.piece = piece
                app.phase = 2
            elif piece.name == 'White King' or piece.name == 'Black King':
                checkKingMoves(app.playerMove, piece.centerX, piece.centerY)
                if app.playerMove == 'white' and app.whiteKingStart:
                    checkWhiteRocked()
                elif app.playerMove == 'black' and app.blackKingStart:
                    checkBlackRocked()
                app.piece = piece
                app.phase = 2

    elif app.phase == 2:
        if moveMarkers != None:
            oldPos = [app.piece.centerX, app.piece.centerY]
            pos = movePiece(mouseX, mouseY)
            if pos != None:
                if app.playerMove == 'white':

                    app.whiteLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
                    app.legalMove = checkKingThreat(app.playerMove, oldPos[0], oldPos[1], pos[0], pos[1], whitePieces[0].centerX, whitePieces[0].centerY)

                elif app.playerMove == 'black':

                    app.blackLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
                    app.legalMove = checkKingThreat(app.playerMove, oldPos[0], oldPos[1], pos[0], pos[1], blackPieces[0].centerX, blackPieces[0].centerY)

                
                if app.legalMove == True:
                    posPiece(pos, oldPos)

                    if app.legalMove == True:
                        wipePiece()
                print('legalMove is', app.legalMove)
                

        selectedMarkers.clear()
        moveMarkers.clear()

        app.phase = 1

def makeMove(move):
    a1 = move[0]
    a2 = move[3]

    x1 = 20
    x2 = 20
    y1 = 20
    y2 = 20

    if a1.islower() == True:
        a1 = a1.upper()

    if a2.islower() == True:
        a2 = a2.upper()
    move = a1+move[1]+move[2]+a2+move[4]

    for i in range(len(boardHorizPos)):
        if move[0] == boardHorizPos[i]:
            x1 = 60 + i * 40
        if move[3] == boardHorizPos[i]:
            x2 = 60 + i * 40
    
    for i in range(len(boardVertPos)):
        if move[1] == boardVertPos[i]:
            y1 = 60 + i * 40
        if move[4] == boardVertPos[i]:
            y2 = 60 + i * 40

    onMousePress(x1, y1)
    onMousePress(x2, y2)

    print(move)

def testingPawnSwitching():
    makeMove('h2-h4')

    makeMove('A7-a5')

    makeMove('h4-H5')

    makeMove('a5-a4')

    makeMove('h5-h6')

    makeMove('a4-a3')

    makeMove('h6-g7')

    makeMove('a3-b2')

def testingKingThreat(piece):
    makeMove('e2-e4')
    makeMove('e7-e5')

    makeMove('d1-g4')
    makeMove('d8-g5')

    makeMove('f1-c4')
    makeMove('f8-c5')

    makeMove('d2-d4')
    makeMove('d7-d5')

    makeMove('f2-f4')
    makeMove('f7-f5')

    makeMove('c1-e3')
    makeMove('c8-e6')

    makeMove('b1-a3')
    makeMove('b8-a6')

    makeMove('g1-h3')
    makeMove('g8-h6')

    makeMove('e4-d5')
    makeMove('e5-d4')

    makeMove('e3-d4')
    makeMove('g5-f4')

    makeMove('g4-f5')
    makeMove('e6-d5')

    if piece == 'vertqueen':
        makeMove('f5-e5')

    elif piece == 'diagqueen':
        makeMove('f5-g6')

    elif piece == 'bishop':
        makeMove('c4-b5')

    elif piece == 'rook':
        makeMove('e1-g1')
        makeMove('f4-g3')

        makeMove('f1-e1')

def testingCastle(threaten):
    makeMove('b1-a3')
    makeMove('b8-a6')

    makeMove('e2-e3')
    makeMove('e7-e6')

    makeMove('a3-b5')
    makeMove('a6-b4')

    makeMove('f2-f4')
    makeMove('f7-f5')

    makeMove('g1-f3')
    makeMove('g8-f6')

    makeMove('g2-g4')
    makeMove('g7-g5')

    makeMove('f1-h3')
    makeMove('f8-h6')

    makeMove('b5-c3')
    makeMove('b4-c6')

    makeMove('d2-d3')
    makeMove('d7-d6')

    makeMove('d1-e2')
    makeMove('d8-e7')

    makeMove('c1-d2')
    makeMove('c8-d7')

    if threaten == 'king':
        makeMove('f3-g5')
        makeMove('f6-g4')

        makeMove('g5-e6')
        makeMove('g4-e3')

        makeMove('e6-g7')

    elif threaten == 'lrook':
        makeMove('f3-e5')
        makeMove('f6-e4')

        makeMove('e5-c4')
        makeMove('e4-c5')

        makeMove('c4-b6')

    elif threaten == 'rrook':
        makeMove('f3-g5')
        makeMove('f6-g4')

        makeMove('g5-f7')

# testingCastle('king')
# testingCastle('lrook')
# testingCastle('rrook')
# testingCastle(None)

# testingKingThreat('vertqueen')
# testingKingThreat('diagqueen')
# testingKingThreat('bishop')
# testingKingThreat('rook')
# testingKingThreat(None)

# testingPawnSwitching()

cmu_graphics.run()