import lxml
import selenium
import time

def clickShuffle():
  shuffle = driver.find_element_by_id('catrandomp1')
  shuffle.click()


# prevTier



def tutorial():
  print('\nThis program seeks to streamline the process of finding new classical music pieces.\n')
  time.sleep(1.5)
  print('This program will accomplish its goal by using the International Music Score Library Project (IMSLP) database of composers and compositions.\n')
  time.sleep(3)
  print('You will be provided with three tiers of options to find a piece of classical music:')
  time.sleep(2)
  print('1) a completely random composer from the entire IMSLP database')
  print('2) a random or chosen popular musical era')
  print('3) a random or chosen popular composer from the established era\n') 
  time.sleep(3)
  print('If you find a random era/composer or chosen era/composer to be unfit to your liking, then you may choose to restart, OR keep running the program to produce new results.\n')
  time.sleep(3)

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

# exProtocol
 
