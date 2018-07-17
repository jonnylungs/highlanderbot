from bs4 import BeautifulSoup
import requests

#clean up javascript
def javaclean(string):
    copy = ''
    for x in range(len(string)):
        if string[x] != '\\':
            copy += string[x]
    return copy

source = requests.get('https://www.herricks.org/').text
soup = BeautifulSoup(source, 'lxml')

slideshow = soup.find('div', class_ = 'ui-widget app gallery json')

text = slideshow.find('script').text

text = text.split('{"photoname":')
text.pop(0)

headlines = list(map(lambda x: (x.split(',')[0])[1:-1], text))

text = slideshow.find('script').text

text = slideshow.find('script').text
text = text.split('"caption":')
text.pop(0)

par = list(map(lambda x: (x.split('"pause":"","link":"/'))[:-1], text))

for x in range(len(par)):
    string = ''
    for y in range(len(headlines[x])):
        string += '_'
    print(string)
    print(headlines[x])
    print(string)
    print()
    print(javaclean(str(par[x][0][1:-2])))
    print()

