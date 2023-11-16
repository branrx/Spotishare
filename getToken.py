import requests as req

import hashlib
import requests as req
import base64

name = "brandonlikescoffeeandcoffeetastesnicebrandonlikescoffee"
hashedName = hashlib.sha256(name.encode('utf8'))
hashInBase = base64.b64encode(hashedName.digest()).decode

authUrl = "https://accounts.spotify.com/api/token"

#   client
clientId = 'c632ab8cff854da09c7f1d9b2bb93b65'
redirectUri = 'http://localhost:8080/' 

#   code
code = 'AQDOaF7Y6vumJear194uPv8Z0FVJiDwRkds04LNzFQjfe45gX0CzKxLJ6TyXnNmgtpvnIicYBFslDkUdqF9qCDeiPKP4bivOdl_RMgGyOLUACN5TmrTgmQD4Um6354QbgHs3jWr9CpQuUt7RylTpQ3FAoNoDTOOxKmb3ToHTwSW7zybxM4Gg7REoDjui2tCkfQQMnpekdaaig29ZZUdGyyywM38QoZN924u1yqC-tOAuWNyW3mJPTcdLtRQyu9vPmZ6MN80DgmfJ9P1Fo_yQwu8Un7hpfwY'

#   request parameters
params = {
  'client_id': clientId,
  'grant_type': 'authorization_code',
  'code': code,
  'redirect_uri': redirectUri,
  'code_verifier': name
}

#   get request
a = req.post(url= authUrl, params= params, headers= {'Content-Type': 'application/x-www-form-urlencoded'})
print(a.url)
print(a.status_code)
