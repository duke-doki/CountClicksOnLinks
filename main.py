import os
from urllib.parse import urlparse

import requests
import argparse
from dotenv import load_dotenv


def shorten_link(token, long_url):
    headers = {'Authorization': f'Bearer {token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(
        url, 
        headers=headers, 
        json={"long_url": long_url}
    )
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(token, bitlink):
    bitlink = urlparse(bitlink)
    headers = {'Authorization': f'Bearer {token}'}
    link = ("https://api-ssl.bitly.com/v4/"
            "bitlinks/{}{}/clicks/summary").format(
                bitlink.netloc, 
                bitlink.path
            )
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    clicks = response.json()['total_clicks']
    return clicks


def is_bitlink(token, url_to_check):
    url_to_check = urlparse(url_to_check)
    headers = {'Authorization': f'Bearer {token}'}
    link = ("https://api-ssl.bitly.com/"
        "v4/bitlinks/{}{}").format(url_to_check.netloc, url_to_check.path)
    response = requests.get(link, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Enter a link')
    args = parser.parse_args()
    link_to_check = args.link
    try:
        if is_bitlink(bitly_token, link_to_check):
            print('Количество кликов: ', count_clicks(bitly_token, link_to_check))
        else:
            print('Битлинк: ', shorten_link(bitly_token, link_to_check))
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')


if __name__ == '__main__':
    main()
