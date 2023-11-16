def parseToken(rawToken: str) -> str:
    
    token = rawToken.split('&')[0].split('=')

    return token[1]
