import globals

maxEnergy = 100
# Amount of energy per dash
increment = 10 

def energy_bar():
  """
  Owner: Jacob
  Parameters: none
  Returns: none
  Purpose: Creates the energy bar on screen to show energy remaining. 
  """
  
  # Calculates max amount of dashes there will be
  max_dashes = 100/increment  
  
  # Calculates the amount of dashes worth of energy there is
  current_dashes = int((globals.energy) / max_dashes)
  # Gets the amount of empty space there should be if there is less than max dashes
  empty_spaces = increment - current_dashes
  bar_display  = "-" * current_dashes
  # Gets the correct amount of empty space and converts it to empty space
  length_display = " " * empty_spaces

  print("")
  print("Energy remaining: " + "|" + bar_display + length_display + "|")
  print(" "*20 + f"{globals.energy}/{maxEnergy}")
