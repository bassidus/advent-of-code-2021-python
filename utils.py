from requests import get


def convert_string_list_to_int_list(lst):
    int_list = []
    for value in lst:
        int_list.append(int(value))
    return int_list


def fetch(url, return_type=str):
    with open('.cookie') as cookie:
        cookies = dict(session=cookie.read().strip())

    response = get(url, cookies=cookies)
    string_list = response.text.split()

    if return_type == int:
        return convert_string_list_to_int_list(string_list)

    return string_list
