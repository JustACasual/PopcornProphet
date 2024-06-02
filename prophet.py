import random
from imdb import Cinemagoer

# Define the IMDb top 50 movies list again.
def get_top_50_movies():
    ia = Cinemagoer()
    top_50_movies = []
    top_movies = ia.get_top250_movies()
    for i, movie in enumerate(top_movies[:50]):
        title = movie['title']
        year = movie['year']
        top_50_movies.append((i+1, title, year))
    return top_50_movies

# Recommended movies so far, including the previous state before reset.
def get_recommended_movies():
    recommended_movies = [
        (2, "The Godfather", 1972),
        (3, "The Godfather: Part II", 1974),
        (35, "Back to the Future", 1985),
        (8, "Pulp Fiction", 1994),
    ]
    return recommended_movies

# Function to pick another random movie from the top 50, excluding already recommended ones.
def recommend_movie(top_50_movies, recommended_movies):
    available_movies = [movie for movie in top_50_movies if movie not in recommended_movies]
    if not available_movies:
        return "All movies have been recommended."
    new_recommendation = random.choice(available_movies)
    recommended_movies.append(new_recommendation)
    return new_recommendation

# Function to get the list of all recommended movies.
def get_all_recommendations(recommended_movies):
    return recommended_movies

# Display the next recommendation and the updated list of all recommended movies.
def display_recommendations(next_recommendation, recommendations):
    print("Next Recommendation:", next_recommendation)
    print("All Recommendations:", recommendations)

def main():
    top_50_movies = get_top_50_movies()
    recommended_movies = get_recommended_movies()
    next_recommendation = recommend_movie(top_50_movies, recommended_movies)
    recommendations = get_all_recommendations(recommended_movies)
    display_recommendations(next_recommendation, recommendations)

if __name__ == "__main__":
    main()
