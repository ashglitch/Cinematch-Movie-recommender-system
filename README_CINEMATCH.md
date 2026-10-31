# CineMatch — Movie Discovery & Recommendation

CineMatch is a Django student project with a cinematic charcoal-and-red interface. It keeps the original Django foundation while adding a more polished discovery experience. The design uses no emoji UI.

## Features

- Personalized movie recommendations and similar-title discovery
- Search and genre filtering
- Interactive spin-to-pick movie wheel with genre selection
- User sign-up/login and personal watchlist
- SQLite database and starter movie catalogue
- Optional MovieLens dataset import for a much larger catalogue
- Optional TMDb import/poster commands for compatible local data
- Responsive layouts for desktop and mobile

## Run on Windows

1. Install Python 3.10 or newer.
2. Extract the ZIP to a normal folder.
3. Open that folder in VS Code. It is the folder containing `manage.py`.
4. Open Terminal → New Terminal and run:

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   py manage.py migrate
   py manage.py load_movies
   py manage.py runserver
   ```

5. Open http://127.0.0.1:8000/ in your browser.

Alternatively, double-click `run_cinematch.bat`; it installs requirements, migrates the database, loads starter movies, and starts the development server.

## Import the MovieLens dataset (recommended)

After installing dependencies and running migrations, run:

```powershell
py manage.py import_movielens
```

This command downloads the MovieLens latest-small archive from GroupLens and imports movie titles, genres, and average ratings. The dataset is not bundled in this ZIP because it is fetched from the official source at setup time. Details and attribution guidance are in `DATASET_INFO.md`. Official page: https://grouplens.org/datasets/movielens/latest/

## Optional metadata and posters

The project contains `import_tmdb` and `import_posters` commands for compatible local files. External metadata/poster datasets may have separate terms and may require an API key; check their terms before using or redistributing them. MovieLens itself does not provide posters or plot descriptions.

## Troubleshooting

- If `py` is not recognized, try `python` instead.
- If the MovieLens import fails, check your internet connection and try again; the starter catalogue can still be used.
- If the wheel has no candidates, load the starter catalogue with `py manage.py load_movies` and refresh the page.
- To create an administrator account, run `py manage.py createsuperuser`.

## Before deployment

This is a local student-project prototype. Before publishing it publicly, set a private `SECRET_KEY`, turn `DEBUG` off, configure `ALLOWED_HOSTS`, enable HTTPS, and configure production static-file serving.
