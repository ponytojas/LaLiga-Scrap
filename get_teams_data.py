import get_managers
import get_teams_urls
import get_players_data
import pandas as pd
import os

if __name__ == "__main__":

    urls = get_teams_urls.getTeamsURL()
    get_managers.getManagerData(urls)

    if not os.path.exists('./data/'):
        os.makedirs('./data')

    data = pd.read_csv("./data/teams.csv", sep= ';') 
    teams = data['Team']
    teams = teams.tolist()
    get_players_data.getPlayersData(urls, teams)

    pass