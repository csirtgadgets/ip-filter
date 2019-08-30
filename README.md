# ip-filter
The FASTEST way to filter ip addresses

```bash
$ pip install pytricia

$ python3 filter.py 192.168.1.1
Whitelisted!

$ python3 filter.py 1.1.1.1
Not Whitelisted!

$ python3 filter.py 192.168.1.0/24
Whitelisted!

```