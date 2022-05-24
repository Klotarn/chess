from calendar import TUESDAY
from http.client import UNPROCESSABLE_ENTITY
from pickle import FALSE
from types import TracebackType
from urllib.parse import non_hierarchical
from cmu_graphics import *

app.rows = 8
app.cols = 8
board = makeList(app.rows, app.cols)

boardHorizPos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
boardVertPos = ['8', '7', '6', '5', '4', '3', '2', '1']

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

whiteQueen = Group()
whiteQueen.name = 'White Queen'

blackQueen = Group()
blackQueen.name = 'Black Queen'

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

def drawQueen(fill, x, y):
    spikeX = x
    spikeX -= 30
    spikeRotateAngle = -45
    for i in range(5):
    #     # x = x-20 + 10 * i
        
        spikeX += 10
        spikeRotateAngle += 15
        if fill == 'navajoWhite':
            whiteQueen.add(Polygon(spikeX, y-2, spikeX+5, y+50-2, spikeX-5, y+50-2, fill = fill, rotateAngle = spikeRotateAngle, border = 'black', borderWidth = 1))
        else:
            blackQueen.add(Polygon(spikeX, y-2, spikeX+5, y+50-2, spikeX-5, y+50-2, fill = fill, rotateAngle = spikeRotateAngle, border = 'black', borderWidth = 1))
        
    for i in range(3):
        if fill == 'navajoWhite':
            whiteQueen.add(Oval(x, y+50 + 5 * i, 35, 20, fill = fill, border = 'black', borderWidth = 1))
            
        else:
            blackQueen.add(Oval(x, y+50 + 5 * i, 35, 20, fill = fill, border = 'black', borderWidth = 1))
    
    if fill == 'navajoWhite':
        whiteQueen.height = 35
        whiteQueen.width = 35
        whiteQueen.centerX = x
        whiteQueen.centerY = y
    
    else:
        blackQueen.height = 35
        blackQueen.width = 35
        blackQueen.centerX = x
        blackQueen.centerY = y
    
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
    # print(rook.width, rook.height)
    rook.width = 29
    rook.height = 35
    rook.centerX = x
    rook.centerY = y

    
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
    
    # print(knight.width, knight.height)
    
    knight.width = 21
    knight.height = 35
    knight.centerX = x
    knight.centerY = y
    
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
    
    # print(bishop.width, bishop.height)
    
    bishop.width = 20
    bishop.height = 35
    
    bishop.centerX = x
    bishop.centerY = y
    
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
    
    # print(pawn, pawn.width, pawn.height)
    pawn.width = 18.3
    pawn.height = 25
    pawn.centerX = x
    pawn.centerY = y
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

for row in range(len(board)):
    for col in range(len(board[row])):
        print(board[row][col].vert, board[row][col].horiz)

whitePieces = []
blackPieces = []

whitePieces.append(whiteKing)
whitePieces.append(whiteQueen)

blackPieces.append(blackKing)
blackPieces.append(blackQueen)

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
                # print(whitePieces[i].name, i)
                if whitePieces[i].hits(mouseX, mouseY):
                    # print(whitePieces[i].name)
                    x = whitePieces[i].centerX
                    y = whitePieces[i].centerY
                    pieceSelected = True
                    selectedMarkers.add(Circle(x, y, 15, fill = 'lime', opacity = 50))
                    piece = whitePieces[i]
    elif playerMove == 'black':
        for i in range(len(blackPieces)):
            if pieceSelected == False:
                # print(blackPieces[i].name, i)
                if blackPieces[i].hits(mouseX, mouseY):
                    # print(blackPieces[i].name)
                    x = blackPieces[i].centerX
                    y = blackPieces[i].centerY
                    pieceSelected = True
                    selectedMarkers.add(Circle(x, y, 15, fill = 'lime', opacity = 50))
                    piece = blackPieces[i]
    return piece

def checkPawnMoves(playerMove, x, y):
    print(playerMove)
    if playerMove == 'white':

        for row in range(app.rows):

            for col in range(app.cols):

                if board[row][col].hits(x, y):
                    print(board[row][col].vert, board[row][col].horiz)
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
                                # print('blockFront is true')
                                # print('hit black piece')

                            if board[row-2][col].hits(targetX, targetY):
                                moveTwoFront = False
                                # print('move 2 front disable 1')
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
                                # blockFront = True
                                # print('blockFront is true')
                                # print('hit white piece')
                            if board[row-2][col].hits(targetX, targetY):
                                moveTwoFront = False
                                # print('move 2 front disabel 2')
                    if board[row][col].vert != '2':
                        moveTwoFront = False
                        # print('move 2 front disable 3')

                    if moveFront == True:
                        # moveMarkers.add(Circle(board[row-1][col].centerX, board[row-1][col].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row-1, col)

                    if moveTwoFront == True:
                        # moveMarkers.add(Circle(board[row-2][col].centerX, board[row-2][col].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row-2, col)
                        # print('moveTwoFront is true')

                    if moveFrontLeft == True:
                        # moveMarkers.add(Circle(board[row-1][col-1].centerX, board[row-1][col-1].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row-1, col-1)
                    if moveFrontRight == True:

                        # moveMarkers.add(Circle(board[row-1][col+1].centerX, board[row-1][col+1].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row-1, col+1)

    elif playerMove == 'black':
        for row in range(app.rows):
            for col in range(app.cols):
                if board[row][col].hits(x, y):
                    print(board[row][col].vert, board[row][col].horiz)
                    ### check move in front
                    moveFront = True
                    # blockFront = False
                    moveFrontLeft = False
                    moveFrontRight = False
                    moveTwoFront = True
                    for i in range(len(whitePieces)):
                        targetX = whitePieces[i].centerX
                        targetY = whitePieces[i].centerY
                        if moveFront == True:
                            if board[row+1][col].hits(targetX, targetY):
                                moveFront = False
                                # blockFront = True
                                # print('blockFront is true')
                                # print('hit black piece')
                            if board[row+2][col].hits(targetX, targetY):
                                moveTwoFront = False
                                # print('move 2 front disable 1')
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
                                # blockFront = True
                                # print('blockFront is true')
                                # print('hit white piece')
                            if board[row+2][col].hits(targetX, targetY):
                                moveTwoFront = False
                                # print('move 2 front disabel 2')
                    if board[row][col].vert != '7':
                        moveTwoFront = False
                        # print('move 2 front disable 3')

                    if moveFront == True:
                        # moveMarkers.add(Circle(board[row+1][col].centerX, board[row+1][col].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row+1, col)

                    if moveTwoFront == True:
                        # moveMarkers.add(Circle(board[row+2][col].centerX, board[row+2][col].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row+2, col)
                        # print('moveTwoFront is true')
                    if moveFrontLeft == True:
                        # moveMarkers.add(Circle(board[row+1][col-1].centerX, board[row+1][col-1].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row+1, col-1)
                    if moveFrontRight == True:
                        # moveMarkers.add(Circle(board[row+1][col+1].centerX, board[row+1][col+1].centerY, 15, fill='red', opacity = 50))
                        addMoveMarker(row+1, col+1)

def checkKnightMoves(playerMove, x, y):
    print(playerMove)
    # if playerMove == 'white':

    for row in range(app.rows):

        for col in range(app.cols):

            if board[row][col].hits(x, y):

                print(board[row][col].vert, board[row][col].horiz)

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

                print(vert, horiz)

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
                    # print('move r disabled cuz col')

                # if playerMove == 'white':
                countUp = 1
                while moveUp == True:
                # for j in range(8):
                    # print('row and count', row, countUp)
                    # print('dif', row-countUp)
                    if row-countUp == -1:
                        moveUp = False
                        # print('move up disabled because of board boundaries')
                    
                    if moveUp == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp, 'black check')

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    nextUp = True
                                    # print('move up disabled because of hit black Piece')
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp, 'white check')

                                if board[row-countUp][col].hits(targetX, targetY):
                                    moveUp = False
                                    nextUp = True
                                    # print('move up disabled because of hit black Piece')
                                    print(whitePieces[i].name)

                    if moveUp == True:
                        addMoveMarker(row-countUp, col)
                        # print('added marker at', row-countUp, col)
                        # if moveUp == False:
                        #     break
                        # print('added upmove marker at', board[row-countUp][col].vert, board[row-countUp][col].horiz)
                    if nextUp == True:
                        addMoveMarker(row-countUp, col)
                        # print('added marker on black piece')
                    countUp += 1

                countDown = 1
                while moveDown == True:
                    print(row, countDown)

                    # if row+countDown < 8:
                    # if board[row+countDown][col].centerY > 340:
                    #     moveDown = False
                    if row+countDown == 8:
                        moveDown = False

                    if moveDown == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move down is', moveDown)

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown, 'black check')

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                    nextDown = True
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown)

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move down is', moveDown, 'white check')

                                if board[row+countDown][col].hits(targetX, targetY):
                                    moveDown = False
                                    nextDown = True
                                    print(whitePieces[i].name)
                
                    if moveDown == True:
                        addMoveMarker(row+countDown, col)
                        # print('added downmove marker on', board[row+countDown][col].vert, board[row+countDown][col].horiz)
                    
                    if nextDown == True:
                        addMoveMarker(row+countDown, col)
                        # print('added downmove marker on', board[row+countDown][col].vert, board[row+countDown][col].horiz)
                    countDown += 1
                # for x in range

                countR = 1
                while moveR == True:
                    if col+countR == 8:
                        moveR = False
                        # print('disable move r cuz col + count')

                    if moveR == True:
                        if playerMove == 'white':
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move down is', moveDown)

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown, 'black check')

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    nextR = True
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown)

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move down is', moveDown, 'white check')

                                if board[row][col+countR].hits(targetX, targetY):
                                    moveR = False
                                    nextR = True
                                    print(whitePieces[i].name)
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

                                # print('move down is', moveDown)

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown, 'black check')

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                    nextL = True
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move down is', moveDown)

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                
                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move down is', moveDown, 'white check')

                                if board[row][col-countL].hits(targetX, targetY):
                                    moveL = False
                                    nextL = True
                                    print(whitePieces[i].name)
                    if moveL == True:
                        addMoveMarker(row, col-countL)
                    if nextL == True:
                        addMoveMarker(row, col-countL)
                    countL += 1
                    
def checkBishopMoves(playerMove, x, y):
    print('checking bishop moves')
    for row in range(app.rows):
        for col in range(app.cols):
            if board[row][col].hits(x, y):
                vert = board[row][col].vert
                horiz = board[row][col].horiz

                print('position:', vert, horiz)

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

                                # print('move up is', moveUp)

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp, 'black check')

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    nextUpL = True
                                    # print('move up disabled because of hit black Piece')
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp, 'white check')

                                if board[row-countUpL][col-countUpL].hits(targetX, targetY):
                                    moveUpL = False
                                    nextUpL = True
                                    # print('move up disabled because of hit black Piece')
                                    print(whitePieces[i].name)
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

                                # print('move up is', moveUp)

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp, 'black check')

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    nextUpR = True
                                    # print('move up disabled because of hit black Piece')
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp, 'white check')

                                if board[row-countUpR][col+countUpR].hits(targetX, targetY):
                                    moveUpR = False
                                    nextUpR = True
                                    # print('move up disabled because of hit black Piece')
                                    print(whitePieces[i].name)
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

                                # print('move up is', moveUp)

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp, 'black check')

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    nextDownL = True
                                    # print('move up disabled because of hit black Piece')
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp, 'white check')

                                if board[row+countDownL][col-countDownL].hits(targetX, targetY):
                                    moveDownL = False
                                    nextDownL = True
                                    # print('move up disabled because of hit black Piece')
                                    print(whitePieces[i].name)
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

                                # print('move up is', moveUp)

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp, 'black check')

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    nextDownR = True
                                    # print('move up disabled because of hit black Piece')
                                    print(blackPieces[i].name)

                        elif playerMove == 'black':
                            for i in range(len(blackPieces)):
                                targetX = blackPieces[i].centerX
                                targetY = blackPieces[i].centerY

                                # print('move up is', moveUp)

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    # print('move up disabled because of hit white piece')

                            for i in range(len(whitePieces)):
                                targetX = whitePieces[i].centerX
                                targetY = whitePieces[i].centerY

                                # print('move up is', moveUp, 'white check')

                                if board[row+countDownR][col+countDownR].hits(targetX, targetY):
                                    moveDownR = False
                                    nextDownR = True
                                    # print('move up disabled because of hit black Piece')
                                    print(whitePieces[i].name)
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
                print('position:', vert, horiz)

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

def movePiece(targetX, targetY):

    pos = None

    for marker in moveMarkers.children:

        if pos == None:

            if marker.hits(targetX, targetY):

                pos = [marker.centerX, marker.centerY]

    return pos

def newTurn():
    if app.playerMove == 'white':
        print('app.playerMove was white')
        app.playerMove = 'black'
    elif app.playerMove == 'black':
        print('app.playerMove was black')
        app.playerMove = 'white'           
    print('newTurn was called and next player is', app.playerMove)         

def posPiece(pos, oldPos):
    app.piece.centerX = pos[0]
    app.piece.centerY = pos[1]
    
    dx = pos[0]-oldPos[0]
    dy = pos[1]-oldPos[1]

    print(dx, dy)

    if app.playerMove == 'white':
        if app.whiteLastMove[0] == 'White Pawn' and (app.whiteLastMove[1] == 'FrontLeft' or app.whiteLastMove[1] == 'FrontRight'):
            passantWipe()
        elif app.whiteLastMove[0] == 'White Rook':
            if oldPos[0] == 60:
                app.whiteRookLStart = False
            elif oldPos[0] == 340:
                app.whiteRookRStart = False
        elif app.whiteLastMove[0] == 'White King':
            app.whiteKingStart = False
            if dx == 80:
                posRocked('right', app.playerMove)
            elif dx == -80:
                posRocked('left', app.playerMove)

    elif app.playerMove == 'black':
        if app.blackLastMove[0] == 'Black Pawn' and (app.blackLastMove[1] == 'FrontLeft' or app.blackLastMove[1] == 'FrontRight'):
            passantWipe()
        elif app.blackLastMove[0] == 'Black Rook':
            if oldPos[0] == 60:
                app.blackRookLStart = False
            elif oldPos[0] == 340:
                app.blackRookRStart = False
        elif app.blackLastMove[0] == 'Black King':
            app.blackKingStart = False
            if dx == 80:
                posRocked('right', app.playerMove)
            elif dx == -80:
                posRocked('left', app.playerMove)
            
def passantWipe():
    if app.playerMove == 'white':
        x = app.whiteLastMove[2]
        y = app.whiteLastMove[3] + 40
        listLen = len(blackPieces)
        for i in range(len(blackPieces)):
            # print(i)
            if len(blackPieces) == listLen:
                if blackPieces[i].hits(x, y):
                    print(blackPieces[i].name)
                    delPiece = blackPieces.pop(i)
                    delPiece.visible = False
    elif app.playerMove == 'black':
        x = app.blackLastMove[2]
        y = app.blackLastMove[3] - 40
        listLen = len(whitePieces)
        for i in range(len(whitePieces)):
            # print(i)
            if len(whitePieces) == listLen:
                if whitePieces[i].hits(x, y):
                    print(whitePieces[i].name)
                    delPiece = whitePieces.pop(i)
                    delPiece.visible = False

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
            # print(i)
            if len(blackPieces) == listLen:
                if app.piece.hitsShape(blackPieces[i]):
                    print(blackPieces[i].name)
                    delPiece = blackPieces.pop(i)
                    delPiece.visible = False
        newTurn()

    elif app.playerMove == 'black':
        listLen = len(whitePieces)
        for i in range(len(whitePieces)):
            # print(i)
            if len(whitePieces) == listLen:
                if app.piece.hitsShape(whitePieces[i]):
                    print(whitePieces[i].name)
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
    # print('y diff was', dy)
    # print('last move was', lastMove)
    return lastMove

def checkKingThreat(playerMove, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True
    hitWhite = False
    hitBlack = False
    whitePos = [None, None]
    blackPos = [None, None]

    lastMoveIsKing = False

    if playerMove == 'white':
        if app.whiteLastMove[0] == 'White King':
            lastMoveIsKing = True
        
    elif playerMove == 'black':
        if app.blackLastMove[0] == 'Black King':
            lastMoveIsKing = True

    if lastMoveIsKing == False:
        # print('do stuff')
        angle = angleTo(oldPieceX, oldPieceY, kingX, kingY)
        print(angle)
        ### Check angles related to bishops and queens
        if isSafe == True and (angle == 45 or angle == 135 or angle == 225 or angle == 315):
            isSafe = threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
        
        if isSafe == True and (angle == 0 or angle == 90 or angle == 180 or angle == 270):
            isSafe = threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)

        if isSafe == True:
            print('--------angle didnt match, trying diagonal')
            for i in range(4):
                tempAngle = 45 + 90 * i
                isSafe = threatCheckDiagonal(playerMove, tempAngle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            print('--------angle didnt match, trying vert horiz')
            for i in range(4):
                tempAngle = 90 * i
                isSafe = threatCheckVertHoriz(playerMove, tempAngle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break

    elif lastMoveIsKing == True:
        print('-------- King was moved')
        if isSafe == True:
            print('-------- checking diagonal')
            for i in range(4):
                angle = 90 * i
                print('checking', angle)
                isSafe = threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break
        
        if isSafe == True:
            print('-------- checking vert horiz')
            for i in range(4):
                angle = 45 + 90 * i
                print('checking', angle)
                isSafe = threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY)
                if isSafe == False:
                    break

    return isSafe

def threatCheckDiagonal(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True
    whitePos = [None, None]
    blackPos = [None, None]
    hitWhite = False
    hitBlack = False
    
    # if playerMove == 'white':
        # if angle == 135:
    print('checking up left')
    for i in range(7):
        x = threatGetX(kingX, i, angle)
        y = threatGetY(kingY, i, angle)
        if x > 60 and y > 60 and x < 340 and y < 340:
            if playerMove == 'white':
                for j in range(len(whitePieces)):
                    if x != oldPieceX and hitWhite == False:
                        if whitePieces[j].hits(x, y):
                            print('hit white piece not old x')
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                if x == oldPieceX and y == oldPieceY:
                    print('checked the old pieceX')

                if newPieceX == x and newPieceY == y:
                    print('piece was hit after move')
                    
                    hitWhite = True
                    whitePos[0] = x
                    whitePos[1] = y

                for j in range(len(blackPieces)):
                    if x != oldPieceX and hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

            elif playerMove == 'black':
                for j in range(len(blackPieces)):
                    if x != oldPieceX and hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            print('hit black piece not old x')
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

                if x == oldPieceX and y == oldPieceY:
                    print('checked the old pieceX')
                    # hitBlack = True
                    ### maybe hitblack is true and set black x?
                if newPieceX == x and newPieceY == y:
                    print('piece was hit after move')

                    hitBlack = True
                    blackPos[0] = x
                    blackPos[1] = y

                for j in range(len(whitePieces)):
                    if x != oldPieceX and hitWhite == False:
                        if whitePieces[j].hits(x, y):
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                

        if x <= 60 or y <= 60 or x >= 340 or y >= 340:
            break
    
    print('white x:', whitePos[0])
    print('black x:', blackPos[0])

    if whitePos[0] != None and blackPos[0] != None:
        if playerMove == 'white':
            if angle == 135 or angle == 45:
                if whitePos[0] > blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe is true due to white > black')
            elif angle == 225 or angle == 315:
                if whitePos[0] < blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to white < black')
                    
        elif playerMove == 'black':
            if angle == 135 or angle == 45:
                if blackPos[0] > whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to black > white')

            elif angle == 225 or angle == 315:
                if blackPos[0] < whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to black < white')

    if playerMove == 'white':
        if blackPos[0] == None:
            isSafe = True
            print('safe is true due to no black in los')

        elif whitePos[0] == None:
            isSafe = False
            print('safe false due to black pos existing but no white pos')

        if isSafe == False:
            if blackPos[0] != None:
                isSafe = True
                print('safe set to true preparing for checking bishop and queen')
                for i in range(len(blackBishops)):
                    if blackBishops[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False
                        print('safe set to false due to bishop los')

                
                if blackQueen.hits(blackPos[0], blackPos[1]):
                    isSafe = False
                    print('safe set to false due to queen los')

    elif playerMove == 'black':
        if whitePos[0] == None:
            isSafe = True
            print('safe is true due to no white in los')
        
        elif blackPos[0] == None:
            isSafe = False
            print('safe false due to white pos existing but no black pos')

        if isSafe == False:
            if whitePos[0] != None:
                isSafe = True
                print('safe set to true preparing for checking bishop and queen')
                for i in range(len(whiteBishops)):
                    if whiteBishops[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        print('safe set to false due to bishop los')

                if whiteQueen.hits(whitePos[0], whitePos[1]):
                    isSafe = False
                    print('safe set to false due to queen los')

    if isSafe == False:
        print('not a safe move')
    
    elif isSafe == True:
        print('safe move')

    return isSafe

def threatCheckVertHoriz(playerMove, angle, oldPieceX, oldPieceY, newPieceX, newPieceY, kingX, kingY):
    isSafe = True
    whitePos = [None, None]
    blackPos = [None, None]
    hitWhite = False
    hitBlack = False

    ### Do smth to check x when king is moved

    print('king  x y vs new x y', kingX, kingY, newPieceX, newPieceY)
    
    # if playerMove == 'white':
        # if angle == 135:
    # print('checking up left')
    print('checking', angle)
    for i in range(7):
        x = threatGetX(kingX, i, angle)
        y = threatGetY(kingY, i, angle)
        print('x y is:', x, y)
        if x >= 60 and y >= 60 and x <= 340 and y <= 340:
            if playerMove == 'white':
                for j in range(len(whitePieces)):
                    if hitWhite == False:
                        if whitePieces[j].hits(x, y):
                            print('hit white')
                            hitWhite = True
                            whitePos[0] = x
                            whitePos[1] = y

                if x == oldPieceX and y == oldPieceY:
                    print('checked the old pieceX')

                if newPieceX == x and newPieceY == y and hitWhite == False:
                    
                    print('moved piece was hit after move')
                    
                    hitWhite = True
                    whitePos[0] = x
                    whitePos[1] = y

                for j in range(len(blackPieces)):
                    # if x != oldPieceX and hitBlack == False:
                    if hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            print('hit black piece')
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

            elif playerMove == 'black':
                for j in range(len(blackPieces)):
                    if hitBlack == False:
                        if blackPieces[j].hits(x, y):
                            print('hit black piece not old x')
                            hitBlack = True
                            blackPos[0] = x
                            blackPos[1] = y

                if x == oldPieceX and y == oldPieceY:
                    print('checked the old pieceX')
                    # hitBlack = True
                    ### maybe hitblack is true and set black x?
                if newPieceX == x and newPieceY == y and hitBlack == False:
                    print('moved piece was hit after move')

                    hitBlack = True
                    blackPos[0] = x
                    blackPos[1] = y

                for j in range(len(whitePieces)):
                    # if x != oldPieceX and hitWhite == False:
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
    
    print('white x:', whitePos[0])
    print('black x:', blackPos[0])

    if whitePos[0] != None and blackPos[0] != None:
        isSafe = False
        print('isSafe set to false to prepare for comparing pos')
        # if playerMove == 'white':
        if angle == 270:
            if playerMove == 'white':
                if whitePos[0] < blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe is true due to whiteX > blackX')
            elif playerMove == 'black':
                if blackPos[0] < whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe is true due to blackX > whitex')

        elif angle == 90:
            if playerMove == 'white':
                if whitePos[0] > blackPos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to whiteX < blackX')
                
            elif playerMove == 'black':
                if blackPos[0] > whitePos[0]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to blackX < whiteX')
                
        elif angle == 180:
            if playerMove == 'white':
                if whitePos[1] > blackPos[1]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to whiteY < blackY')
            elif playerMove == 'black':
                if blackPos[1] > whitePos[1]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to blackY < whiteY')
                    
        elif angle == 0:
            if playerMove == 'white':
                if whitePos[1] < blackPos[1]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to whiteY > blackY')
            elif playerMove == 'black':
                if blackPos[1] < whitePos[1]:
                    if isSafe == False:
                        isSafe = True
                        print('safe true due to blackY > whiteY')
                    

        if playerMove == 'white':
            if whitePos == blackPos:
                print('white took black and move is safe')
                isSafe = True
        
        elif playerMove == 'black':
            if whitePos == blackPos:
                print('black took white and move is safe')
                isSafe = True

    if playerMove == 'white':
        if blackPos[0] == None:
            isSafe = True
            print('safe is true due to no black in los')

        elif whitePos[0] == None:
            isSafe = False
            print('safe false due to black pos existing but no white pos')

        if isSafe == False:
            if blackPos[0] != None:
                isSafe = True
                print('safe set to true preparing for checking rook and queen')
                for i in range(len(blackRooks)):
                    if blackRooks[i].hits(blackPos[0], blackPos[1]):
                        isSafe = False
                        print('safe set to false due to bishop los')

                
                if blackQueen.hits(blackPos[0], blackPos[1]):
                    isSafe = False
                    print('safe set to false due to queen los')

    elif playerMove == 'black':
        if whitePos[0] == None:
            isSafe = True
            print('safe is true due to no white in los')
        
        elif blackPos[0] == None:
            isSafe = False
            print('safe false due to white pos existing but no black pos')

        if isSafe == False:
            if whitePos[0] != None:
                isSafe = True
                print('safe set to true preparing for checking rook and queen')
                for i in range(len(whiteRooks)):
                    if whiteRooks[i].hits(whitePos[0], whitePos[1]):
                        isSafe = False
                        print('safe set to false due to bishop los')

                if whiteQueen.hits(whitePos[0], whitePos[1]):
                    isSafe = False
                    print('safe set to false due to queen los')

    if isSafe == False:
        print('not a safe move')
    
    elif isSafe == True:
        print('safe move')

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
    # print(app.playerMove)
    ### Selects piece
    if app.phase == 1:
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

                    # print(app.piece, oldPos, pos)
                    app.whiteLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
                    app.legalMove = checkKingThreat(app.playerMove, oldPos[0], oldPos[1], pos[0], pos[1], whitePieces[0].centerX, whitePieces[0].centerY)

                elif app.playerMove == 'black':

                    app.blackLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
                    app.legalMove = checkKingThreat(app.playerMove, oldPos[0], oldPos[1], pos[0], pos[1], blackPieces[0].centerX, blackPieces[0].centerY)

            # print(pos)
            # if pos != None:
                print('legalMove is', app.legalMove)
                if app.legalMove == True:
                    posPiece(pos, oldPos)

                    wipePiece()
                

        selectedMarkers.clear()
        moveMarkers.clear()

        # if appillegalMove == False:
        app.phase = 1

    
### Test

### Test Rook
# onMousePress(60, 300)
# onMousePress(60, 220)

# onMousePress(180, 100)
# onMousePress(180, 140)

# onMousePress(60, 220)
# onMousePress(60, 180)

# onMousePress(100, 100)
# onMousePress(100, 180)

# onMousePress(60, 180)
# onMousePress(100, 140)

# onMousePress(340, 100)
# onMousePress(340, 140)


### Test king
onMousePress(220, 300)
onMousePress(220, 220)

onMousePress(220, 100)
onMousePress(220, 180)

onMousePress(180, 340)
onMousePress(300, 220)

onMousePress(180, 60)
onMousePress(300, 180)

onMousePress(260, 340)
onMousePress(140, 220)

onMousePress(260, 60)
onMousePress(140, 180)

onMousePress(180, 300)
onMousePress(180, 220)

onMousePress(180, 100)
onMousePress(180, 180)

onMousePress(260, 300)
onMousePress(260, 220)

onMousePress(260, 100)
onMousePress(260, 180)

onMousePress(140, 340)
onMousePress(220, 260)

onMousePress(140, 60)
onMousePress(220, 140)

onMousePress(100, 340)
onMousePress(60, 260)

onMousePress(100, 60)
onMousePress(60, 140)

onMousePress(300, 340)
onMousePress(340, 260)

onMousePress(300, 60)
onMousePress(340, 140)

onMousePress(220, 220)
onMousePress(180, 180)

onMousePress(220, 180)
onMousePress(180, 220)

onMousePress(220, 260)
onMousePress(180, 220)

onMousePress(300, 180)
onMousePress(260, 220)

onMousePress(180, 220)
onMousePress(220, 260)

onMousePress(260, 220)
onMousePress(220, 220)

# Rect(40, 40, 40, 40, opacity = 1)

cmu_graphics.run()
