#!/usr/bin/env python

# https://www.mozilla.org/en-US/MPL/2.0/

# https://github.com/jsommers/pytricia
# pip install pytricia

import pytricia

WHITELIST = [
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

WL = pytricia.PyTricia()
for i in WHITELIST:
    WL[i] = True


def is_whitelisted(ip):
    if ip in WL:
        return True

# EXAMPLES
# python3 filter.py 192.168.1.0/24
# python3 filter.py 192.168.1.1
# python3 filter.py 1.1.1.1


def main():
    import sys

    ip = sys.argv[1]

    if is_whitelisted(ip):
        print("Whitelisted!")

    else:
        print("Not Whitelisted!")


if __name__ == '__main__':
    main()
