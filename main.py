import requests
from bs4 import BeautifulSoup
from termcolor import colored
from requests.exceptions import ConnectionError
import time
import replit

replit.clear()
char = open("Bulbasaur.txt", "r")
data = char.read()
bulb = data.split("\n")
char.close()
move1 = ''
move2 = ''
move3 = ''
move4 = ''
listofhtml = []
listofhtml2 = []
listofhtml3 = []
listofhtml4 = []
website1 = ''
website2 = ''
website3 = ''
website4 = ''
list1 = []
list2 = []
list3 = []
list4 = []
MASTERLIST = []
print(
  "This is a tool that can help you find Pokèmon that are able to have the moveset that you want"
)
time.sleep(2)
print()
print()
generation = input(
  "Which Pokèmon generation would you like to search? gen1=rby gen2=gs gen3=rse gen4=dp gen5=bw gen6=xy gen7=sm gen8=swsh gen9=sv, etc. "
)
move1 = input("What would you like your Pokèmon's first move be? ")
move2 = input(
  "What would you like your Pokèmon's second move be? Enter 'null' to skip this move. "
)
move3 = input(
  "What would you like your Pokèmon's third move be? Enter 'null' to skip this move. "
)
move4 = input(
  "What would you like your Pokèmon's fourth move be? Enter 'null' to skip this move. "
)
print()
if generation == "rse":
  website1 = "www.serebii.net/attackdex/" + move1 + ".shtml"
  website2 = "www.serebii.net/attackdex/" + move2 + ".shtml"
  website3 = "www.serebii.net/attackdex/" + move3 + ".shtml"
  website4 = "www.serebii.net/attackdex/" + move4 + ".shtml"
else:
  website1 = "www.serebii.net/attackdex-" + generation + "/" + move1 + ".shtml"
  website2 = "www.serebii.net/attackdex-" + generation + "/" + move2 + ".shtml"
  website3 = "www.serebii.net/attackdex-" + generation + "/" + move3 + ".shtml"
  website4 = "www.serebii.net/attackdex-" + generation + "/" + move4 + ".shtml"
print()
if move1 == "null":
  pass
else:
  if "http://" not in website1:
    website1 = ''.join(("http://", website1))
  print("Searching...")
  time.sleep(2)
  try:
    page = requests.get(website1)
  except ConnectionError:
    print()
    print(website1)
    print(
      colored("The moveset you entered does not exist in this generation",
              "red"))
    exit()
  else:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Searching for Pokemon...")
    results = soup.find(id="content")
    p = soup.find_all('p')
    listofhtml = []
    for x in p:
      listofhtml.append(str(x))
    htmlstring=''.join(listofhtml)
    for n in range(0, 1010, 1):
      if bulb[n] in htmlstring:
        list1.append(bulb[n])

print()
print()
print()
if move2 == "null":
  pass
else:
  if "http://" not in website2:
    website2 = ''.join(("http://", website2))
  print("Searching...")
  time.sleep(2)
  try:
    page = requests.get(website2)
  except ConnectionError:
    print()
    print(
      colored("The moveset you entered does not exist in this generation",
              "red"))
    exit()
  else:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Searching for Pokemon...")
    results = soup.find(id="content")
    p = soup.find_all('p')
    listofhtml2 = []
    for x in p:
      listofhtml2.append(str(x))
    htmlstring2=''.join(listofhtml2)
    for n in range(0, 1010, 1):
      if bulb[n] in htmlstring2:
        list2.append(bulb[n])
  print()
  print()
  print()
if move3 == "null":
  pass
else:
  if "http://" not in website3:
    website3 = ''.join(("http://", website3))
  print("Searching...")
  time.sleep(2)
  try:
    page = requests.get(website3)
  except ConnectionError:
    print()
    print(
      colored("The moveset you entered does not exist in this generation",
              "red"))
    exit()
  else:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Searching for Pokemon...")
    results = soup.find(id="content")
    p = soup.find_all('p')
    listofhtml3 = []
    for x in p:
      listofhtml3.append(str(x))
    htmlstring3=''.join(listofhtml3)
    for n in range(0, 1010, 1):
      if bulb[n] in htmlstring3:
        list3.append(bulb[n])
  print()
  print()
  print()
if move4 == "null":
  pass
else:
  if "http://" not in website4:
    website4 = ''.join(("http://", website4))
  print("Searching...")
  time.sleep(2)
  try:
    page = requests.get(website4)
  except ConnectionError:
    print()
    print(
      colored("The moveset you entered does not exist in this generation",
              "red"))
    exit()
  else:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Searching for Pokemon...")
    results = soup.find(id="content")
    p = soup.find_all('p')
    listofhtml4 = []
    for x in p:
      listofhtml4.append(str(x))
    htmlstring4=''.join(listofhtml4)
    for n in range(0, 1010, 1):
      if bulb[n] in htmlstring4:
        list4.append(bulb[n])
  print()
  print()
  print()
for z in range(0, len(list1), 1):
  if move2 == "null" or list1[z] in list2:
    if move3 == "null" or list1[z] in list3:
      if move4 == "null" or list1[z] in list4:
        MASTERLIST.append(list1[z])
if len(MASTERLIST) == 0:
  print("Sorry, no Pokèmon were found with this moveset...")
else:
  print("Here are Pokèmon with the moveset you ordered:", MASTERLIST)
