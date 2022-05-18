from calendar import TUESDAY
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

            r = Rect(40 + col * 40, 40 + row * 40, 40, 40, fill = color)
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

## test pawn
# drawPawn('navajoWhite', 220, 260)
# whitePieces.append(whitePawns[8])


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
                moveDown = True
                moveR = True
                moveL = True

                if vert == '8':
                    moveUp = False
                elif vert == '1':
                    moveDown = False

                if horiz == 'A':
                    moveL = False
                elif horiz == 'G':
                    moveR = False

                if playerMove == 'white':
                    count = 1
                    # while moveUp == True:
                    # for j in range(8):
                    #     print(count)
                        
                    #     for i in range(len(whitePieces)):
                    #         targetX = whitePieces[i].centerX
                    #         targetY = whitePieces[i].centerY

                    #         print('move up is', moveUp)

                    #         if board[row-count][col].hits(targetX, targetY):
                    #             moveUp = False
                    #             print('move up disabled because of hit white piece')
                    #         elif board[row-count][col].centerY < 60:
                    #             moveUp = False
                    #             print('move up disabled because of board boundaries')
                    #         else:
                    #             addMoveMarker(row-count, col)
                    #             print('added marker at', row-count, col)
                    #         if moveUp == False:
                    #             break
                    #     count += 1
                    # for x in range

                    

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
    print('newTurn is called and next player is', app.playerMove)
    if app.playerMove == 'white':
        print('app.playerMove is white')
        app.playerMove = 'black'
    elif app.playerMove == 'black':
        print('app.playerMove is black')
        app.playerMove = 'white'                    

def posPiece(pos):
    app.piece.centerX = pos[0]
    app.piece.centerY = pos[1]
    if app.playerMove == 'white':
        if app.whiteLastMove[0] == 'White Pawn' and (app.whiteLastMove[1] == 'FrontLeft' or app.whiteLastMove[1] == 'FrontRight'):
            passantWipe()
    elif app.playerMove == 'black':
        if app.blackLastMove[0] == 'Black Pawn' and (app.blackLastMove[1] == 'FrontLeft' or app.blackLastMove[1] == 'FrontRight'):
            passantWipe()

def passantWipe():
    if app.playerMove == 'white':
        x = app.whiteLastMove[2]
        y = app.whiteLastMove[3] + 40
        listLen = len(blackPieces)
        for i in range(len(blackPieces)):
            print(i)
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
            print(i)
            if len(whitePieces) == listLen:
                if whitePieces[i].hits(x, y):
                    print(whitePieces[i].name)
                    delPiece = whitePieces.pop(i)
                    delPiece.visible = False

def wipePiece():
    if app.playerMove == 'white':
        listLen = len(blackPieces)
        for i in range(len(blackPieces)):
            print(i)
            if len(blackPieces) == listLen:
                if app.piece.hitsShape(blackPieces[i]):
                    print(blackPieces[i].name)
                    delPiece = blackPieces.pop(i)
                    delPiece.visible = False
        newTurn()

    elif app.playerMove == 'black':
        listLen = len(whitePieces)
        for i in range(len(whitePieces)):
            print(i)
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
    if app.playerMove == 'black':
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
    lastMove.append(moveType)
    lastMove.append(newX)
    lastMove.append(newY)
    print('y diff was', dy)
    print('last move was', lastMove)
    return lastMove

app.phase = 1
app.piece = None
app.playerMove = 'white'
app.whiteLastMove = [None, None, None, None]
app.blackLastMove = [None, None, None, None]


def onMousePress(mouseX, mouseY):
    print(app.playerMove)
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

    elif app.phase == 2:
        if moveMarkers != None:
            oldPos = [app.piece.centerX, app.piece.centerY]
            pos = movePiece(mouseX, mouseY)
            if app.playerMove == 'white':
                app.whiteLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
            elif app.playerMove == 'black':
                app.blackLastMove = getLastMove(app.piece, oldPos[0], oldPos[1], pos[0], pos[1])
            print(pos)
            if pos != None:

                posPiece(pos)

                wipePiece()
                

        selectedMarkers.clear()
        moveMarkers.clear()
        app.phase = 1

    
### Test

### Test Rook

onMousePress(60, 300)
onMousePress(60, 220)
onMousePress(180, 100)
onMousePress(180, 140)
onMousePress(60, 220)
onMousePress(60, 180)
onMousePress(100, 100)
onMousePress(100, 180)
onMousePress(60, 180)
onMousePress(100, 140)
onMousePress(340, 100)
onMousePress(340, 140)

cmu_graphics.run()
