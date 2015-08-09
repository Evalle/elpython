class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "Happy bday to you"])

smells_like_teen_spirit = Song(["Load up on guns and bring your friends",
                                "It's fun to lose and to pretend"])

happy_bday.sing_me_a_song()

smells_like_teen_spirit.sing_me_a_song()

