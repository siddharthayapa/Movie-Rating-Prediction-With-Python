# Movie rating prediction
def predict_movie_rating(user_ratings, movie_id):
    """
    Predict the rating for a movie based on average user ratings.
    :param user_ratings: Dictionary with movie IDs and their ratings
    :param movie_id: Movie ID for which prediction is needed
    :return: Predicted rating (float)
    """
    if movie_id in user_ratings:
        # Calculate the average rating for the movie
        ratings = user_ratings[movie_id]
        predicted_rating = sum(ratings) / len(ratings)
        return round(predicted_rating, 2)
    else:
        return "No rating data available for this movie."

# Example data: user ratings for movies
user_ratings = {
    1: [4.5, 4.0, 5.0],  # Ratings for movie with ID 1
    2: [3.0, 3.5, 4.0],  # Ratings for movie with ID 2
    3: [2.0, 2.5],       # Ratings for movie with ID 3
}

# Predict ratings for movies
movie_id = 1  # Movie ID to predict rating for
predicted_rating = predict_movie_rating(user_ratings, movie_id)

print(f"Predicted rating for movie {movie_id}: {predicted_rating}")

movie_id = 4  # Movie ID to predict rating for (not in the dataset)
predicted_rating = predict_movie_rating(user_ratings, movie_id)

print(f"Predicted rating for movie {movie_id}: {predicted_rating}")
