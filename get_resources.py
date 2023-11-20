import txt_to_list as ttl 
import time

def getPlaylists() -> dict:
    f = open("playlists.txt", "r")

    playlists = ttl.to_list_single(f)

    return listToDict(playlists)

def listToDict(tempList) -> dict:
    temp = dict()

    for item in tempList:
        splitItem = item.split(":")
        temp[splitItem[0]] = splitItem[1]

    return temp

def playlistMenu() -> str:
    playlists = getPlaylists()
    options = dict()
    index = 0

    if(len(playlists)==0):
        return 'new'

    print("\nSelect a playlist.")
    for item in playlists:
        print(f'{index}. {item}')
        options[index] = item
        index+=1

    print(f'{index}. Create new playlist')

    while True:
        selection = input()
        if int(selection)>=0 and int(selection)<=len(playlists):
            break
        else:
            print(f'Option should be 0 to {len(playlists)+1}')

    return getPlaylistOption(playlists, options, selection)

def getPlaylistOption(playlists, options, selection) -> str:
    new = len(playlists)
    
    if int(new)==int(selection):
        #   Returns command to create new playlist
        return 'new:new'
    else:
        #   Uses the index to get key from playlist ergo returning the playlist id
        print(f"\nActive playlist: {options[int(selection)]}")
        return f'{options[int(selection)]}:{playlists[options[int(selection)]]}'
    
def verifyToken() -> str:
    f = open('token.txt', 'r')
    tokenTime = ttl.to_list_single(f)

    if len(tokenTime)==0:
        return 'expired'

    tokenTime = listToDict(tokenTime)

    #   10 mins threshold, so limit is at least less than 50 mins old
    #   Else token is considered expired
    tokenTimeMins = float(tokenTime['time'])/60
    currentTime = time.time()/60

    if (currentTime-tokenTimeMins)>50:
        print("Token expired")
        return 'expired'
    
    print(f'Token time till expiration: {40 - int(currentTime-tokenTimeMins)} minutes.')
    return tokenTime['token']

def saveToken(token):
    currentTime = time.time()

    f = open('token.txt', 'w')
    f.write(f'time:{currentTime}')
    f.write(f'\n')
    f.write(f'token:{token}')
    f.close()