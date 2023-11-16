import os
os.system('cls')

print('Spotishare v1.0 \nMade by Brandon Simoko')
print('This program is designed to create playlists on spotify using songs available locally on your computer.')

import spotishare
import song_scrapper
import parse_token
import easy_auth
import os

#   Create spotishare object
spotishareObj = spotishare.Spotishare()

#   Get playlist name
createPlaylist = input('\nDo you want to create a new playlist y/n?: ')

if(createPlaylist=='y'):
    playlistName = input('\nEnter a name for your playlist: ')
    description = input('\nEnter a description for your playlist: ')

    #   Create playlist
    print('\nCreating playlist...')
    spotishareObj.createPlaylist(playlistName, description)
else:
    playlistName = 'For you'

#   Get local directory containing the audio files to add to the playlist
path = input('\nEnter local music directory path ( Format: e.g S:\Music ): ')

#   Get code url, for authentication
#   Make token request
codeUrl = easy_auth.requestCode()
print(f'\nPlease open this Url: \n {codeUrl}')

#   User authentication
rawToken = input('\nPlease enter url acquired: ')
spotishareObj.token = parse_token.parseToken(rawToken = rawToken)

print('\nToken successfully acquired.')

#   Create receipt, named after the playlist, stores records of songs added to the playlist
receipt = open(f'{playlistName}.txt', 'a')

#   Compile all music files found in provided directory
print('\nCompiling music files.')
localFiles = song_scrapper.getFiles(path=path)

#   Search all songs on spotify, then add to playlist
spotishareObj.searchTracks(localFiles, receipt)

#   Close the receipt file
receipt.close()
