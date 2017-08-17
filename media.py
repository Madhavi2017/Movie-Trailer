import webbrowser
# importing webbrower


# class to store our favourite movies
class Movie():
    # defining function to intiliase memory for the following intsnaces
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # self=instance is created
        self.title = movie_title
        self.story = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # defining function to play trailer
    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
