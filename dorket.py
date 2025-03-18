from googlesearch import search
import time
from colorama import Fore
import itertools

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
time.sleep(1.5)

print(Fore.GREEN + "!If you have no response just leave a * symbol or blank!")
inurl = input('URL keyword: ')
intext = input('Text in webpage: ')
filetype = input('Filetype: ')
topLevelDomain = input('TLD: ')
related = input('Related webpage: ')

if filetype == '*':
    filetype = "doc | pdf | xls | txt | ps | rtf | odt | sxw | psw | ppt | pps | xml"

search_query = f'inurl:{inurl} intext:{intext} filetype:{filetype} site:*.{topLevelDomain} related:{related}'

time.sleep(0.9)
print(Fore.BLUE + 'Processing request...')
time.sleep(1)

# Manually limit results using itertools.islice
try:
    for i in itertools.islice(search(search_query, lang='en', pause=2.0), 50):
        print(i)
except Exception as e:
    print(Fore.RED + f"Error: {e}")
