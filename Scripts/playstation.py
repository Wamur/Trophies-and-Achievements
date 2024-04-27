import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://www.truetrophies.com/gamelist?page="

all_games = []

for page_num in range(1, 111):
    url = base_url + str(page_num)
    
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    
    for row in soup.find_all('tr')[1:]:
        game = {}
        cells = row.find_all('td')
        game['name'] = cells[1].text.strip()
        game['score'] = cells[2].text.strip()
        game['ratio'] = cells[3].text.strip()
        game['gamers'] = cells[4].text.strip()
        game['completion_percentage'] = cells[5].text.strip()
        game['completion_time'] = cells[6].text.strip()
        game['rating'] = cells[7].text.strip()
        all_games.append(game)

df = pd.DataFrame(all_games)
df.to_csv('playstation.csv', index=False)
