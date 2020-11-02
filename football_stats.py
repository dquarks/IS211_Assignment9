import re
import requests as req
from bs4 import BeautifulSoup as bs

def sanitize(text,repl):
    return re.sub(r'\s+', repl, str(text))

webpage = req.get('https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/')
content = webpage.content
soup = bs(content,'html.parser')
player_data = soup.find_all('span', class_='CellPlayerName--long')
player_stats = soup.find_all('td', class_='TableBase-bodyTd--number')

x = 11 #    First player's touch-down score starts at index 11.
for i in range(20):
    player_info = player_data[i].text
    total_td    = player_stats[x].text

    clean_total_td          = sanitize(total_td, '')
    clean_player            = sanitize(player_info, ' ')
    structure_player_info   = (re.sub(r'\s+', ',', clean_player.strip())).split(',')
    try:
        print('Player: %s | Position: %s | Team: %s | Total Touchdowns: %s'
                % ((structure_player_info[0] + ' ' + structure_player_info[1]),
                    structure_player_info[2], structure_player_info[3], clean_total_td))
    except IndexError: #    Likely the result of a player with missing team or position. Not the best solution.
        print('Player: %s | Position: %s | Team: %s | Total Touchdowns: %s'
                % ((structure_player_info[0] + ' ' + structure_player_info[1]),
                    'None', 'None', clean_total_td))
    x = x + 13
