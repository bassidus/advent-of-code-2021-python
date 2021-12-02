from requests import get


def fetch(url):
    with open('.cookie') as cookie:
        cookies = dict(session=cookie.read().strip())

    response = get(url, cookies=cookies)
    string_list = response.text.split()

    return string_list
