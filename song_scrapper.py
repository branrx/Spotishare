import os
import music_tag as meta

#   Traverses the system directory
#   Grabs all files, grabs contained metadata
#   Formats the artist and title string to url standard
def getFiles(path: str) -> dict:
    path = formatPath(path)
    files = os.listdir(path)
    
    tempDict = dict()

    for file in files:
        songData = meta.load_file(f'{path}//{file}')

        #   Save original attribute values before parsing
        titleOG = str(songData['title'])
        artistOG = str(songData['artist'])

        if len(artistOG)==0:
            continue

        if len(titleOG)==0:
            continue

        title = str(songData['title'])
        #   Format the artist string to url standard
        artist = str(songData['artist']).replace(' ', '+')
        
        if str(songData['title']).find('(')>-1:
            #   Split the title from other artists string
            title = str(songData['title']).split('(')[0]

        #   Format the title string to url standard
        title = title.replace(' ', '+')

        #   Remove ending +
        title = title.rstrip('+')

        #   Format the artist string to url standard
        artist = str(songData['artist']).replace(' ', '+')

        #   Add items to the dictionary
        tempDict[f'{artist}+{title}'] = f'{artistOG} - {titleOG}'

    return tempDict

def formatPath(path: str) -> str:
    return path.replace('\\', '//')
