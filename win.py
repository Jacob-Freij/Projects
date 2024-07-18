import os

import globals
from aprintline import print_line

# shouldBreak is used to be able to break the while loop in main
# when the user wins
shouldBreak = 0

def win():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: If player wins, clear the screen and print a congratulatory message.
  """
  global shouldBreak
  
  if globals.minecartRepaired is True:
    os.system("clear")
    print_line("Congratulations! You live a happy life outside of the mine.")
    shouldBreak = 1
