# Add and remove elements in a tuple using conversion.

fav_movies = ("Thor" , "Iron-Man" , "Avengers" , "Avengers-Infinity-War", "Avengers-Endgame", "Avenger-Domsday")

y=list(fav_movies)

y.remove("Thor")

print(y)

y.append("Gurdian-Of-Galxay")

x=tuple(y)

print(x)