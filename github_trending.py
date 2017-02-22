import datetime
import requests
import json


API_URL = 'https://api.github.com/search/repositories'
TOP_SIZE = 20


def get_last_week_date():
    today = datetime.date.today()
    week = datetime.timedelta(days=7)
    last_week_date = today - week
    return last_week_date


def get_trending_repositories(top_size, last_week_date, api_url):
    params = {'q': 'created:>={0}'.format(last_week_date), 'sort': 'stars'}
    response = requests.get(api_url, params=params)
    repositories = json.loads(response.text)
    return repositories['items'][:top_size]


def get_repositories_info(repositories):
    pattern = ['html_url', 'stargazers_count', 'open_issues']
    repositories_info = [
                         {x: repo[x] for x in repo if x in pattern}
                         for repo in repositories
                         ]
    return repositories_info


def output_repositories_info_to_console(repositories_info):
    for repo in repositories_info:
        print('URL: {0}'.format(repo.get('html_url')))
        print('\t''Stars: {0}'.format(repo.get('stargazers_count')))
        print('\t''Open issues: {0}'.format(repo.get('open_issues')))


if __name__ == '__main__':
    last_week_date = get_last_week_date()
    repositories = get_trending_repositories(TOP_SIZE, last_week_date, API_URL)
    repositories_info = get_repositories_info(repositories)
    output_repositories_info_to_console(repositories_info)
