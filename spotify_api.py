import requests as req
import json
import parse_token

def getAll(trackObj):
    results = trackObj['tracks']['items']
    for result in results:
        print(result['name'])
        print(result['artists'][0]['name']) 
        print(result['uri']) 
        print('-----------------------------------------------------------------------')  

def getOne(trackObj):
    return trackObj['tracks']['items'][0]['name'] + " - " + trackObj['tracks']['items'][0]['artists'][0]['name']

#   client
clientId = 'c632ab8cff854da09c7f1d9b2bb93b65'
redirectUri = 'http://localhost:8080/' 
url = 'https://accounts.spotify.com/authorize'

rawToken = 'http://localhost:8080/#access_token=BQCyuuffrg0oP6RNU33ZZ8yLiGJhQ5Wv8bhRtptmvq-887yGddMPoi9Yiq3Fp7b4jH72F7sDc6rIOqJDfjAuGlKKEWioPHgl4fu1_qL_ygYpFL9XmdVcA0-MFmLGW20NXE4tlO9M0pqT6yRYfo_Uvx20R5u-GLrSVpTdKPIZ9otk6TsnEnMBajMj1QiSnPKEOZqPUrr7k09FmhpMWmJIXqQTg4vA59ZsDl2bjRiwaHGwAfrnLSkzkf5KFGafrSBi6Z6LJP8&token_type=Bearer&expires_in=3600&state=%3Cbuilt-in+method+decode+of+bytes+object+at+0x000002BF289E2830%3E'
token = parse_token.parseToken(rawToken = rawToken)

query = "Anson+Seabra+Walked+Through+Hell"
searchType = 'track'


#   prepare url
userid = 'q77ndqadt94zsvl8g0mcl2k96'
authUrl = 'https://api.spotify.com/v1/search'
#authUrlPlaylist = 'https://api.spotify.com/v1/users/q77ndqadt94zsvl8g0mcl2k96/playlists'
scope = 'playlist-read-private playlist-modify-private'

headers = {
    'Authorization': 'Bearer ' + token,
}

params = {
    'q': query,
    'type': searchType,
    'market': 'US',
    'limit': '5',
    'offset': '0'
}

#   get request
a = req.get(url= authUrl, params=params, headers=headers)
print(a.status_code)
trackObj = a.json()

print(getAll(trackObj))
 



