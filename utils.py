from requests import get


def fetch_ints(url):
    cookie = '.cookie'

    with open('.cookie') as cookie:
        cookies = dict(session=cookie.read().strip())

    response = get(url, cookies=cookies)
    str_lst = response.text.split()
    int_lst = []
    for s in str_lst:
        int_lst.append(int(s))

    return int_lst
