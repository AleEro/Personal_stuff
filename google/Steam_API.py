import json
from steam.webapi import WebAPI

from time import ctime

CREDENTIALS_FILE = r'steam_key.json'
# to use this const you should register yours steam key

with open(CREDENTIALS_FILE, mode='r', encoding='utf-8') as file:
    file = file.read()
    s = json.loads(file)


def steam_get(link):
    mod_id = link.split('=')[1].split('&')[0]
    z = WebAPI(key=s['key']).ISteamRemoteStorage.GetPublishedFileDetails(itemcount=1, publishedfileids=[mod_id])
    return ctime(z['response']['publishedfiledetails'][0]['time_updated'])
