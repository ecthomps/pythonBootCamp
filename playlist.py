playlist = {
            "title": "new age instrumental", 
            "author": "chris young", 
            "songs": [
                {"title": "intro", "artist": ["flex"], "album": "beginning", "duration": 2.5},
                {"title": "intro_remix", "artist": ["flex", "rock"], "album": "beginning", "duration": 4.5},
                {"title": "another_one", "artist": ["life"], "album": "levels", "duration": 3.25}
            ]
        }

#print song titles
for song in playlist['songs']:
    print(song['title'])

#print the total duration of the songs
total_dur = 0
for song in playlist['songs']:
    total_dur += song['duration']
print(total_dur)