
from django.core.management.base import BaseCommand
from movies.models import Movie


MOVIES = [
    ("Inception", "Sci-Fi", 2010, 8.8, "A thief enters dreams to steal secrets and plant an idea."),
    ("Interstellar", "Sci-Fi", 2014, 8.7, "Explorers travel through a wormhole to find a new home for humanity."),
    ("The Matrix", "Sci-Fi", 1999, 8.7, "A hacker discovers the hidden truth about his reality."),
    ("Dune", "Sci-Fi", 2021, 8.0, "A young noble travels to a dangerous desert planet."),
    ("Arrival", "Sci-Fi", 2016, 7.9, "A linguist tries to communicate with mysterious visitors."),
    ("The Dark Knight", "Action", 2008, 9.0, "Batman faces a criminal mastermind who threatens Gotham."),
    ("John Wick", "Action", 2014, 7.4, "A retired assassin returns to the underworld."),
    ("Gladiator", "Action", 2000, 8.5, "A betrayed Roman general seeks justice."),
    ("Mad Max: Fury Road", "Action", 2015, 8.1, "Survivors race across a dangerous wasteland."),
    ("Top Gun: Maverick", "Action", 2022, 8.2, "A veteran pilot trains a new generation of aviators."),
    ("The Avengers", "Action", 2012, 8.0, "Superheroes unite to protect Earth."),
    ("Black Panther", "Action", 2018, 7.3, "A new king protects the hidden nation of Wakanda."),
    ("Mission: Impossible - Fallout", "Action", 2018, 7.7, "An agent races to stop a global catastrophe."),
    ("Die Hard", "Action", 1988, 8.2, "A detective confronts criminals in a skyscraper."),
    ("The Hangover", "Comedy", 2009, 7.7, "Friends try to piece together a chaotic night in Las Vegas."),
    ("Superbad", "Comedy", 2007, 7.6, "Two friends navigate the end of high school."),
    ("Mean Girls", "Comedy", 2004, 7.1, "A new student enters a competitive high-school social scene."),
    ("Home Alone", "Comedy", 1990, 7.7, "A child defends his home from two burglars."),
    ("Groundhog Day", "Comedy", 1993, 8.0, "A weatherman relives the same day repeatedly."),
    ("The Grand Budapest Hotel", "Comedy", 2014, 8.1, "A hotel concierge becomes involved in a strange mystery."),
    ("3 Idiots", "Comedy", 2009, 8.4, "Three engineering students challenge academic pressure."),
    ("Hera Pheri", "Comedy", 2000, 8.2, "Three men become tangled in a ridiculous phone scam."),
    ("Titanic", "Drama", 1997, 7.9, "Two passengers fall in love aboard a doomed ocean liner."),
    ("The Shawshank Redemption", "Drama", 1994, 9.3, "Two prisoners form a lasting friendship."),
    ("Forrest Gump", "Drama", 1994, 8.8, "A kind-hearted man witnesses major moments in history."),
    ("The Pursuit of Happyness", "Drama", 2006, 8.0, "A father struggles to build a better life for his son."),
    ("Good Will Hunting", "Drama", 1997, 8.3, "A gifted young man discovers his potential with a therapist."),
    ("Whiplash", "Drama", 2014, 8.5, "A drummer faces an intense and demanding music instructor."),
    ("The Social Network", "Drama", 2010, 7.8, "The creation of a social networking company sparks conflict."),
    ("Taare Zameen Par", "Drama", 2007, 8.3, "An art teacher helps a child who struggles at school."),
    ("The Notebook", "Romance", 2004, 7.8, "Two young lovers face obstacles across the years."),
    ("Pride and Prejudice", "Romance", 2005, 7.8, "Elizabeth Bennet navigates love and social expectations."),
    ("La La Land", "Romance", 2016, 8.0, "A musician and an actor pursue dreams in Los Angeles."),
    ("Before Sunrise", "Romance", 1995, 8.1, "Two strangers spend a night talking in Vienna."),
    ("10 Things I Hate About You", "Romance", 1999, 7.3, "A high-school dating scheme becomes unexpectedly complicated."),
    ("The Conjuring", "Horror", 2013, 7.5, "Paranormal investigators help a family in a haunted house."),
    ("Get Out", "Horror", 2017, 7.8, "A visit to meet a girlfriend's family takes a disturbing turn."),
    ("A Quiet Place", "Horror", 2018, 7.5, "A family survives in a world hunted by sound-sensitive creatures."),
    ("The Shining", "Horror", 1980, 8.4, "A family's winter stay at a hotel becomes terrifying."),
    ("IT", "Horror", 2017, 7.3, "A group of children confronts a sinister entity."),
    ("Se7en", "Thriller", 1995, 8.6, "Two detectives hunt a killer inspired by the seven deadly sins."),
    ("Gone Girl", "Thriller", 2014, 8.1, "A disappearance turns a marriage into a media spectacle."),
    ("Shutter Island", "Thriller", 2010, 8.2, "A marshal investigates a disappearance at a remote hospital."),
    ("Knives Out", "Thriller", 2019, 7.9, "A detective investigates a wealthy family's suspicious death."),
    ("The Silence of the Lambs", "Thriller", 1991, 8.6, "An FBI trainee seeks help from an imprisoned criminal."),
    ("Toy Story", "Animation", 1995, 8.3, "Toys come alive when humans are not around."),
    ("Finding Nemo", "Animation", 2003, 8.2, "A clownfish crosses the ocean to find his missing son."),
    ("Spider-Man: Into the Spider-Verse", "Animation", 2018, 8.4, "A teenager meets Spider-heroes from other dimensions."),
    ("Coco", "Animation", 2017, 8.4, "A boy explores the Land of the Dead through music."),
    ("The Lion King", "Animation", 1994, 8.5, "A young lion learns to accept his destiny."),
]


class Command(BaseCommand):
    help = "Load sample movies into the CineMatch database"

    def handle(self, *args, **options):
        added = 0

        for title, genre, year, rating, description in MOVIES:
            _, created = Movie.objects.update_or_create(
                title=title,
                defaults={
                    "genre": genre,
                    "year": year,
                    "rating": rating,
                    "description": description,
                },
            )

            if created:
                added += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Loaded {len(MOVIES)} movies. Added {added} new records."
            )
        )
