import datetime
import requests
import json


def get_time_period():
    today = datetime.date.today()
    week = datetime.timedelta(days=7)
    time_period = today - week
    return time_period


def get_trending_repositories(top_size, time_period):
    api_url = 'https://api.github.com/search/repositories'
    params = {'q': 'created:>={0}'.format(time_period), 'sort': 'stars'}
    response = requests.get(api_url, params=params)
    repositories = json.loads(response.text)
    return repositories['items'][:top_size]


def get_repositories_info(repositories):
    repositories_info = []
    for repository in repositories:
        repositories_info.append(
                                 {
                                  'url': repository['html_url'],
                                  'stars': repository['stargazers_count'],
                                  'owner': repository['owner']['login'],
                                  'open_issues': repository['open_issues']
                                 }
                                )
    return repositories_info


def output_repositories_info_to_console(repositories_info):
    for item in repositories_info:
        print(item)


if __name__ == '__main__':
    time_period = get_time_period()
    top_size = 20
    repositories = get_trending_repositories(top_size, time_period)
    repositories_info = get_repositories_info(repositories)
    output_repositories_info_to_console(repositories_info)
