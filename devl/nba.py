import re
import pandas as pd
htmlbase = "http://www.basketball-reference.com/leagues/NBA_2016_games-$month.html"
months = ['october',
        'november',
        'december',
        'january',
        'february',
        'march',
        'april',
        'may',
        'june']
games = []
for month in months:
    html = re.sub('\$month',month,htmlbase)
    print html
    tables = pd.read_html(html)
    games.append(tables[0])
# games.to_csv(fp)
# else:
# games = pd.read_csv(fp)
# games.head()
Unnamed: 'a1', 'date', 'start', u'Visitor/Neutral'
, u'PTS',
       u'Home/Neutral', u'PTS.1', u'abc', u' .1', u'Attend.', u'
Notes'],


ames = {'Date': 'date', 'Start (ET)': 'start',
                'Unamed: 2': 'box', 'Visitor/Neutral': 'away_team', 
                'PTS': 'away_points', 'Home/Neutral': 'home_team',
                'PTS.1': 'home_points', 'Unamed: 7': 'n_ot'}
