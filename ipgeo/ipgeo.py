"""Main module."""
from urllib.request import urlopen
import json


"""access the url and response the json for geo by giving ip"""
def APIrequest(ipaddr):
    urlIpGeo = 'http://ip-api.com/json/'
    if ipaddr.ip:
        """Temporary"""
        print(ipaddr.ip)
        urlIpGeo = 'http://ip-api.com/json/'
    try:
        resp = urlopen(urlIpGeo).read().decode('UTF-8')
        json_obj = json.loads(resp)
        return json_obj
    except Exception as e:
        print(e)
        return 1


# This is a new line that ends the file.
