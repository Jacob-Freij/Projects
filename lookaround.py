import globals
import mining
from aprintline import print_line

def look(x, y):
  """
  Owner: Alice
  Parameters: x, y (coordinates to determine what room the player is in)
  Returns: none
  Purpose: Use a 2D list to determine what type of room the player is in, and print a description.
  """

  # Match statement to print description based on what type of room it is
  match globals.roomTypes[y-1][x-1]:
    case "e":
      print_line("\nThe room is empty. People finished \nmining everything from here \nlong ago.")
      
    case "c":
      print_line(f"\nThe room has {mining.coal[y-1][x-1]} pieces of coal.")
      
    case "i":
      print_line(f"\nThe room has {mining.iron[y-1][x-1]} pieces of iron.")
      
    case "p":
      print_line(f"\nThe room has {mining.copper[y-1][x-1]} pieces of copper.")
      
    case "t":
      print_line("\nThe room has a giant tar pit in \nthe middle. You might lose materials \nif you go through it.")
      
    case "l":
      print_line("\nThe room has sharp stalactites \nhanging from the ceiling. They \ncould harm you if you go through \nthem.")
      
    case "s":
      print_line("\nThe room has a trapped survivor. \nHe calls out in pain. You can rescue \nhim with \"rescue\" but it will cost \nyou all your energy and 15 hours. \nHe will help you mine twice as fast.")
      
    case "f":
      print_line("\nThe room has a forge and a broken \nminecart in it. You need 70 iron, \n30 copper, and 100 coal to repair \nthe minecart.")
      
    case "x":
      print_line("\nThe room has minecart tracks running \nout a tunnel. You cannot enter \nwithout a repaired minecart.")
