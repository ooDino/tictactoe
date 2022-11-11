grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
gameStatus = True
count = 1
n = 0


def printGrid():
    print(" | " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print(" | " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print(" | " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")


def playGame():
    if count % 2 == 0:
        grid[n] = "X"
    else:
        grid[n] = "O"


def takeInput():
    global n
    n = int(input("Please select a location for your next move (0 - 8): "))
    while grid[n] != "-":
        n = int(input("That spot is taken. Please choose another one: "))


def playAgain():
    global gameStatus, grid
    if gameStatus == False:
        check = input("Would you like to play again? Type Yes or No: ")
        if check == "Yes":
            gameStatus = True
            grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            printGrid()


def checkStatus():
    global gameStatus
    if grid[0] == grid[1] == grid[2] and grid[0] != "-":
        print("Game Over!\n" + grid[0] + " player won!")
        gameStatus = False
    elif grid[2] == grid[5] == grid[8] and grid[2] != "-":
        print("Game Over!\n" + grid[2] + " player won!")
        gameStatus = False
    elif grid[0] == grid[3] == grid[6] and grid[0] != "-":
        print("Game Over!\n" + grid[0] + " player won!")
        gameStatus = False
    elif grid[6] == grid[7] == grid[8] and grid[6] != "-":
        print("Game Over!\n" + grid[6] + " player won!")
        gameStatus = False
    elif grid[4] == grid[5] == grid[6] and grid[4] != "-":
        print("Game Over!\n" + grid[4] + " player won!")
        gameStatus = False
    elif grid[1] == grid[4] == grid[7] and grid[1] != "-":
        print("Game Over!\n" + grid[4] + " player won!")
        gameStatus = False
    elif grid[0] == grid[4] == grid[8] and grid[0] != "-":
        print("Game Over!\n" + grid[0] + " player won!")
        gameStatus = False
    elif grid[2] == grid[4] == grid[6] and grid[2] != "-":
        print("Game Over!\n" + grid[2] + " player won!")
        gameStatus = False

    playAgain()


printGrid()

while gameStatus:
    takeInput()
    playGame()
    printGrid()
    checkStatus()
    count += 1
