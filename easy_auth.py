import requests as r
import hashlib
import base64

def requestCode() -> str:

  name = "brandonlikescoffeeandcoffeetastesnicebrandonlikescoffee"
  hashedName = hashlib.sha256(name.encode('utf8'))
  hashInBase = base64.b64encode(hashedName.digest()).decode

  #   client
  clientId = 'c632ab8cff854da09c7f1d9b2bb93b65'
  redirectUri = 'http://localhost:8080/' 
  url = 'https://accounts.spotify.com/authorize'

  scope = 'playlist-read-private playlist-modify-private playlist-modify-public'

  #   request parameters
  params = {'response_type': 'token',
    'client_id': clientId,
    'scope': scope,
    'redirect_uri': redirectUri,
    'state': hashInBase
  }

  # Get access code
  codeUrl = r.get(url=url, params=params)
  
  return codeUrl.url