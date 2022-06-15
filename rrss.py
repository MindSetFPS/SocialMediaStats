import twint
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

c = twint.Config()

#To do: Screenshot specific windows regardless of what is in top of screen. (Obs does this, so it should be possible in theory)

#A Jornada has 3 moments: GameDay, Live and Results
c.Username = "newstargg"

tweets = []
gamedays = []
live = []
results_derrota = []
results_victoria = []

#search wins
c.Search = "GANAMOS  #LigaDeHonorEntel "
c.Store_object = True
c.Store_object_tweets_list = results_victoria

twint.run.Search(c)

#search defeats
c.Search = "DERROTA  #LigaDeHonorEntel "
c.Store_object_tweets_list = results_derrota

twint.run.Search(c)

#search gamedays
c.Search = "#LoL | Liga De Honor Entel 🏆"
c.Store_object_tweets_list = gamedays
twint.run.Search(c)

#setup profile
pf = webdriver.FirefoxProfile("/home/daniel/.mozilla/firefox/4rato2pw.newstar")
#open browser
browser = webdriver.Firefox(executable_path='/home/daniel/Documents/cocina/spamgenerator/geckodriver', firefox_profile=pf)
time.sleep(4)

for tweet in results_victoria:
    print(tweet.link)
    #take screenshot
    browser.get(tweet.link + '/analytics')
    time.sleep(4)
    #for FHD screen
    pyautogui.screenshot( 'Resultado ' + tweet.datestamp + '.png', region=(663, 306, 590, 500))

for tweet in results_derrota:
    print(tweet.link)
    #take screenshot
    browser.get(tweet.link + '/analytics')
    time.sleep(4)
    #for FHD screen
    pyautogui.screenshot( 'Resultado ' + tweet.datestamp + '.png', region=(663, 306, 590, 500))

for tweet in gamedays:
    print(tweet.link)
    #take screenshot
    browser.get(tweet.link + '/analytics')
    time.sleep(4)
    #for FHD screen
    pyautogui.screenshot( 'Gameday ' + tweet.datestamp + '.png', region=(663, 306, 590, 500))

browser.quit()
#1 - Open Browser
#2 - Open GameDay 
#3 - Show statistics
#4 - Take screenshot
#5 - Copy numbers