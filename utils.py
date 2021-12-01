from requests import get


def fetch_ints(url):
    result = []

    with open('.cookie') as cookie:
        cookies = dict(session=cookie.read().strip())

    response = get(url, cookies=cookies)
    response = response.text.split()
    for value in response:
        result.append(int(value))

    return result
