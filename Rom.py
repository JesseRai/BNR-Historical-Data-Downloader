import requests
import argparse

def get_idbs_csv(cid, filename):
    headers = {
        'Referer': 'https://www.bnr.ro/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'cid': cid,
        'period': 'all',
        'dfrom': '',
        'dto': '',
        'format': 'CSV',
    }

    url = 'https://www.bnr.ro/idbsfiles'
    response = requests.get(url, headers=headers, params=params, verify=False)

    if response.status_code == 200:
        with open(f'{filename}.csv', 'wb') as f:
            f.write(response.content)
        print(f'Downloaded {filename}.csv')
    else:
        print(f'Failed to download file. Status code: {response.status_code}')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('cid', type=str)
    parser.add_argument('filename', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    get_idbs_csv(args.cid, args.filename)
