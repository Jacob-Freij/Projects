import os

from aprintline import print_line


def gameover():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: If oxygen runs out, end the game and print game over message.
  """
  
  os.system("clear")
  print_line("You died from lack of oxygen and did \nnot make it out of the mine. Maybe in \nthe future someone will excavate the \ncollapsed mine and discover your body.")
  
  