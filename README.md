# CineMatch — Movie Recommendation System

**Discover your next favourite movie.**

CineMatch is a Django-based movie recommendation web application designed to make discovering movies easier and more enjoyable. It provides a centralized platform where users can explore movies, discover recommendations, create accounts, and maintain a personal watchlist.

Built with Python and Django, CineMatch combines a web-based interface with movie data management to deliver a personalized movie discovery experience.

---

## Overview

Choosing a movie can be surprisingly difficult when there are thousands of options available. CineMatch aims to simplify this process by bringing movie discovery and personal watchlist management into one place.

The project focuses on creating an intuitive, visually engaging experience that helps users explore movies and keep track of titles they want to watch.

## Features

### Movie Discovery
- Browse and explore movies through a dedicated web interface.
- Access movie information provided by the application's movie dataset.
- Discover movies through the recommendation functionality.

### User Authentication
- User registration and login.
- Individual user accounts.
- Account-based access to personalized features.

### Personal Watchlist
- Maintain a collection of movies to watch later.
- Keep track of selected movies through a dedicated watchlist interface.

### Movie Data Management
- Import and manage movie data through Django management commands.
- Support for movie dataset integration.
- Organized database models for storing movie information and user watchlists.

### Interactive User Interface
- Custom CSS styling and JavaScript functionality.
- Dedicated pages for movie discovery, authentication, and watchlists.
- A cinematic visual direction designed to make the browsing experience engaging.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Django | Backend web framework |
| SQLite | Local development database |
| HTML | Web page structure |
| CSS | Styling and layout |
| JavaScript | Client-side interactions |
| Pandas | Data processing and dataset handling |
| Git & GitHub | Version control and source code hosting |

*The stack above reflects the project's current setup and dependencies; individual components may be used by specific modules rather than throughout the application.*

---

## Project Structure

```text
Cinematch-Movie-recommender-system/
│
├── cinematch/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── movies/
│   ├── management/
│   │   └── commands/
│   │       ├── import_movielens.py
│   │       ├── import_posters.py
│   │       ├── import_tmdb.py
│   │       └── load_movies.py
│   │
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   │
│   ├── templates/
│   │   └── movies/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── watchlist.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── recommendations.py
│   ├── admin.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Getting Started

Follow these steps to run CineMatch locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or a compatible version supported by the project dependencies.
- pip, Python's package installer.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/ashglitch/Cinematch-Movie-recommender-system.git
```

Navigate to the project directory:

```bash
cd Cinematch-Movie-recommender-system
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

This initializes the database tables required by the application.

### 5. Create an Administrator Account (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to configure your administrator account.

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

**http://127.0.0.1:8000/**

The application should now be available locally.

---

## Movie Dataset Setup

CineMatch includes management commands for loading and importing movie data.

The repository contains commands related to MovieLens and TMDB data, as well as poster imports.

Before importing data, check the available command options and the instructions in `DATASET_INFO.md`.

For example, the MovieLens import command may be run as follows if its required dataset files are available:

```bash
python manage.py import_movielens
```

**Note:** The exact dataset files, their locations, and any additional arguments depend on the import command's implementation. Consult the project documentation before running an import.

Some movie metadata or poster-import workflows may require external data sources or API credentials. Keep any credentials in environment variables or a local `.env` file, and never commit secrets to GitHub.

---

## Database

CineMatch uses Django's database framework to manage application data.

SQLite is suitable for local development and testing. Django migrations are included to create and update the database schema.

The local database file is not required to clone the repository. After cloning, run the migrations and follow the dataset setup instructions to prepare your local instance.

---

## Security Notes

Before running or deploying the application:

- Keep secret keys and API credentials out of source control.
- Store sensitive configuration in environment variables.
- Do not upload your local database if it contains personal or development data.
- Use secure production settings before making the application publicly accessible.
- Configure an appropriate production database and static-file serving strategy when deploying.

The Django development server is intended for development, not production hosting.

---

## Future Enhancements

Potential improvements for future versions include:

- **Genre Selection Wheel:** An interactive, pizza-slice-style wheel for choosing movie genres and discovering films.
- **Enhanced Recommendations:** More personalized recommendations based on user preferences and movie characteristics.
- **Advanced Search and Filtering:** Search movies by genre, release year, rating, and other attributes.
- **Movie Ratings and Reviews:** Allow users to rate movies and share their opinions.
- **Improved Movie Details:** Add richer movie information, posters, and metadata.
- **Deployment:** Host the application online so users can access it without running it locally.
- **Responsive Design:** Further improve usability across mobile devices, tablets, and desktops.

These items represent potential improvements and should not be considered implemented until they are available in the application.

---

## Learning Objectives

This project provides practical experience with:

- Developing a full-stack web application using Django.
- Designing database models and working with migrations.
- Implementing user authentication and personalized features.
- Processing and importing structured movie datasets.
- Connecting backend logic to frontend templates.
- Using Git and GitHub for version control and project collaboration.

---

## Contributing

Suggestions and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes locally.
5. Submit a pull request describing your improvements.

For example:

```bash
git checkout -b feature/your-feature-name
```

---

## Author

**Aashi Gupta**

GitHub: [@ashglitch](https://github.com/ashglitch)

Project Repository: [CineMatch — Movie Recommender System](https://github.com/ashglitch/Cinematch-Movie-recommender-system)

---

## License

A license has not yet been specified for this project. If you plan to distribute or accept contributions to the code, consider adding an appropriate open-source license.

---

**CineMatch — Find your next favourite movie.**
