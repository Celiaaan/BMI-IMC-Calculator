WEBHOOK_URL = "https://discord.com/api/webhooks/845407314998460467/C5M3AO9GCN44MERIOBw59Z0yFcUcLWutrmhSIFggKityweQzUoab3ZzcOrGfzpDYVKRq"

import json
from urllib import request
from urllib.error import HTTPError

payload = {
        'content' : '@everyone'+'https://www.youtube.com/watch?v=0wTVRPUJyv0'
    }


if True:
    # Les paramètres d'en-tête de la requête
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL,
                          data=json.dumps(payload).encode('utf-8'),
                          headers=headers,
                          method='POST')


def SPAM():
    try:
        response = request.urlopen(req)
        print(response.status)
        print(response.reason)
        print(response.headers)
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e.file.read())

from functools import cache, lru_cache


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(4000):
        print(i, fib(i))
    print("done")


if __name__ == '__main__':
    main()