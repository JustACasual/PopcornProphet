import random
import requests
from bs4 import BeautifulSoup, NavigableString
import json


# Define the IMDb top 50 movies list using Wikipedia page.
def get_top_50_movies():
    url = "https://de.wikipedia.org/wiki/IMDb_Top_250_Movies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_table = soup.find("table", class_="wikitable")
    top_50_movies = []
    for row in movie_table.find_all("tr")[1:51]:
        cells = row.find_all("td")
        rank_content = [content for content in cells[0].contents if isinstance(content, NavigableString)]
        rank = int(rank_content[0].strip())
        title = cells[1].text.strip()
        year = int(cells[2].text.strip())
        top_50_movies.append({"rank": rank, "title": title, "year": year})
    return top_50_movies

# Recommended movies so far
def get_recommended_movies():
    try:
        with open("history.json", "r") as file:
            recommended_movies = json.load(file)
    except FileNotFoundError:
        recommended_movies = []
        with open("history.json", "w") as file:
            json.dump(recommended_movies, file, indent=4)
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
    print("Next Recommendation:")
    print("Title:", next_recommendation['title'])
    print("Rank:", next_recommendation['rank'])
    print("Year:", next_recommendation['year'])
    user_input = input("Show all recommendations? (y/n): ")
    if user_input.lower() == "y":
        print("All Recommendations:")
        for recommendation in recommendations:
            print("Title:", recommendation['title'])
            print("Rank:", recommendation['rank'])
            print("Year:", recommendation['year'])
            print("---------------------------------")

# Save the updated list of recommended movies to a file.
def save_recommendations(recommended_movies):
    user_confirmation = input("Save recommendation? (y/n): ")
    if user_confirmation.lower() == "y":
        with open("history.json", "w") as file:
            json.dump(recommended_movies, file, indent=4)
        print("Recommendation saved.")
    else:
        print("Recommendation not saved.")

def main():
    top_50_movies = get_top_50_movies()
    recommended_movies = get_recommended_movies()
    next_recommendation = recommend_movie(top_50_movies, recommended_movies)
    recommendations = get_all_recommendations(recommended_movies)
    display_recommendations(next_recommendation, recommendations)
    save_recommendations(recommended_movies)

if __name__ == "__main__":
    main()
