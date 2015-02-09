import media
import fresh_tomatoes

sssssss = media.Movie("Sssssss",
                      "David, a college student, is looking for a job. He is hired by Dr. Stoner as a lab assistant for his research and experiments on snakes",
                      "http://ia.media-imdb.com/images/M/MV5BMTMxNzc3NDY5OV5BMl5BanBnXkFtZTcwMjY1NDYyMQ@@._V1__SX1138_SY995_.jpg",
                      "http://youtu.be/MnasfM3UtDc")

night_of_the_comet = media.Movie("Night of the Comet",
                     "The Earth is passing through the tail of a comet, an event which has not occurred in 65 million years.",
                     "http://upload.wikimedia.org/wikipedia/en/f/ff/NightoftheCometPoster.jpg",
                     "http://youtu.be/y9O-0B6OC0E")

enter_the_void = media.Movie("Enter the Void",
                             "Oscar lives in Tokyo with his younger sister Linda and supports himself by dealing drugs, against the advice of his friend, Alex.",
                             "http://upload.wikimedia.org/wikipedia/en/3/39/Enter-the-void-poster.png",
                             "http://youtu.be/JJkPLYmUyzg")

shark_attack_3 = media.Movie("Shark Attack 3: Megalodon",
                             "While diving, Ben finds a broken power cable with a large shark tooth stuck in it.",
                             "http://upload.wikimedia.org/wikipedia/en/2/2d/Shark_Attack_3_cover.jpg",
                             "http://youtu.be/BRYAL0fQ51g")

alien = media.Movie("Alien",
                    "In space, no one can hear you scream",
                    "http://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                    "http://youtu.be/bEVY_lonKf4")

movies = [sssssss, night_of_the_comet, enter_the_void, shark_attack_3, alien]
fresh_tomatoes.open_movies_page(movies)


