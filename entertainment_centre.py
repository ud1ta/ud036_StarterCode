import media
import fresh_tomatoes

#Movie object for 2001: A Space Odyssey
aso_2001 = media.Movie("2001: A Space Odyssey",
                        #"An epic drama of adventure and exploration",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg",
                        "https://www.youtube.com/watch?v=XHjIqQBsPjk")

#Movie object for Blade Runner
blade_runner = media.Movie("Blade Runner",
                            #"Man has made his match. Now it's his problem.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,671,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=eogpIG53Cis")

#Movie object for First They Killed My Father
ftkmf = media.Movie("First They Killed My Father",
                    #"A Daughter of Combodia Remembers",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgzOTQ1NDUwOF5BMl5BanBnXkFtZTgwNjAwNTkwMzI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=uS3Vp_quGCw")

#Movie object for Blade Runner 2049
blade_runner_2049 = media.Movie("Blade Runner 2049",
                            #"Man has made his match. ...Now it's his problem.",
                            "https://cdn1.thr.com/sites/default/files/2017/05/blade_runner_xlg-embed.jpg",
                            "https://www.youtube.com/watch?v=gCcx85zbxz4")

#Movie object for Dunkirk
dunkirk = media.Movie("Dunkirk",
                      #"When 400,000 men couldn't get home...Home came for them",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=T7O7BtBnsG4")

#Movie object for Into the Wild
supertramp = media.Movie("Into the Wild",
                       # "Go with your heart",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")


#List of all the movie objects used by the open_movies_page method in the fresh_tomatoes module
movies = [aso_2001, blade_runner, ftkmf, blade_runner_2049, dunkirk, supertramp]

fresh_tomatoes.open_movies_page(movies)
