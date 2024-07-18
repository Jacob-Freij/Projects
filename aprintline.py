import time

# Function to prints the text letter by letter
def print_line(text):
  """
  Owner: Jacob
  Parameters: text
  Returns: none
  Purpose: When used, the prints the line letter by letter for whatever strinf is in the parameter
  """
  '''
  end = "" prints the next character to directly to the right of the last character, flush = True prints each character in the string one by one instead of loading the entire string and then printing it together
  '''
  for i in text:
        
    print(i, end="", flush=True)
    time.sleep(0.01)
lines = []

def print_multiple_lines(lines):
  """
  Owner: Jacob
  Parameters: lines
  Returns: none
  Purpose: Prints multiple line, just repeats the print_line function, and prints a series of lines in the list.
  """
  for line in lines:
    print_line(line)
       
  print("")
  lines.clear()
  
