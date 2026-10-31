
import pandas as pd

from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = "Match poster URLs to existing movies using TMDb IDs"

    def handle(self, *args, **options):
        csv_path = "dataset/train.parquet"

        self.stdout.write("Reading poster dataset...")

        # Read only the columns we need.
        df = pd.read_parquet(
            csv_path,
            columns=["tmdb_id", "web_url"],
        )

        # Keep one valid poster URL per TMDb ID.
        df = df.dropna(subset=["tmdb_id", "web_url"])
        df["tmdb_id"] = pd.to_numeric(
            df["tmdb_id"], errors="coerce"
        )
        df = df.dropna(subset=["tmdb_id"])
        df["tmdb_id"] = df["tmdb_id"].astype("int64")
        df = df.drop_duplicates(subset=["tmdb_id"])

        poster_map = dict(zip(df["tmdb_id"], df["web_url"]))

        updated = 0

        # Update only movies that have a matching poster.
        movies = Movie.objects.filter(
            tmdb_id__isnull=False
        ).only("id", "tmdb_id", "poster_url")

        for movie in movies.iterator(chunk_size=500):
            url = poster_map.get(movie.tmdb_id)

            if url and url.startswith("https://image.tmdb.org/"):
                if movie.poster_url != url:
                    movie.poster_url = url
                    movie.save(update_fields=["poster_url"])
                    updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Poster import complete! Updated {updated} movies."
            )
        )
