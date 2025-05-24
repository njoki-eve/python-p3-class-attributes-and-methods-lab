class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update total count
        Song.count += 1
        
        # Update genres list and count
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        
        # Update artists list and count
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1