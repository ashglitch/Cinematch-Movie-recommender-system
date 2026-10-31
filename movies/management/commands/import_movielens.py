import csv
import io
import urllib.request
import zipfile
from collections import defaultdict
from django.core.management.base import BaseCommand, CommandError
from movies.models import Movie

DATA_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

class Command(BaseCommand):
    help = "Download MovieLens latest-small dataset and import its movies/ratings."

    def handle(self, *args, **options):
        self.stdout.write("Downloading MovieLens latest-small dataset from GroupLens...")
        try:
            request = urllib.request.Request(DATA_URL, headers={"User-Agent": "CineMatch student project"})
            with urllib.request.urlopen(request, timeout=60) as response:
                archive_bytes = response.read()
            archive = zipfile.ZipFile(io.BytesIO(archive_bytes))
            movie_file = next(n for n in archive.namelist() if n.endswith("/movies.csv"))
            rating_file = next(n for n in archive.namelist() if n.endswith("/ratings.csv"))
            ratings = defaultdict(list)
            with archive.open(rating_file) as stream:
                for row in csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8")):
                    ratings[row["movieId"]].append(float(row["rating"]))
            added = updated = 0
            with archive.open(movie_file) as stream:
                for row in csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8")):
                    title = row["title"]
                    year = 2000
                    if title.endswith(")") and "(" in title:
                        try: year = int(title.rsplit("(", 1)[1][:4])
                        except ValueError: pass
                    raw_genres = row["genres"].split("|")
                    supported = [g for g in raw_genres if g in dict(Movie.GENRE_CHOICES)]
                    genre = supported[0] if supported else "Drama"
                    vals = ratings.get(row["movieId"], [])
                    rating = (sum(vals) / len(vals) * 2) if vals else 0.0
                    movie, created = Movie.objects.update_or_create(
                        title=title[:200],
                        defaults={"genre": genre, "year": max(1888, min(year, 2100)),
                                  "description": "Genres: " + ", ".join(raw_genres),
                                  "rating": min(10.0, rating), "poster_url": ""}
                    )
                    if created: added += 1
                    else: updated += 1
            self.stdout.write(self.style.SUCCESS(f"MovieLens import complete. Added: {added}; updated: {updated}."))
            self.stdout.write("Note: MovieLens has no poster images. Use a TMDb poster dataset separately if desired.")
        except Exception as exc:
            raise CommandError(f"Could not download/import MovieLens: {exc}")
