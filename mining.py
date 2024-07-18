import time

import globals
import messages
from aprintline import print_line

numIron = 0
numCoal = 0
numCopper = 0

# Four 2D lists to track type of metals in each room, and amount of each metal
metals = [["e", "e", "e", "e", "e", "e", "e", "e", "e"],
          ["e", "e", "c", "e", "i", "e", "e", "e", "e"],
          ["e", "e", "i", "e", "p", "e", "e", "e", "e"],
          ["e", "e", "e", "e", "i", "e", "e", "e", "e"],
          ["e", "e", "e", "i", "e", "c", "e", "e", "e"],
          ["e", "e", "e", "e", "e", "e", "e", "e", "e"]]

iron = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 30, 0, 0, 0, 0],
        [0, 0, 20, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 50, 0, 0, 0, 0],
        [0, 0, 0, 10, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

coal = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 70, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 60, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

copper = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 40, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def mine(x, y, mineTime):
  """
  Owner: Alice
  Parameters: x, y (coordinates to determine what room the player is in), mineTime
  Returns: none  
  Purpose: Figure out which metal the player is mining using several 2D lists, and modify the appropriate variables to keep track of metal mined, metal that remains, and time spent.
  """

  global numIron, numCoal, numCopper
  global metals, iron, coal, copper

  # Uses y-1 and x-1 because of how the metals 2D list is designed: the row index is looked at first (y), and the column index is looked at second in the chosen row (x).
  # -1 is because mapping.map list size and metals list size are 1 different

  # Check which type of metal
  if metals[y - 1][x - 1] == "i":
    # Only start mining if there are materials in the room
    if iron[y - 1][x - 1] > 0:
      # Keep mining for the specified amount of time
      for _ in range(0, mineTime):
        # Stop mining if all the materials have been mined
        if iron[y - 1][x - 1] > 0:
          # Adjust appropriate variables
          numIron += globals.mineSpeed
          iron[y - 1][x - 1] -= globals.mineSpeed
          
          globals.time -= 1
          globals.energy -= 15
      print(". . .")
      time.sleep(1)
      messages.statistics()
    else:
      print_line("\nYou already mined everything here.")

  # Repeat with other two materials
  elif metals[y - 1][x - 1] == "c":
    if coal[y - 1][x - 1] > 0:
      for _ in range(0, mineTime):
        if coal[y - 1][x - 1] > 0:
          numCoal += globals.mineSpeed
          coal[y - 1][x - 1] -= globals.mineSpeed
          
          globals.time -= 1
          globals.energy -= 15
      print(". . .")
      time.sleep(1)
      messages.statistics()
    else:
      print_line("\nYou already mined everything here.")

  elif metals[y - 1][x - 1] == "p":
    if copper[y - 1][x - 1] > 0:
      for _ in range(0, mineTime):
        if copper[y - 1][x - 1] > 0:
          numCopper += globals.mineSpeed
          copper[y - 1][x - 1] -= globals.mineSpeed
          
          globals.time -= 1
          globals.energy -= 15
      print(". . .")
      time.sleep(1)
      messages.statistics()
    else:
      print_line("\nYou already mined everything here.")
        
  else:
    print_line("\nYou can't mine here.")
