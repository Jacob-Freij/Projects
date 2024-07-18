import random
import time
import os

import globals
import messages
from aprintline import print_line


def sleep():
  """
  Owner: Jacob
  Parameters: none
  Returns: none
  Purpose: Choose a random number of hours for the user to sleep depending on the amount of energy, and afterwards restore energy to 100.
  """

  tired_lvl_1 = random.randint(4, 5)
  tired_lvl_2 = random.randint(6, 7)
  tired_lvl_3 = random.randint(8, 9)

  if globals.energy == 100:
    print_line("\nYou don't need to sleep right now.")
  else:
    print_line("\nYou find a place to rest your head.")
    os.system("clear")

    if globals.energy >= 50:
      globals.time -= tired_lvl_1
      print_line(f'\nYou slept for {tired_lvl_1} hours to replenish \nyour energy.')
    elif globals.energy >= 35:
      globals.time -= tired_lvl_2
      print_line(f'\nYou slept for {tired_lvl_2} hours to replenish \nyour energy.')
    elif globals.energy >= 20:
      globals.time -= tired_lvl_3
      print_line(f'\nYou slept for {tired_lvl_3} hours to replenish \nyour energy.')
    else:
      print_line("\nYou fall to the ground from exhaustion \nand sleep for 10 hours.")
      globals.time -= 10

    globals.energy = 100

    print("\n. . .")
    time.sleep(1)
    

    messages.statistics()
