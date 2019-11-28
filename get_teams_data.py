import get_managers
import get_teams_urls
import get_players_data
import pandas as pd

if __name__ == "__main__":

    urls = get_teams_urls.getTeamsURL()
    #get_managers.getManagerData(urls)

    data = pd.read_csv("teams.csv", sep= ';') 
    teams = data['Team']
    teams = teams.tolist()
    get_players_data.getPlayersData(urls, teams)

    pass