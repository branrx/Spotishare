# Spotishare
Simple program that automates the process of adding tracks to a ==Spotify== playlist.

###  Motivation
There is this girl that I work with, we kind of like the same type of music. Mostly, songs that would'nt play on auxillary LOL. Problem is we cannot share playlists because we use different platforms to stream music. I have over 5000 songs on my computer and there is no way I could add them one by one to a Spotify playlist. Ergo I made this program so it can automatically compile all the files I have locally and add them to a spotify.

###  How it works
It uses tracks on the users local computer, grabs the attributes (artist name, title). Uses that information to search for the particular song on spotify. Then creates a playlist a playlist where all the tracks are added.

###  Technologies used
- [Spotify Web API](https://developer.spotify.com/documentation/web-api)

###  External Modules 
-  [music-tag](https://pypi.org/project/music-tag/)
-  [requests](https://pypi.org/project/requests/)

###  Work-Flow
*  Create a new playlist or use an existing one
    *  Provide name and description for the playlist
      > Do you want to create a new playlist y/n?:
      > 'Enter a name for your playlist: '
      > 'Enter a description for your playlist: '
*  Provide directory path where your audio files are located
*  It provides you with a link to sign in to your spotify.
    *  Open the link in your browser  
    *  Then grant access
    *  Then copy the url that's provided on the local host link
    *  Paste that url in console input
*   Program then compiles all your files, searches the tracks and adds them to the spotify playlist
*   Receipt file .txt contains all tracks that were added to the playlist, and the filename of the receipt file is the name of the playlist.
