from googlesearch import search
import time
import colorama
from colorama import Fore

print("""
   _,  
  / |                  __        
 / ___,  ____ ___     /' |
 /'   `\,--,/'   `\  /'   |
(       )  (       )'
 \_   _/'  `\_   _/         
                                          
      ~Dorket~
    """)

time.sleep(1)

print(Fore.GREEN + 'Made by BojamaV')

time.sleep(2)

dork = input(Fore.RED + 'Enter your google dork: ')
keyword = input(Fore.RED + 'Enter URL keywords: ')
glob = input(Fore.RED + 'enter the link domain (com/gov/net): ')

time.sleep(0.9)

print(Fore.BLUE + 'Processing request...')

time.sleep(1)

search_query=("intext" + dork + "inurl" + keyword + "site:*." + glob)
for i in search(search_query,
    tld=glob,
    lang='en',
    num=10000,
    stop=10000,
    pause=2.0):
    print(i)
