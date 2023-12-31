import hashlib
import requests as req
import base64

name = ""
hashedName = hashlib.sha256(name.encode('utf8'))
hashInBase = base64.b64encode(hashedName.digest()).decode

#   client
clientId = ''
redirectUri = 'http://localhost:8080/' 

#   prepare url
authUrl = 'https://accounts.spotify.com/authorize'
scope = 'playlist-read-private'

#   request parameters
params = {'response_type': 'code',
  'client_id': clientId,
  'scope': scope,
  'code_challenge_method': 'S256',
  'code_challenge': hashInBase,
  'redirect_uri': redirectUri
}

#   get request
a = req.get(url= authUrl, params= params)
print(a.url)
