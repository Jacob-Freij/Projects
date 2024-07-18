import random

from aprintline import print_line
import globals
import mining



def stalactite_loss():
  """
  Owner: Jacob
  Parameters: none
  Returns: none
  Purpose: If the player enters the stalactite room, apply a random chance of harm from falling stalactites.
  """

  energyloss = [10, 15, 20]
  random_index = random.randint(0, 2)
  odds = random.randint(0, 2)
# 1 in 3 chance of activating
  if (odds):
    print_line("\nYou step lightly to carefully avoid the \nstalactites, and luckily don't get hurt.")
    
  else:
    print_line(f"\nYou hear rumbling. Before you can \nmove, a stalactite falls on you \nand you lose {energyloss[random_index]} energy.")
    globals.energy -= energyloss[random_index]

  continuing = input("")

def tarpit_loss():
  """
  Owner: Jacob
  Parameters: none
  Returns: none
  Purpose: When the player enters a room with a tarpit, apply a random chance to drop some items in the tarpit.
  """

  materials = ["iron", "coal", "copper"]

  if random.randint(0, 1) == 1:
    random_material = random.choice(materials)

    if random_material == "iron":
      if mining.numIron >= 2:
        mining.numIron -= 2
        print_line("\nYou venture through the tarpit. \nWhen you get out, you realize \nyou lost 2 iron.")
      else:
        print_line("\nYou venture through the tarpit, \nand luckily keep all your materials.")
    elif random_material == "coal":
      if mining.numCoal >= 2:
        mining.numCoal -= 2
        print_line("\nYou venture through the tarpit. \nWhen you get out, you realize \nyou lost 2 coal.")
      else:
        print_line("\nYou venture through the tarpit, \nand luckily keep all your materials.")

    elif random_material == "copper":
      if mining.numCopper >= 2:
        mining.numCopper -= 2
        print_line("\nYou venture through the tarpit. \nWhen you get out, you realize \nyou lost 2 copper.")
      else:
        print_line("\nYou venture through the tarpit, \nand luckily keep all your materials.")
  else:
    print_line("\nYou venture through the tarpit, \nand luckily keep all your materials.")
  print_line(f"\n\nMaterials: {mining.numIron} iron, {mining.numCopper} copper, {mining.numCoal} coal")
  
  continuing = input("")

def chanceroom(x, y):
  """
  Owner: Jacob
  Parameters: x, y (coordinates to determine what room the player is in) 
  Returns: none
  Purpose: Figures out if the room is a tarpit or a stalactite, if so runs the appropiate function.
  """

  if globals.roomTypes[y-1][x-1] == "l":
    stalactite_loss()
  if globals.roomTypes[y-1][x-1] == "t":
    tarpit_loss()
