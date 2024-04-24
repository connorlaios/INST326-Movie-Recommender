""" A Program that recommends movies based on the users favorite movies. """

import argparse
import sys
class Movie:
    """A movie.
    
    Attributes:
        name (str): a string of the movie's name.
        genre (str): a string of the movie's genre.
    
    """
class Movies:
    """The purpose of this class is to represent a specific movie
  
    Attributes:
       "name": a string containing the name of the movie
       "genre": a string containing the genre of the movie
         
    """
    def __init__(self, name, genre):
        """ Initializes a new movie object
      
        Args:
       	    "name": a string containing the name of the movie
       	    "genre": a string containing the genre of the movie         
       
        Side effects:
           create and populate the attributes as a list of dictionary where 
           the name is the key and the genre is the value
    
        """
        self.name = name
        self.genre = genre

    def count_genre(self, mov_dict):
        """ Takes in the favorite movies dictionary and counts the number of
        movies the user has from each popular movie genre. Whichever genre has
        the highest number of occurances, will be set as the users favorite 
        genre. (List comprehension)
        Implemented by Connor Laios.

        Args:
            mov_dict (Dictionary): Dictionary with the users favorite movies as
            the keys and its associated genre as the value.

        Returns:
            fav_genre (str): A string with the name of the users favorite genre.
        """
        genre_list = list(mov_dict.values())

        action = [x for x in genre_list if "Action" in x]
        adventure = [x for x in genre_list if "Adventure" in x]
        drama = [x for x in genre_list if "Drama" in x]
        comedy = [x for x in genre_list if "Comedy" in x]
        horror = [x for x in genre_list if "Horror" in x]
        romance = [x for x in genre_list if "Romance" in x]
        
        if (len(action) > len(adventure) and len(action) > len(drama) and
            len(action) > len(comedy) and len(action) > len(horror) and 
            len(action) > len(romance)):
            fav_genre = "Action"
        if (len(adventure) > len(action) and len(adventure) > len(drama) and 
            len(adventure) > len(comedy) and len(adventure) > len(horror) and 
            len(adventure) > len(romance)):
            fav_genre = "Adventure"
        if (len(drama) > len(action) and len(drama) > len(adventure) and 
            len(drama) > len(comedy) and len(drama) > len(horror) and 
            len(drama) > len(romance)):
            fav_genre = "Drama"
        if (len(comedy) > len(action) and len(comedy) > len(adventure) and 
            len(comedy) > len(drama) and len(comedy) > len(horror) and 
            len(comedy) > len(romance)):
            fav_genre = "Comedy"
        if (len(horror) > len(action) and len(horror) > len(adventure) and 
            len(horror) > len(drama) and len(horror) > len(comedy) and 
            len(horror) > len(romance)):
            fav_genre = "Horror"
        if (len(romance) > len(action) and len(romance) > len(adventure) and 
            len(romance) > len(drama) and len(romance) > len(comedy) and 
            len(romance) > len(horror)):
            fav_genre = "Romance"

        return fav_genre

    def recommend_movies(self, fav_genre):
        """ Creates a list of each movie genre, each list will contain highly
        rated movies from the genre. It will then use fav_genre to return the
        list of highly rated movies from the users favorite genre. 
        (Conditional Expressions)
        Implemented by Connor Laios.

        Args:
            fav_genre (str): The users favorite genre.

        Returns:
            mov_recs (list): List of movies that will be recommended to user.

        """
        mov_recs = (["Die Hard", "The Matrix", "The Dark Night", "Gladiator",
                     "Black Panther", "Aliens", "Jurassic Park"] 
                     if fav_genre == "Action" 
                     else ["Uncharted", "Jumanji", "Moby Dick", "King Kong", 
                     "The Lost City of Z", "Tenet", "Back To The Future"] 
                     if fav_genre == "Adventure" 
                     else ["The Shawshank Redemption", "Gravity", "Parasite", 
                     "Interstellar", "Joker", "Searching", "Wonder"] 
                     if fav_genre == "Drama" 
                     else ["The Hangover", "Deadpool", "Dumb & Dumber", 
                     "Horrible Bosses", "21 Jump Street", "Superbad", 
                     "Groundhog Day"] if fav_genre == "Comedy" 
                     else ["The Conjuring", "The Boy", "Get Out", "It", 
                     "A Quiet Place", "Hush", "Smile"] if fav_genre == "Horror" 
                     else ["The Notebook", "Titanic", "About Time", 
                     "Crazy, Stupid, Love", "Me Before You", "The Best of Me", 
                     "The Shape of Water"])


        return mov_recs
    
    def sort_movie(self, mov_recs):
        """sorts user's recommened movies alphabetically 
        -Implemented by Carrington Gant (List sorting with key function)
        
        Args:
            mov_recs(list): List of movies reccomended to user.    
        Returns:
            sorted_movrecs(list): Alphabetized movie names in list.
        
        """
        sorted_movrecs = sorted(mov_recs, key = lambda x: x[0])
        return (sorted_movrecs)

    def remove_duplicates(self, mov_dict, rec_list):
        """ Takes in the users favorite movies dictionary and the recommended
        movies list and removes the movies the user has already seen from the 
        recommended movies list. 
        --Implemented by Carrington Gant (Set operations).

        Args:
            mov_dict (Dictionary): Dictionary with the users favorite movies as
            the keys and its associated genre as the value.
            rec_list (list): List of movies that will be recommended to user.

        Returns:
            final_rec (list): List of movies that will be recommended to user
            with the ones they have seen removed.

        """
        movdict_set = set(mov_dict.keys())
        reclist_set = set(rec_list)
        final_rec = reclist_set - movdict_set
        return final_rec
        
    def __repr__(self):
        """A representation of a Movie Object
        - magic method, __repr__
        Implemented by Bridget 
        
        Args:
            no args
        
        Returns:
            returns the the title of a movie and its genre
        """
        return f'Movie("{self.name}, {self.genre}")'
        
     
def display_movies(fav_genre, mov_recs):
    """Shows a list of recommended movies for user based on the
        user's calculated favorite genre 
        - f-string 
        Implemented by Bridget 
        
        Args:
            fav_genre(str): a string of the user's favorite genre
            mov_recs(list): a list of recommended movies for user
        
        Returns:
            returns the list of recommended movies
        """
    print(f"We have calculated that your favorite movie genre is: {fav_genre}")
    print(f"Here are some movies we recommend you watch:")
    print(*mov_recs, sep = ", ")
    
        
def main(filepath):
    """Read movie data from user

    Args:
        filepath (str): a path to a txt file containing movie data
    Returns:
        recommendations(list): list of movie recommendations
    """
    movie_dict = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            info = line.split("\t")
            movie_dict[info[0]] = info[1]
            movie_data = Movies(info[0], info[1])
        
        fav_genre = movie_data.count_genre(movie_dict)
        movie_recs = (movie_data.recommend_movies
                     (movie_data.count_genre(movie_dict)))
        remove_duplicates = movie_data.remove_duplicates(movie_dict, movie_recs)
        sort_movie = movie_data.sort_movie(remove_duplicates)
        display_movies(fav_genre, sort_movie)
        
            
def parse_args(arglist):
    """Parse command-line arguemnts
    
    Expect 1 mandatory argument
    -filepath(str): a path to a txt file containing movie data
    
    Args:
        arglist(list of str): arguments from the command line

    Returns:
        namespace: the parsed arguments, as a namespace.
    """    ''''''
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="path to txt file containing"
                        "user's movie")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)
    
        
