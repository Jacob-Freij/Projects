import globals

maxtime = 120
# Number of dashes, represents 10 hours each
numDashes = 12

def time_bar():
  """
  Owner: Jacob
  Parameters: none
  Returns: none
  Purpose: Creates the time bar on screen to show time remaining.
  """
  # Calculate the number of hours each dash represents
  hours_per_dash = maxtime / numDashes

  # Calculate the number of dashes representing the elapsed time
  current_dashes = int(globals.time / hours_per_dash)

  # Create the time bar display
  bar_display = "-" * current_dashes
  empty_spaces = numDashes - current_dashes
  length_display = " " * empty_spaces

  # Print the time bar
  print("Hours remaining: " + "|" + bar_display + length_display + "|")
  print((" "*20) +f"{globals.time}/{maxtime}")
