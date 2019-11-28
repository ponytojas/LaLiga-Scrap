import get_managers
import get_teams_urls
import pandas as pd

if __name__ == "__main__":

    urls = get_teams_urls.getTeamsURL()
    get_managers.getManagerData(urls)

    data = pd.read_csv("teams.csv", sep= ';') 
    teams = data['Team'].toLisT()

    pass