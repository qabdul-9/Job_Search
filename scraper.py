import requests
from bs4 import BeautifulSoup

def main():

    print('''
__        __   _                          _ 
\ \      / /__| | ___ ___  _ __ ___   ___| |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
  \ V  V /  __/ | (_| (_) | | | | | |  __/_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
        ''')

    url = "https://www.xula.edu/about/mission-values.html"
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers).text
    # response = requests.get(url)
    soup = BeautifulSoup(response, 'html.parser')

    # Extract all links
    for link in soup.find_all('a'):
        print(link.get('href'))
    print(soup.find('div', class_='editorarea').text)

    url = "https://catalog.louisiana.edu/content.php?catoid=21&navoid=7555"
    response = requests.get(url, headers=headers).text
    # response = requests.get(url)
    soup = BeautifulSoup(response, 'html.parser')

    # Extract all links
    for link in soup.find_all('a'):
        print(link.get('href'))
    print(soup.find_all('p'))

if __name__ == "__main__":
    main()

