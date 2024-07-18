from aprintline import print_line

import globals


def rescue(x, y):
  """
  Owner: Alice
  Parameters: x, y (coordinates used to figure out which room the player is in)
  Returns: none
  Purpose: If the user chooses to rescue the trapped person, decrease energy and time and double mining speed.
  """
  
  if globals.roomTypes[y-1][x-1] == "s":
    globals.energy = 0
    globals.time -= 15
    globals.mineSpeed *= 2
    
    print_line("\nYou spend the day digging the survivor out. \nHe is very thankful and as thanks he agrees \nto help you to mine and escape. But first, \nyou're exhausted and you have to sleep.")
  else:
    print_line("\nThere is no one to rescue here.")
    