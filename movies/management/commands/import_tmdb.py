
import json
import pandas as pd

from datetime import datetime
from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = "Import movies from the TMDb CSV dataset"

    def handle(self, *args, **options):
        csv_path = "dataset/tmdb_5000_movies.csv"
        df = pd.read_csv(csv_path)

        genre_map = {
            "Action": "Action",
            "Comedy": "Comedy",
            "Drama": "Drama",
            "Science Fiction": "Sci-Fi",
            "Romance": "Romance",
            "Horror": "Horror",
            "Thriller": "Thriller",
            "Animation": "Animation",
            "Adventure": "Adventure",
            "Fantasy": "Fantasy",
        }

        added = 0
        updated = 0
        skipped = 0

        for _, row in df.iterrows():
            try:
                title = str(row["title"]).strip()

                if not title or title.lower() == "nan":
                    skipped += 1
                    continue

                raw_genres = json.loads(row["genres"])
                selected_genre = None

                for genre_item in raw_genres:
                    mapped = genre_map.get(genre_item["name"])
                    if mapped:
                        selected_genre = mapped
                        break

                if not selected_genre:
                    skipped += 1
                    continue

                release_date = row["release_date"]
                if pd.isna(release_date) or not str(release_date).strip():
                    year = 2000
                else:
                    year = datetime.strptime(
                        str(release_date), "%Y-%m-%d"
                    ).year

                if year < 1888 or year > 2100:
                    skipped += 1
                    continue

                description = row["overview"]
                if pd.isna(description) or not str(description).strip():
                    description = "No description available."

                rating = row["vote_average"]
                if pd.isna(rating):
                    rating = 0.0

                tmdb_id = int(row["id"])

                movie, created = Movie.objects.update_or_create(
                    tmdb_id=tmdb_id,
                    defaults={
                        "title": title[:200],
                        "genre": selected_genre,
                        "year": year,
                        "description": str(description),
                        "rating": float(rating),
                    },
                )

                if created:
                    added += 1
                else:
                    updated += 1

            except (ValueError, TypeError, KeyError, json.JSONDecodeError):
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete! Added: {added}, "
                f"Updated: {updated}, Skipped: {skipped}"
            )
        )
