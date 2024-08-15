import os

import requests

BASE_URL = 'https://hackattic.com'
HA_TOKEN = os.environ.get('HA_TOKEN')


def get_input(problem_set: str):
    url = f'{BASE_URL}/challenges/{problem_set}/problem?access_token={HA_TOKEN}'
    return requests.get(url).json()


def post_result(problem_set: str, payload: str):
    url = f'{BASE_URL}/challenges/{problem_set}/solve?playground=1&access_token={HA_TOKEN}'
    print()
    print(requests.post(url, json=payload).json())
