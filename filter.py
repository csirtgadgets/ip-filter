
# pip install pytricia

import pytricia

PERM_WHITELIST = [
    "0.0.0.0/8",
    "10.0.0.0/8",
    "127.0.0.0/8",
    "192.168.0.0/16",
    "169.254.0.0/16",
    "192.0.2.0/24",
    "224.0.0.0/4",
    "240.0.0.0/5",
    "248.0.0.0/5",
]

# https://github.com/jsommers/pytricia
def process(data=[], whitelist=[]):
    wl = pytricia.PyTricia()

    whitelist += PERM_WHITELIST
    [wl[i] = True for i in whitelist]

    for i in data:
        if i not in wl:
            yield i
