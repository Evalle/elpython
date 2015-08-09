class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday_lyrics = ["Happy birthday to you",
                     "Happy birthday to you"]

slts_lyrics = ["Load up on guns and bring your friends",
               "It's fun to lose and to pretend"]

happy_bday = Song(happy_bday_lyrics)

smells_like_teen_spirit = Song(slts_lyrics)

happy_bday.sing_me_a_song()

smells_like_teen_spirit.sing_me_a_song()

