import get_managers
import get_teams_urls

if __name__ == "__main__":

    urls = get_teams_urls.getTeamsURL
    get_managers.getManagerData(urls)

    pass