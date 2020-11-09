
# coding: utf-8

# In[ ]:


import requests
import json
from IPython.display import Image
from IPython.display import Audio

class Song():
    def __init__(self, artist_name, track_name, artwork, snippet):
        self.artist_name = artist_name
        self.track_name = track_name
        self.artwork = artwork
        self.snippet = snippet
    def display_cover_art(self):
        display(Image(self.artwork))
    def __str__(self):
        return "'{}' by {}".format(self.track_name, self.artist_name)
    def display_snippet(self):
        display(Audio(self.snippet))
    def get_title(self):
        return self.track_name
    
        
class Artist():
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_song_index = -1
    def get_songs(self):
        r = requests.get("https://itunes.apple.com/search", params={'term': self.name, 'attribute': 'artistTerm', 'limit': 25, 'entity': 'song'})
        songs_json = json.loads(r.text)
        for song_json in songs_json["results"]:
            song = Song(song_json["artistName"], song_json["trackName"], song_json["artworkUrl100"], song_json["previewUrl"])
            self.songs.append(song)
        # make a request to the itunes api
        # store all of the songs in the itunes api in self.songs
    def get_next_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.songs):
            print("No more songs")
            return None
        return self.songs[self.current_song_index]
    def has_more_songs(self):
        return self.current_song_index + 1 < len(self.songs)
    def __str__(self):
        return self.name

    
exited = False
playlist = []
with open('playlist_file.json', 'r') as f:
    playlist_raw = json.load(f)
    for song in playlist_raw:
        playlist.append(Song(
            song['artist_name'],
            song['track_name'],
            song['artwork'],
            song['snippet']
        ))
while not exited:
    start = """Main Menu
        - Type 'exit' to leave
        - Type 'playlist' to see your playlist so far
        - Otherwise, enter an artist name"""
    print(start)
    print('')
    
    user_input = input("Enter an artist (or exit/playlist): ")
    if user_input == 'exit':
        with open('playlist_file.json', 'w') as f:
            json_out = []
            for song in playlist:
                json_out.append({
                    'artist_name': song.artist_name,
                    'track_name': song.track_name,
                    'artwork': song.artwork,
                    'snippet': song.snippet
                })
            json.dump(json_out, f, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        exited = True
        continue
    elif user_input == 'playlist':
        print('')
        print("=== Playlist ===")
        print('')
        print('')
        for each_song in playlist:
            each_song.display_cover_art()
            each_song.display_snippet()
            print(each_song)
            print('')
            
    else:
        artist = Artist(user_input)
        print("You entered: " + str(artist))
        artist.get_songs()

        while artist.has_more_songs():
            song = artist.get_next_song()
            song.display_cover_art()
            song.display_snippet()
            print(song)
            #print the cover art and a snippet of the song by that given artist
            yes_no_back = input("Add to a playlist? (yes/no/back): ")
            if yes_no_back == "yes":
                print('yes')
                playlist.append(song)
                #add song to the playlist
                #bring up new song by that author
            elif yes_no_back == "no":
                continue
                #bring up new song by that author
            elif yes_no_back == "back":
                break
            else:
                print('Error')


