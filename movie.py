"""Movie class."""

from data_wrangling import read_csv_rows
from data_wrangling import columnar 

class Movie:

    title: str
    mcu_year: float
    release_year: int

    def __init__(self, name: str, mcu_point: float, release: int):
        """Movie's constructor."""
        self.title = name
        self.mcu_year = mcu_point
        self.release_year = release

    def __str__(self) -> str:
        """Magic method for print()."""
        return f"{self.title} ({self.release_year})"
    

filename: str = "data/mcu_timeline.csv"
table: list[dict[str, str]] = read_csv_rows(filename)
table = columnar(filename)

# PHASE 1-3 MCU MOVIES
all_movies: list[Movie] = []

iron_man_1: Movie = Movie("Iron Man", 2010.1, 2008)
hulk: Movie = Movie("The Incredible Hulk", 2005.1, 2008)
iron_man_2: Movie = Movie("Iron Man 2", 2011.1, 2010)
thor_1: Movie = Movie("Thor", 2011.2, 2011)
captain_america_1: Movie = Movie("Captain America: The First Avenger", 1941.1, 2011)
avengers_1: Movie = Movie("The Avengers", 2012.1, 2012)
iron_man_3: Movie = Movie("Iron Man 3", 2012.2, 2012)
thor_2: Movie = Movie("Thor: The Dark World", 2013.1, 2013)
captain_america_2: Movie = Movie("Captain America: The Winter Soldier", 2014.1, 2014)
guardians_of_the_galaxy: Movie = Movie("Guardians of the Galaxy", 2014.2, 2014)
avengers_2: Movie = Movie("Avengers: Age of Ultron", 2015.1, 2015)
ant_man_1: Movie = Movie("Ant-Man", 2015.2, 2015)
captain_america_3: Movie = Movie("Captain America: Civil War", 2016.1, 2016)
doctor_strange: Movie = Movie("Doctor Strange", 2016.4, 2016)
guardians_of_the_galaxy_2: Movie = Movie("Guardians of the Galaxy Vol. 2", 2014.3, 2017)
spider_man_1: Movie = Movie("Spider-Man: Homecoming", 2016.3, 2017)
thor_3: Movie = Movie("Thor: Ragnarok", 2017.1, 2017)
black_panther: Movie = Movie("Black Panther", 2017.1, 2017)
avengers_3: Movie = Movie("Avengers: Infinity War", 2018.2, 2018)
ant_man_2: Movie = Movie("Ant-Man and the Wasp", 2018.1, 2018)
captain_marvel: Movie = Movie("Captain Marvel", 1995.1, 2019)
avengers_4: Movie = Movie("Avengers: Endgame", 2023.1, 2019)
spider_man_2: Movie = Movie("Spider-Man: Far From Home", 2024.1, 2019)

all_movies.append(iron_man_1)
all_movies.append(hulk)
all_movies.append(iron_man_2)
all_movies.append(thor_1)
all_movies.append(captain_america_1)
all_movies.append(avengers_1)
all_movies.append(iron_man_3)
all_movies.append(thor_2)
all_movies.append(captain_america_2)
all_movies.append(guardians_of_the_galaxy)
all_movies.append(avengers_2)
all_movies.append(ant_man_1)
all_movies.append(captain_america_3)
all_movies.append(doctor_strange)
all_movies.append(guardians_of_the_galaxy_2)
all_movies.append(spider_man_1)
all_movies.append(thor_3)
all_movies.append(black_panther)
all_movies.append(avengers_3)
all_movies.append(ant_man_2)
all_movies.append(captain_marvel)
all_movies.append(avengers_4)
all_movies.append(spider_man_2)