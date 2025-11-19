import requests as rq
import json
from urllib.parse import quote , quote_plus


def get_location(address:str):

    link = "https://nominatim.openstreetmap.org/search?format=json&q={}"


    request_headers = {


    "Host": "nominatim.openstreetmap.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "TE": "trailers"

    }


    loc = rq.get(url=link.format(quote(address)),headers=request_headers)

    if loc.status_code != 200:
        return "Error"
    
    else:
         data = json.loads(loc.content.decode("utf-8"))
         if data == []:
             return "Not Found"
         
         else:
             return data

    

