import lxml
import selenium
from selenium import webdriver
import time
from composers import *
import random

def exProtocol():
  while True:
    restart = input("Would you like to end the program and close your tabs? Type 'y' for yes and 'n' for no. ")
    if restart.lower() == 'y':
      print("\nThank you for using this program!")
      time.sleep(2)
      break
    elif restart.lower() == 'n':
      print("The program will now wait for 5 minutes and close after the time is up.")
      print("You may also close the program whenever you please, but know that the created tabs will close when the program closes.")
      time.sleep(300)
      break

def tutorial():
  print('\nThis program seeks to streamline the process of finding new classical music pieces.\n')
  print('This program will accomplish its goal by using the International Music Score Library Project (IMSLP) database of composers and compositions.\n')
  print('You will be provided with three tiers of options to find a piece of classical music:')
  print('1) a completely random composer from the entire IMSLP database')
  print('2) a random or chosen popular musical era')
  print('3) a random or chosen popular composer from the established era\n') 
  print('If you find a random era/composer or chosen era/composer to be unfit to your liking, then you may choose to restart, OR keep running the program to produce new results.')
  print('\nWhile the webpages are loading, do not click out of the tab or else the program will malfunction and you will have to press the IMSLP Shuffle button (🔀) on your own.')

def movingOn():
  print('\nWould you like a random composer, or to continue on to the musical eras?')
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

eraTier = "\nAll right- moving on to the musical eras.\n"

def iterFirstTier():
  first_tier = input('Type "r" for a random composer from the entire IMSLP database, or "e" to continue to the musical eras: ')
  if first_tier.lower() == 'r':
    print("\nChoice confirmed: random composer. Check the program once you are done looking at the webpage.")
    time.sleep(1.5)
    driver = webdriver.Chrome() 
    driver.get('https://imslp.org/wiki/Category:Composers')
    driver.maximize_window()
    shuffle = driver.find_element_by_class_name('cattool')
    shuffle.click()
    exProtocol()
  elif first_tier.lower() == 'e':
    print(eraTier)
  else:
    print('\nInvalid input. Please try again.')
    iterFirstTier()

def eraReset():
    collection_list = ['Baroque', 'Classical', 'Romantic', 'Modern']
    randomEra(collection_list)

def randomEra(collection_list):
    if len(collection_list) > 0:
        print("\nYour random era is: ")
        random_era = random.choice(collection_list)
        print(random_era)
        collection_list.remove(random_era)
        print("Would you like another choice, or to continue to the next section?")
        conf = input('Type "r" for another random choice, or "c" to continue to the next section: ')
        if conf.lower() == 'r':
            randomEra(collection_list)
        elif conf.lower() == 'c':
          iterThirdTier(random_era)
        else:
          print("\nInvalid input. Please try again")
          iterSecondTier()
    elif len(collection_list) == 0:
        eraReset()

def iterSecondTier():
  print("Here are the musical eras: \n")
  for item in collection_list:
    print(item),
  print('\nWould you like a random or chosen era?')
  rc_era = input('Type "r" for a random era or "c" for a chosen era: ')
  if rc_era.lower() == 'r':
    eraReset()
  elif rc_era.lower() == 'c':
    era_inquiry = input("\nWhich era would you like? Choose from the above list by typing the era: ")
    if era_inquiry.lower().title() in collection_list:
      iterThirdTier(era_inquiry.lower().title())
    else:
      print("\nInvalid input. Please try again.")
      iterSecondTier()
  else:
    print("\nInvalid input. Please try again")
    iterSecondTier()


def iterThirdTier(era):
  print("\nYou have chosen the {} era. Here are all the composers in {} era:".format(str(era).lower().title(),str(era).lower().title()))
  final_era = collection[era]
  print(list(final_era.keys()))
  print("Would you like a random or chosen composer?")
  rc_compose = input('Type "r" for a random composer or "c" for a chosen composer: ')
  era_keys = final_era.keys()
  era_values = final_era.values()
  if rc_compose.lower() == 'r':
    shuffle_era = random.choice(list(era_keys))
    print("\nRandom composer: {}".format(str(shuffle_era)))
    print("Would you like to continue to the composer's webpage or have another random entry?")
    will_you = input('Type "c" for continue or "r" for another random composer: ')
    if will_you.lower() == 'c':
      print("\nUnderstood. Opening {}'s webpage.".format(str(shuffle_era).lower().title()))
      web_opening = list(era_values)[list(era_keys).index(shuffle_era)]
      time.sleep(1.5)
      driver = webdriver.Chrome() 
      driver.get(web_opening)
      driver.maximize_window()
      shuffle = driver.find_element_by_class_name('cattool')
      shuffle.click()
      exProtocol()
    elif will_you.lower() == 'r':
      iterThirdTier(era)
    else:
      print("\nInvalid input. Please try again.")
      iterThirdTier(era)
  elif rc_compose.lower() == 'c':
    print("Enter the number of the composer, as it appears in the following list.")
    index = 0
    for item in final_era:
      print(index, item)
      index += 1
    choose_comp = input("Enter the number here: ")
    if 0 <= int(choose_comp) <= (len(era_keys) - 1):
      final_comp = list(era_keys)[int(choose_comp)]
      print("Composer chosen. Pulling up {}'s webpage.".format(final_comp))
      web_opening = list(era_values)[list(era_keys).index(final_comp)]
      time.sleep(1.5)
      driver = webdriver.Chrome() 
      driver.get(web_opening)
      driver.maximize_window()
      shuffle = driver.find_element_by_class_name('cattool')
      shuffle.click()
      exProtocol()
    else:
      print("\nInvalid input. Please try again.")
      iterThirdTier()
  else:
    print("\nInvalid input. Please try again.")
    iterThirdTier(era)
