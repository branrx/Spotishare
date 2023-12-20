import requests as req
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
clientId = ''
redirectUri = 'http://localhost:8080/' 
url = 'https://accounts.spotify.com/authorize'

rawToken = ''
token = parse_token.parseToken(rawToken = rawToken)

query = "Anson+Seabra+Walked+Through+Hell"
searchType = 'track'


#   prepare url
userid = ''
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
 



