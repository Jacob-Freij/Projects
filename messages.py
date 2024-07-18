from aprintline import lines
from aprintline import print_line
from aprintline import print_multiple_lines
import globals
import mining


def introduction():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: Print the introduction so the user knows the backstory and where to start.
  """
  
  print_line("Welcome to Mining Escapade.\n")
  print_line("\nYou are a miner. Just now, while you were mining, \nyou suddenly heard a loud boom. You rushed out and \nsaw the entrance caving in! You look around and \ndecide you have roughly 5 days or 120 hours of oxygen \nleft before you suffocate. Your only chance of escape \nis that you know there is an abandoned minecart track \nand forge somewhere. \n\nStart by exploring using w/a/s/d to move around the map \nand \"look\" to find the forge and track. You can access \nthe list of commands at any time by typing \"help\". \nDo not run out of oxygen or you will die. Press enter \nafter each action when you are ready to continue. \n\nDo not press any keys while the \ncomputer is printing.")


def list_of_commands():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: Prints the list of available commands and descriptions.
  """

  lines.append("\n\"look\" to inspect your surroundings\n")
  lines.append("\"mine\" to mine materials\n")
  lines.append("\"w\"/\"a\"/\"s\"/\"d\" to move\n")
  lines.append("\"sleep\" to regain energy\n")
  lines.append("\"forge\" to repair the minecart\n")
  lines.append("\"escape\" to escape the mine once you've repaired the minecart\n")
  lines.append("\"stats\" to see important information\n")
  lines.append("\"story\" to see the introduction again")
  print_multiple_lines(lines)


def statistics():
  """
  Owner: Alice
  Parameters: none
  Returns: none
  Purpose: Print the current game statistics, including energy, hours of oxygen left, and materials.
  """

  lines.append(f"\nEnergy: {globals.energy}\n")
  lines.append(f"Hours of oxygen: {globals.time}\n")
  lines.append(f"Materials: {mining.numIron} iron, {mining.numCopper} copper, {mining.numCoal} coal")
  
  print_multiple_lines(lines)
