def movie_organizer(*args):

    movie_dict = {}

    for movie, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(movie)



    sorted_dict = sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    

    result = ''
    
    for movies in sorted_dict:
        result += f'\n{movies[0]} - {len(movies[1])}'
        for movie in sorted(movies[1]):
            result += f'\n* {movie}' 
        
    return result.strip()



print(movie_organizer(

("Avatar: The Way of Water", "Action"), ("House Of Gucci", "Drama"), ("Top Gun", "Action"), ("Ted", "Comedy"), ("Duck Soup", "Comedy"), ("The Dark Knight", "Action"), ("A Star Is Born", "Musicals"), ("The Warrior", "Action"), ("Like A Boss", "Comedy"), ("The Green Mile", "Drama"), ("21 Jump Street", "Comedy")))