# Dataset setup

CineMatch includes a management command that fetches the MovieLens latest-small dataset directly from GroupLens and imports its movie titles, genres, and average ratings into the local database.

From the project directory, after installing requirements and running migrations:

```bash
python manage.py import_movielens
```

Official dataset page: https://grouplens.org/datasets/movielens/latest/

The latest-small dataset contains about 9,700 movies and 100,000 ratings. It is intended for education and development. Review the included dataset README/license terms and acknowledge GroupLens in your project report. MovieLens does not include poster images or plot summaries. The app's starter catalogue remains available if the download is unavailable.

The dataset archive itself is not bundled in this ZIP; the import command downloads it when you run the command on a computer with internet access. This avoids repackaging external dataset files without verifying their current terms.
