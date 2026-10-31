
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Movie


def get_recommendations(movie_id, limit=5):
    movies = list(Movie.objects.all())

    if len(movies) < 2:
        return []

    # Combine each movie's genre and description
    movie_texts = [
        f"{movie.genre} {movie.genre} {movie.description}"
        for movie in movies
    ]

    # Convert text into numerical features
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(movie_texts)

    # Calculate similarity between movies
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Find the selected movie
    selected_index = next(
        (i for i, movie in enumerate(movies)
         if movie.id == movie_id),
        None
    )

    if selected_index is None:
        return []

    # Rank the most similar movies
    scores = list(enumerate(similarity_matrix[selected_index]))
    scores = [
        (index, score)
        for index, score in scores
        if index != selected_index
    ]
    scores.sort(key=lambda item: item[1], reverse=True)

    return [
        {
            "movie": movies[index],
            "similarity": round(float(score) * 100, 1),
        }
        for index, score in scores[:limit]
    ]

def get_personalized_recommendations(
    favorite_genres,
    favorite_movie_id=None,
    limit=5
):
    movies = list(Movie.objects.all())

    if not movies:
        return {"best_matches": [], "discover": []}

    favorite_genres = set(favorite_genres)
    favorite_movie = next(
        (
            movie for movie in movies
            if favorite_movie_id
            and movie.id == favorite_movie_id
        ),
        None
    )

    # Build text features for all movies
    movie_texts = [
        f"{movie.genre} {movie.genre} {movie.description}"
        for movie in movies
    ]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(movie_texts)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    scored_movies = []

    for index, movie in enumerate(movies):
        # Don't recommend the user's favourite movie itself
        if favorite_movie and movie.id == favorite_movie.id:
            continue

        genres = {
            genre.strip()
            for genre in movie.genre.split(",")
        }

        # Genre preference score
        genre_score = (
            len(genres & favorite_genres) / len(favorite_genres)
            if favorite_genres else 0
        )

        # Similarity to the favourite movie
        movie_score = 0

        if favorite_movie:
            favorite_index = next(
                i for i, item in enumerate(movies)
                if item.id == favorite_movie.id
            )
            movie_score = float(
                similarity_matrix[index][favorite_index]
            )

        # Normalise rating from a 10-point scale
        rating_score = min(max(movie.rating / 10, 0), 1)

        # Personalised combined score
        if favorite_genres and favorite_movie:
            score = (
                0.45 * genre_score
                + 0.40 * movie_score
                + 0.15 * rating_score
            )
        elif favorite_genres:
            score = 0.75 * genre_score + 0.25 * rating_score
        elif favorite_movie:
            score = 0.85 * movie_score + 0.15 * rating_score
        else:
            score = rating_score

        scored_movies.append({
            "movie": movie,
            "score": round(score * 100, 1),
            "genre_score": genre_score,
            "similarity": movie_score,
        })

    # Best matches: highest preference scores first
    best_matches = sorted(
        scored_movies,
        key=lambda item: item["score"],
        reverse=True
    )[:limit]

    # Discovery: prioritise different genres while retaining relevance
    best_ids = {item["movie"].id for item in best_matches}
    remaining = [
        item for item in scored_movies
        if item["movie"].id not in best_ids
    ]

    def discovery_score(item):
        movie = item["movie"]
        genres = {
            genre.strip() for genre in movie.genre.split(",")
        }

        # Give a small bonus to movies outside selected genres
        new_genre_bonus = (
            0.15 if favorite_genres and not genres.intersection(
                favorite_genres
            ) else 0
        )

        return item["score"] + new_genre_bonus * 100

    discover = sorted(
        remaining,
        key=discovery_score,
        reverse=True
    )[:limit]

    return {
        "best_matches": best_matches,
        "discover": discover,
    }

