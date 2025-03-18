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
time.sleep(1.5)
print(Fore.GREEN + "!If you have no response just leave a * symbol or blank!")
inurl = input('URL keyword: ')
intext = input('Text in webpage: ')
filetype = input('Filetype: ')
topLevelDomain = input('TLD: ')
related = input('related webpage: ')
if filetype == '*':
    filetype = "doc | pdf | xls | txt | ps | rtf | odt | sxw | psw | ppt | pps | xml"
x = ('inurl:' + inurl + ' intext:' + intext + ' filetype:' + filetype + ' site:*.' + topLevelDomain + ' related:' + related)


time.sleep(0.9)
print(Fore.BLUE + 'Processing request...')
time.sleep(1)
search_query=(x)
for i in search(search_query,
    tld='com',
    lang='en',
    num=100,
    stop=100,
    pause=2.0):
    print(i)
