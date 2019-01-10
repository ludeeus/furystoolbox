"""Common."""


def share(data):
    """Share"""
    import requests
    base = 'https://bin.halfdecent.io/'
    url = "{}documents".format(base)
    post = requests.post(url, data=data).json()
    print("{}{}".format(base, post['key']))
