import globals
import mining
from aprintline import print_line

def forge(x, y):
  """
  Owner: Alice
  Parameters: x, y (coordinates to determine what room the player is in)
  Returns: none
  Purpose: Determine if the user has enough materials to repair the minecart, and if so repair it. If not explain why.
  """

  if globals.roomTypes[y - 1][x - 1] == "f":
    if (mining.numIron >= 70) & (mining.numCopper >= 30) & (mining.numCoal>= 100):
      globals.minecartRepaired = True
      print_line("\nYou successfully repaired the minecart!")
    else:
      print_line("\nYou don't have enough materials \nto repair the minecart yet.")
      
  else:
    print_line("\nYou aren't in the forge.")
