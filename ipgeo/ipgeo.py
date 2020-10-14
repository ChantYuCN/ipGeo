"""Main module."""
from urllib.request import urlopen
import json
"""access the url and response the json for geo by giving ip, and out to a text file"""


def ipGeoUrl(ipaddr):
    urlIpGeo = 'http://ip-api.com/json/'
    if ipaddr.ip:
        """Temporary"""
        print(ipaddr.ip)
        urlIpGeo = 'http://ip-api.com/json/'
    try:
        resp = urlopen(urlIpGeo).read().decode('UTF-8')
        json_obj = json.loads(resp)
    except Exception as e:
        print(e)
        return 1
    json_doc = json.dumps(json_obj)
    filename = 'location.json'
    with open(filename, 'w') as f:
        f.write(json_doc)
        f.close()


# This is a new line that ends the file.
