# Replace an element in a tuple (convert to list and back).

fav_movies = ("Thor" , "Iron-Man" , "Avengers" , "Avengers-Infinity-War", "Avengers-Endgame", "Avenger-Domsday")

y=list(fav_movies)

y[1] = "Captin-America-The-Winter-Solider"

x=tuple(y)

print(x)