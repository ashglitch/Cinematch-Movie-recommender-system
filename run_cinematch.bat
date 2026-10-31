@echo off
setlocal
cd /d "%~dp0"
py -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py load_movies
 echo.
echo CineMatch is ready. Keep this window open.
echo Open http://127.0.0.1:8000/ in your browser.
python manage.py runserver
pause
