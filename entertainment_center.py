#importing modules garbage collector (gc), media and fresh_tomatoes. Make sure those files are in the same folder as this file.
import media
import fresh_tomatoes
import gc

#Defining movies that need to show up on the webpage.
movie1 = media.Movie("The Shawshank Redemption", "https://static.rogerebert.com/uploads/movie/movie_poster/the-shawshank-redemption-1994/large_9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
movie2 = media.Movie("Pulp Fiction", "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
movie3 = media.Movie("The Dark Knight", "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
movie4 = media.Movie("Fight Club", "https://vignette.wikia.nocookie.net/fightclub/images/6/6a/Fight-club-dvd.jpg/revision/latest?cb=20081116042426", "https://www.youtube.com/watch?v=SUXWAEX2jlg")
movie5 = media.Movie("Inception", "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", "https://www.youtube.com/watch?v=8hP9D6kZseM")
movie6 = media.Movie("The Matrix", "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle", "https://www.youtube.com/watch?v=m8e-FF8MsqU")

#Generate a list of the created Movie objects
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

#Call a function that will take in the list of movies and generate an HTML file including this content
fresh_tomatoes.open_movies_page(movies)


