
def DisplayBoard(board):
  #
  # the function accepts one parameter containing the board's current status
  # and prints it out to the console
  #
  print("+" + 3 * "-------+")
  print("|" + 3 * (7 * " " + "|"))
  for column in range(3):
      print("|" + (2 * " "), board[0][column], (2 * " "), end="")
  print("|")
  print("|" + 3 * (7 * " " + "|"))
  print("+" + 3 * "-------+")
  print("|" + 3 * (7 * " " + "|"))
  for column in range(3):
      print("|" + (2 * " "), board[1][column], (2 * " "), end="")
  print("|")
  print("|" + 3 * (7 * " " + "|"))
  print("+" + 3 * "-------+")
  print("|" + 3 * (7 * " " + "|"))
  for column in range(3):
      print("|" + (2 * " "), board[2][column], (2 * " "), end="")
  print("|")
  print("|" + 3 * (7 * " " + "|"))
  print("+" + 3 * "-------+")

def EnterMove(board): 
  #
  # the function accepts the board current status, asks the user about their move,
  # checks the input and updates the board according to the user's decision
  #
  # while squareAllocated is False. keep prompting the user to enter their move
  squareAllocated = False
  while not squareAllocated:
    no = input("Enter your move: ")
    valid_range = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while no not in valid_range:
      no = input("Enter your move: ")

    no = int(no)

    for row in range(3):
      for column in range(3):
        if board[row][column] == no:
          board[row][column] = "O"
          squareAllocated = True

def DrawMove(board):
  #  
  # the function draws the computer's move and updates the board
  #
  print ("Computer's Move:")
  from random import randrange

  # while squareAllocated is False. a new random no is generated
  squareAllocated = False
  while not squareAllocated:
    no = randrange(1, 10)
    for row in range(3):
        for column in range(3):
          if board[row][column] == no:
            board[row][column] = "X"
            squareAllocated = True

def MakeListOfFreeFields(board):
  #
  # the function browses the board and builds a list of all the free squares;
  # the list consists of tuples, while each tuple is a pair of row and column numbers
  #
  # need to start off with listofFreeFields being empty every time
  global listofFreeFields
  listofFreeFields = []

  for row in range(3):
      for column in range(3):
          if type(board[row][column]) == int:
              listofFreeFields.append((row, column))
  return listofFreeFields

def VictoryFor(board, sign):
  #  
  # the function analyzes the board status in order to check if
  # the player using 'O's or 'X's has won the game
  # 
  global gameStillRunning 

  players = {"X":"computer", "O": "user"}
  # check for win in rows
  for row in board:
    if sign == row[0] == row[1] == row[2]:
      print ("The game is over, the", players[sign], "has won!")
      gameStillRunning = False
      return gameStillRunning
  
  # check for win in columns
  for column in range(3):
    if sign == board[0][column] == board[1][column] == board[2][column]:
      print ("The game is over, the", players[sign], "has won!")
      gameStillRunning = False
      return gameStillRunning

  # check for win in diagonals
  if sign == board[0][0] == board[1][1] == board[2][2]:
    print ("The game is over, the", players[sign], "has won!")
    gameStillRunning = False
    return gameStillRunning
  if sign == board[0][2] == board[1][1] == board[2][0]:
    print ("The game is over, the", players[sign], "has won!")
    gameStillRunning = False
    return gameStillRunning

  # check for tie
  if MakeListOfFreeFields(board) == []:
      print ("The game has ended in a tie!")
      gameStillRunning = False
      return gameStillRunning



# MAIN CODE #
# define variables
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
listofFreeFields = []
gameStillRunning = True
sign = "O"

DisplayBoard(board)

# define game loop
while gameStillRunning:
  if sign == "O":
    EnterMove(board) # user makes their move; board is updated
    DisplayBoard(board)
    #print(MakeListOfFreeFields(board))
  elif sign == "X":
    DrawMove(board) # computer makes their move; board is updated
    DisplayBoard(board)
    #print(MakeListOfFreeFields(board))
  VictoryFor(board, sign)
  # if MakeListOfFreeFields(board) == []:
  #     print ("Its a tie")
  #     gameStillRunning = False
  if sign == "O":
    sign = "X"
  elif sign == "X":
    sign = "O"


