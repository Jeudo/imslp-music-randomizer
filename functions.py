import lxml
import selenium
from selenium import webdriver
import time
import os

# prevTier


def tutorial():
  print('\nThis program seeks to streamline the process of finding new classical music pieces.\n')
  print('This program will accomplish its goal by using the International Music Score Library Project (IMSLP) database of composers and compositions.\n')
  print('You will be provided with three tiers of options to find a piece of classical music:')
  print('1) a completely random composer from the entire IMSLP database')
  print('2) a random or chosen popular musical era')
  print('3) a random or chosen popular composer from the established era\n') 
  print('If you find a random era/composer or chosen era/composer to be unfit to your liking, then you may choose to restart, OR keep running the program to produce new results.\n')

def movingOn():
  print('Would you like a random composer, or to continue on to the musical eras?\n')
  time.sleep(1.5)

def iterIntro():
  tut_conf = input('Type "t" for the tutorial or "s" to skip it: ')
  if tut_conf.lower() == 't':
    tutorial()
    movingOn()
  elif tut_conf.lower() == 's':
    movingOn()
  else:
    print('\nInvalid input. Please try again.')
    iterIntro()

eraTier = "All right- moving on to the musical eras."

def iterFirstTier():
  first_tier = input('Type "r" for a random composer from the entire IMSLP database, or "e" to continue to the musical eras: ')
  if first_tier.lower() == 'r':
    print("Choice confirmed: random composer. Check the program once you are done looking at the webpage.")
    time.sleep(1.5)
    driver = webdriver.Chrome() 
    driver.get('https://imslp.org/wiki/Category:Composers')
    driver.maximize_window()
    shuffle = driver.find_element_by_class_name('cattool')
    shuffle.click()
    while True:
      restart = input("Would you like to end the program and close your tabs? Type 'y' for yes and 'n' for no. ")
      if restart.lower() == 'y':
        print("Thank you for using this program!")
        time.sleep(2)
        break
      elif restart.lower() == 'n':
        print("The program will now wait for 5 minutes and close after time is up.")
        print("You may also close the program whenever you please, but know that the created tabs will close when the program closes.")
        time.sleep(300)
        break
  elif first_tier.lower() == 'e':
    print(eraTier)
  else:
    print('\nInvalid input. Please try again.')
    iterFirstTier()

# exProtocol
 