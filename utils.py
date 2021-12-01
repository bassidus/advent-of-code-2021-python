from requests import get


def fetch(url, return_type):
    result = []

    with open('.cookie') as cookie:
        cookies = dict(session=cookie.read().strip())

    response = get(url, cookies=cookies)
    response = response.text.split()

    if return_type == int:
        for value in response:
            result.append(int(value))
        return result

    return response