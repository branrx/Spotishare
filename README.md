# Spotishare
Simple program that automates the process of adding tracks to a ==Spotify== playlist.

###  Motivation
There is this girl that I work with, we kind of like the same type of music and I like her maybe. Mostly, songs that you would'nt play on auxillary lol. Problem is we cannot share playlists because we use different platforms to stream music. I have over 5000 songs on my computer and there is no way I could add them one by one to a Spotify playlist. Ergo I made this program so it can automatically compile all the files I have locally and add them to a spotify playlist. This way we can collaborate on each other's playlists and fall in love, maybe, I hope so though lol.

###  How it works
It uses tracks on the users local computer, grabs the attributes (artist name, title). Uses that information to search for the particular song on spotify. Then creates a playlist where all the tracks are added.

###  Technologies used
- [Spotify Web API](https://developer.spotify.com/documentation/web-api)

###  External Modules 
-  [music-tag](https://pypi.org/project/music-tag/)
-  [requests](https://pypi.org/project/requests/)

###  Work-Flow
*  Create a new playlist or use an existing one
    *  Provide name and description for the playlist
```      
Do you want to create a new playlist y/n?:
```
```
Enter a name for your playlist:
```
```
Enter a description for your playlist:
```
*  Provide directory path where your audio files are located
```
Enter local music directory path ( Format: e.g S:\Music ): 
```
*  It provides you with a link to sign in to your spotify.
    *  Open the link in your browser
     ```
     Please open this Url: url
     ```
    *  Then grant access
    *  Then copy the url that's provided on the local host link
    *  Paste that url in console input
    ```
    Please enter url acquired: 
    ```
*   Program then compiles all your files, searches the tracks and adds them to the spotify playlist
*   Receipt file .txt contains all tracks that were added to the playlist, and the filename of the receipt file is the name of the playlist.

###   DEV NOTE
Took 3 days to finish, because spotify doesn't offer support for python but rather Rest API, ergo their tutorials are tailored for someone in web developement **JavaScript**. I got a lot of bad requests while trying to authenticate mainly because parameters are parsed differently when using **JavaScript** compared to **Python's** requests library. Also the API's documentation is ambiguous when providing an endpoint, sometimes it does not provide which endpoint to use, it just states endpoint = url, And I'm like which url?, because the url variable is not decalred anywhere.
