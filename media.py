class Movie():
    """This class is used for creating Movie objects containing information 
    regarding title, posterURL and trailerURL.

        Attributes:
            movie_title: A string containing the Movie's title.
            poster_image_url: A string containing the URL to the Movie's poster.
            trailer_youtube_url: A string containing the URL to the Movie's 
                                 trailer.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie with movie_title, movie_poster, movie_trailer"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

