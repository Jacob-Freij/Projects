
from aprintline import print_line
import chancerooms


# Use x and y as coordinates
# These will be used in several other functions to determine which room the player is in
x = 1
y = 1

# 2D list to create the map (" " for passable room, "b" for blocked area, "X" for player)
# The strings that correspond with the rooms on the map can be modified to show where the
# player is 
rooms = [["X", " ", " ", "b", "b", "b", "b", "b", "b"],
         [" ", " ", " ", "b", " ", "b", "b", "b", "b"],
         [" ", "b", " ", " ", " ", " ", "b", "b", "b"],
         ["b", "b", " ", " ", " ", " ", " ", "b", "b"],
         ["b", "b", "b", " ", " ", " ", " ", " ", " "],
         ["b", "b", "b", "b", "b", " ", " ", " ", " "]]

def printMap():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: Prints the map. Uses f-strings and strings from above 2D list to be able to modify the middle character of each room to show where the player is.
  """
  
  print(" ___ ___ ___ ")
  print("|   |   |   |")
  print(f"| {rooms[0][0]}   {rooms[0][1]}   {rooms[0][2]} |")
  print("|_ _|_ _|_ _|    ___")
  print("|   |   |   |   |   |")
  print(f"| {rooms[1][0]}   {rooms[1][1]}   {rooms[1][2]} |   | {rooms[1][4]} |")
  print("|_ _|___|_ _|___|_ _|___")
  print("|   |   |   |   |   |   |")
  print(f"| {rooms[2][0]} |   | {rooms[2][2]}   {rooms[2][3]}   {rooms[2][4]}   {rooms[2][5]} |")
  print("|___|   |_ _|_ _|_ _|_ _|___")
  print("        |   |   |   |   |   |")
  print(f"        | {rooms[3][2]}   {rooms[3][3]}   {rooms[3][4]}   {rooms[3][5]}   {rooms[3][6]} |")
  print("        |___|_ _|_ _|_ _|_ _|___ ___")
  print("            |   |   |   |   |   |   |")
  print(f"            | {rooms[4][3]}   {rooms[4][4]}   {rooms[4][5]}   {rooms[4][6]}   {rooms[4][7]}   {rooms[4][8]} |")
  print("            |___|___|_ _|_ _|_ _|_ _|")
  print("                    |   |   |   |   |")
  print(f"                    | {rooms[5][5]}   {rooms[5][6]}   {rooms[5][7]}   {rooms[5][8]} |")
  print("                    |___|___|___|___|")

def move(action):
  """
  Owner: Alice
  Parameters: action (used to determine from user input which direction to move the player)
  Returns: none
  Purpose: From user input, using a 2D list either move the player to the chosen room or print that the way is blocked. Modify the rooms 2D list to correctly show where the player is.
  """

  # Specifies that the function should be using the global variables x and y, instead of
  # creating two new local ones
  global x, y

  # 2D list that is used to compare whether a room is open (o) or blocked (b), using coordinates
  # Also has an extra square of blocked rooms around the perimeter to keep the player on the map
  map = [["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
         ["b", "o", "o", "o", "b", "b", "b", "b", "b", "b", "b"],
         ["b", "o", "o", "o", "b", "o", "b", "b", "b", "b", "b"],
         ["b", "o", "b", "o", "o", "o", "o", "b", "b", "b", "b"],
         ["b", "b", "b", "o", "o", "o", "o", "o", "b", "b", "b"],
         ["b", "b", "b", "b", "o", "o", "o", "o", "o", "o", "b"],
         ["b", "b", "b", "b", "b", "b", "o", "o", "o", "o", "b"],
         ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]]

  # Checks if the action is allowable, and modifies the strings in rooms to display the proper
  # character position. Also runs chancerooms function
  if action == "w":
    if map[y-1][x] == "o":
      chancerooms.chanceroom(x, y)
      rooms[y-1][x-1] = " "
      y -= 1
      rooms[y-1][x-1] = "X"
    else:
      print_line("\nYou can't move that way.")
      continuing = input("")
      
  elif action == "s":
    if map[y+1][x] == "o":
      chancerooms.chanceroom(x, y)
      rooms[y-1][x-1] = " "
      y += 1
      rooms[y-1][x-1] = "X"
    else:
      print_line("\nYou can't move that way.")
      continuing = input("")
      
  elif action == "a":
    if map[y][x-1] == "o":
      chancerooms.chanceroom(x, y)
      rooms[y-1][x-1] = " "
      x -= 1
      rooms[y-1][x-1] = "X"
    else:
      print_line("\nYou can't move that way.")
      continuing = input("")
      
  elif action == "d":
    if map[y][x+1] == "o":
      chancerooms.chanceroom(x, y)
      rooms[y-1][x-1] = " "
      x += 1
      rooms[y-1][x-1] = "X"
    else:
      print_line("\nYou can't move that way.")
      continuing = input("")
  