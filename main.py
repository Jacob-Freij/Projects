import os

from aprintline import print_line
import energy_display
import escape
import forge
import gameover
import globals
import lookaround
import mapping
import messages
import mining
import sleep
import survivor
import win
import time_display


messages.introduction()

# The continuing variable is used throughout the program to pause
# the program between actions to give the user time to read
continuing = input("\n")

while not globals.escape:
  os.system("clear")

  if globals.time <= 0:
    gameover.gameover()
    break

  if globals.energy <= 0:
    sleep.sleep()
    continuing = input("")

  mapping.printMap()
  energy_display.energy_bar()
  time_display.time_bar()

  action = input("\nWhat would you like to do? ").lower()

  # Match statement figures out which action the user entered,
  # also handles incorrect inputs
  match action:
    case "help":
      messages.list_of_commands()
      continuing = input("")

    case "story":
      messages.introduction()
      continuing = input("")

    case "stats":
      messages.statistics()
      continuing = input("")

    case "look":
      lookaround.look(mapping.x, mapping.y)
      continuing = input("")

    case "w":
      mapping.move(action)

    case "a":
      mapping.move(action)

    case "s":
      mapping.move(action)

    case "d":
      mapping.move(action)

    case "mine":
      mineTime = input("\nHow many hours will you mine? ")

      while True:
        # Try statement to catch incorrect user input and prompt them to correct it
        try:
          mineTime = int(mineTime)
          break
        except ValueError:
          print_line("\nEnter an integer number.")
          mineTime = input("How many hours will you mine? ")

      mining.mine(mapping.x, mapping.y, mineTime)
      continuing = input("")

    case "sleep":
      sleep.sleep()
      continuing = input("")

    case "rescue":
      survivor.rescue(mapping.x, mapping.y)
      continuing = input("")

    case "forge":
      forge.forge(mapping.x, mapping.y)
      continuing = input("")

    case "escape":
      escape.escape(mapping.x, mapping.y)
      continuing = input("")

      win.win()
      if win.shouldBreak == 1:
        break

    case _:
      print_line("\nThat isn't an action. Type \"help\" \nto see the list of actions.")
      continuing = input("")
