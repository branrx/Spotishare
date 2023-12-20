#   GRABS SONGS IN LOCAL STORAGE
#   CREATES PLAYLIST ON SPOTIFY
#   ADDS THE SONG TO SPOTIFY PLAYLIST

import requests as r
import json
import time

class Spotishare:
    def __init__(self) -> None:
        #   User ID
        userId = ''

        #   Files path
        self.path = ''

        #   API variables
        self.playlistEndpoint = f'https://api.spotify.com/v1/me/playlists'

        #   Playlist id
        self.playlistId = ''

        #   Token string
        self.token = ''
        
    #   Creates playlist in spotify
    def createPlaylist(self, name, description: str):
        endpoint  = 'https://api.spotify.com/v1/me/playlists'
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json',
        }
        
        data = {
            'name': name,
            'description': description,
            'public': False,
            'collaborative': False,
        }

        #   Make create request
        post = r.post(url=self.playlistEndpoint, data=json.dumps(data), headers=headers)

        if(post.status_code==201):
            print('Playlist created.')

            #   Save playlist name and id to file
            f = open("playlists.txt", "+a")
            f.write("\n")
            f.write(f'{name}:{post.json()['id']}')
            f.close()

            print(f'playlist id: {post.json()['id']}')
            self.playlistId = post.json()['id']
        else:
            print(f'Failed to create playlist. {post.text}')
    
    #   Takes a track id then adds to playlist of choice
    def addToPlaylist(self, trackIDs: list, playlistId: str) -> None:
        endpoint  = f'https://api.spotify.com/v1/playlists/{self.playlistId}/tracks'

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json',
        }

        data = {
            'uris': trackIDs
        }

        #   Add track to playlist
        post = r.post(url = endpoint, data = json.dumps(data), headers = headers)

        if(post.status_code==201):
            print('Tracks added.')
        else:
            print(f'Failed to add tracks. {post.text}')
            print(post.status_code)

    #   Parse track object results from a spotify response
    def getAll(self, response) -> str:
        try:
            results = response['tracks']['items']
        except Exception as e:
            print(e)
            return ''

        for result in results:
            print(result['name'])
            print(result['artists'][0]['name']) 
            print(result['uri']) 

        try:    
            return result['uri']
        except Exception as e:
            print(e)
            return ''

    def searchTracks(self, fileDict, receipt):
        print('Searching for tracks...')
        endpoint = 'https://api.spotify.com/v1/search'
        
        #   Strore track ids if found on spotify
        trackIDs = list()

        headers = {
            'Authorization': 'Bearer ' + self.token,
            }

        #   Item counter
        count = 1

        for item in fileDict:
            params = {
                'q': item,
                'type': 'track',
                'market': 'US',
                'limit': '1',
                'offset': '0'
            }

            response = r.get(url = endpoint, params=params, headers=headers)
            print(f'\n{count}/{len(fileDict)}.')

            trackid = self.getAll(response.json())
            
            if(trackid!=''):
                print(f'-- FOUND --')
                receipt.write(fileDict[item])
                receipt.write('\n')
                trackIDs.append(trackid)
            else:
                print(f'-- NOT FOUND --\n')
            count+=1

            time.sleep(1)
        
        self.addToPlaylist(trackIDs=trackIDs, playlistId=self.playlistId)
