import globals
from aprintline import print_line

def escape(x, y):
  """
  Owner: Alice
  Parameters: x, y (coordinates to determine what room the player is in)
  Returns: none
  Purpose: Determine if the minecart has been repaired and the player can escape the collapsed mine. If not, explain why.
  """
  
  if globals.roomTypes[y-1][x-1] == "x":
    if globals.minecartRepaired is True:
      print_line("\nYou triumphantly ride the repaired minecart out of the mine!")
      globals.escape = True
    else:
      print_line("\nYou have to repair the minecart first.")
      
  else:
    print_line("\nYou can only escape on the minecart tracks.")
    