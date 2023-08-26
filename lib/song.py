class Song:
    count  = 0
    genres = []
    # unique_genre= {}
    artists = []
    genre_count = {}
    artist_count= {}
    

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        self.add_to_genre_count()
        self.add_to_artist_count()
        

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}  # Reset the genre count dictionary

        for item in cls.genres:
            if item in cls.genre_count:
                cls.genre_count[item] += 1
            else:
                cls.genre_count[item] = 1

        return cls.genre_count

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}  # Reset the genre count dictionary

        for item in cls.artists:
            if item in cls.artist_count:
                cls.artist_count[item] += 1
            else:
                cls.artist_count[item] = 1

        return cls.artist_count

    
# print(add_to_genre_count())

    # @classmethod
    # def add_to_genres(cls, genre):

    #     cls.unique_genre.append(genre)
          