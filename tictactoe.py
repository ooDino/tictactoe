import pygame, sys

# Constants
WIDTH = 600
HEIGHT = 600
BG_RGB = (211, 211, 211)
GRID_RGB = (255, 255, 255)
O_RGB = (242, 82, 120)
X_RGB = (0, 138, 195)
GAMEOVER_RGB = (0, 0, 0)

# Counter used for turns
turn = True

# Class box -> stores the state of the box
class box:
    def __init__(self, used, player):
        self.used = used
        self.player = player


# Check if a box was drawn in
box0 = box(False, "")
box1 = box(False, "")
box2 = box(False, "")
box3 = box(False, "")
box4 = box(False, "")
box5 = box(False, "")
box6 = box(False, "")
box7 = box(False, "")
box8 = box(False, "")

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_RGB)

# Draw the grid
pygame.draw.line(screen, GRID_RGB, (200, 0), (200, 600), 10)
pygame.draw.line(screen, GRID_RGB, (400, 0), (400, 600), 10)
pygame.draw.line(screen, GRID_RGB, (0, 200), (600, 200), 10)
pygame.draw.line(screen, GRID_RGB, (0, 400), (600, 400), 10)

# Function drawX -> draws X
def drawX(x, y):
    pygame.draw.line(screen, X_RGB, (x, y), (x + 100, y + 100), 20)
    pygame.draw.line(screen, X_RGB, (x + 100, y), (x, y + 100), 20)


# Function drawO -> draws Y
def drawO(x, y):
    pygame.draw.circle(screen, O_RGB, (x, y), 65, 15)


# Function checkTurn -> checks whose turn it is
def checkTurn() -> bool:
    global turn
    if turn:
        turn = not turn
        return not turn
    elif not turn:
        turn = not turn
        return not turn


# Checks if a button is pressed and draws appropriate symbol
def checkInput():
    global box0, box1, box2, box3, box4, box5, box6, box7, box8
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        # first row
        if x >= 0 and x <= 200 and y >= 0 and y <= 200 and not box0.used:
            if checkTurn():
                drawO(100, 100)
                box0.player = "O"
            else:
                drawX(50, 50)
                box0.player = "X"
            box0.used = True
        elif x >= 200 and x <= 400 and y >= 0 and y <= 200 and not box1.used:
            if checkTurn():
                drawO(300, 100)
                box1.player = "O"
            else:
                drawX(250, 50)
                box1.player = "X"
            box1.used = True
        elif x >= 400 and x <= 600 and y >= 0 and y <= 200 and not box2.used:
            if checkTurn():
                drawO(500, 100)
                box2.player = "O"
            else:
                drawX(450, 50)
                box2.player = "X"
            box2.used = True
        # second row
        if x >= 0 and x <= 200 and y >= 200 and y <= 400 and not box3.used:
            if checkTurn():
                drawO(100, 300)
                box3.player = "O"
            else:
                drawX(50, 250)
                box3.player = "X"
            box3.used = True
        elif x >= 200 and x <= 400 and y >= 200 and y <= 400 and not box4.used:
            if checkTurn():
                drawO(300, 300)
                box4.player = "O"
            else:
                drawX(250, 250)
                box4.player = "X"
            box4.used = True
        elif x >= 400 and x <= 600 and y >= 200 and y <= 400 and not box5.used:
            if checkTurn():
                drawO(500, 300)
                box5.player = "O"
            else:
                drawX(450, 250)
                box5.player = "X"
            box5.used = True
        # third row
        elif x >= 0 and x <= 200 and y >= 400 and y <= 600 and not box6.used:
            if checkTurn():
                drawO(100, 500)
                box6.player = "O"
            else:
                drawX(50, 450)
                box6.player = "X"
            box6.used = True
        elif x >= 200 and x <= 400 and y >= 400 and y <= 600 and not box7.used:
            if checkTurn():
                drawO(300, 500)
                box7.player = "O"
            else:
                drawX(250, 450)
                box7.player = "X"
            box7.used = True
        elif x >= 400 and x <= 600 and y >= 400 and y <= 600 and not box8.used:
            if checkTurn():
                drawO(500, 500)
                box8.player = "O"
            else:
                drawX(450, 450)
                box8.player = "X"
            box8.used = True


# Checks if the game is over
def gameState() -> bool:
    if box0.player == box1.player == box2.player and box0.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (25, 100), (575, 100), 20)
        return True
    elif box0.player == box3.player == box6.player and box0.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (100, 25), (100, 575), 20)
        return True
    elif box6.player == box7.player == box8.player and box6.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (25, 500), (575, 500), 20)
        return True
    elif box2.player == box5.player == box8.player and box2.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (500, 25), (500, 575), 20)
        return True
    elif box3.player == box4.player == box5.player and box3.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (25, 300), (575, 300), 20)
        return True
    elif box2.player == box4.player == box6.player and box2.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (575, 25), (25, 575), 20)
        return True
    elif box0.player == box4.player == box8.player and box0.player != "":
        pygame.draw.line(screen, GAMEOVER_RGB, (25, 25), (575, 575), 20)
        return True
    else:
        return False


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    check = gameState()
    if gameState():
        image = pygame.image.load("gameover.png")
        screen.blit(image, (160, 190))
        wait = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
        checkInput()
    pygame.display.update()
