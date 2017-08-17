import media
import fresh_tomatoes


# creating instances for the class movie
got = media.Movie("Game of Thrones",
                  "A Game of Thrones is the first novel"
                  " in A Song of Ice and Fire,"
                  "a series of fantasy novels by American"
                  " author George R. R. Martin. It was"
                  " first published on August 1, 1996.",
                  "http://www.hollywoodreporter.com/sites/default"
                  "/files/2011/03/got_-_official_poster.jpg",
                  "https://www.youtube.com/watch?v=Stw6INIS570")
# print(got.story)
# prints storyline
# got.showtrailer()
# opens youtube trailer
# after creating got init function is called
# similarly for the rest of them
flash = media.Movie("Flash",
                    "Barry Allen, a forensic scientist"
                    " with the Central City police force,"
                    "is struck by lightning in a freak accident."
                    " When he wakes up after nine months,"
                    "he discovers that he can achieve great speeds.",
                    "http://seriestv.biz/wp-content/uploads/2017/06/"
                    "The-Flash-Season-4-poster-tv-The-CW.png",
                    "https://www.youtube.com/watch?v=W_ThBS7hrLI")

suits = media.Movie("Suits",
                    "Mike Ross, a talented young college dropout,"
                    "is hired as an associate by Harvey Specter,"
                    " one of New York's best lawyers."
                    "They must handle cases while keeping"
                    " Mike's qualifications a secret.",
                    "https://fanart.tv/fanart/tv/247808"
                    "/tvposter/suits-52b60286a3ee1.jpg",
                    "https://www.youtube.com/watch?v=7tUjQICfJEk")

now = media.Movie("Now You See Me",
                  "The Horsemen, a group of four street magicians,"
                  "rob a huge sum of money that belongs"
                  " to insurance magnate Arthur Tressler."
                  "The group is chased by FBI agent Dylan"
                  " Rhodes and Interpol agent Alma Dray.",
                  "http://t3.gstatic.com/images?q=tbn:ANd9GcSiVU-YMu"
                  "-9iM1YT68QCa322Q_fSe8D9DmmCRahPfTY9evxLty2",
                  "https://www.youtube.com/watch?v=KzJNYYkkhzc")

ratatouille = media.Movie("Ratatouille",
                          "The rat as the chief",
                          "http://static.rogerebert.com/"
                          "uploads/movie/movie_poster"
                          "/ratatouille-2007/large_taAPNsf6G"
                          "4EXBYSG7Jyvd9HHKnH.jpg",
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")

baby = media.Movie("Baby's day out",
                   "Three bumbling crooks pose as photographers"
                   "to kidnap the son of a millionaire."
                   "But the baby turns out to be smarter than them,"
                   "making it difficult for them to hold on to him.",
                   "http://www.gstatic.com/tv/thumb/movieposters"
                   "/15781/p15781_p_v8_ac.jpg",
                   "https://www.youtube.com/watch?v=pzow5wUp7hY")
# list of movies (grouping all the instances together)
movies = [got, flash, suits, now, ratatouille, baby]
# open moviespage and takesin the list of movies
fresh_tomatoes.open_movies_page(movies)
