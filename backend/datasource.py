import psycopg2
import getpass

class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

    def __init__(self):
        pass

    def getBestPicture(self, year):
        '''
        Returns a list of all of the Best Picture winners from the specified starting year until the specified ending year.

        PARAMETERS:
            year

        RETURN:
            a string value of the Best Picture winner for the specified year
        '''
        return ""

    def getBestPicNoms(self, picture):
        '''
        Returns an integer value of the number of nominations that the Best Picture winner earned.

        PARAMETERS:
            picture

        RETURN:
            Integer value for number of nominations earned
        '''
        return 0

    def getBestPicRating(self, picture):
        '''
        Returns an integer value of the IMDb rating of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            Integer value of IMDb rating of Best Picture winner.
        '''
        return 0

	def getBestPicDuration(self, picture):
        '''
        Returns an integer value of the running time of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            Integer value of running time of Best Picture winner.
        '''
        return 0

	def getBestPicRating(self, picture):
        '''
        Returns a float value of the IMDb rating of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            Float value of IMDb rating of Best Picture winner.
        '''
        return 0.

	def getBestPicGenre(self, picture):
        '''
        Returns a string value of the genre of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            String of genre of IMDb rating of Best Picture winner.
        '''
        return ""

	def getBestPicSubgenre(self, picture):
        '''
        Returns a string value of the subgenre of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            String value of subgenre of Best Picture winner.
        '''
        return ""

	def getBestPicRelease(self, picture):
        '''
        Returns month of release of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            String value of release month of Best Picture winner.
        '''
        return ""

	def getBestPicCriticScore(self, picture):
        '''
        Returns integer value of the Metacritic rating of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            Integer value of Metacritic rating of Best Picture winner.
        '''
        return 0

	def getBestPicSynopsis(self, picture):
        '''
        Returns a string value of the synopsis of the Best Picture winner.

        PARAMETERS:
            picture

        RETURN:
            String value of synopsis of Best Picture winner.
        '''
        return ""

	def getBestActorPic(self, year):
        '''
        Returns a string value of the Best Actor winning film in given year.

        PARAMETERS:
            year

        RETURN:
            String value of name of film that won Best Actor in the given year.
        '''
        return ""

	def getBestActorName(self, year):
        '''
        Returns a string value of the Best Actor in given year.

        PARAMETERS:
            year

        RETURN:
            String value of name of actor who won Best Actor in the given year.
        '''
        return ""

	def getBestActorPicRating(self, actorFilm):
        '''
        Returns a float value of the IMDb rating of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            Float value of IMDb rating.
        '''
        return 0

	def getBestActorPicDuration(self, actorFilm):
        '''
        Returns an int value of the duration of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            Int value of duration.
        '''
        return 0

	def getBestActorPicGenre(self, actorFilm):
        '''
        Returns a string value of the genre of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            String value of genre.
        '''
        return ""

	def getBestActorPicSubgenre(self, actorFilm):
        '''
        Returns a string value of the subgenre of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            String value of subgenre.
        '''
        return ""

	def getBestActorPicReleaseMonth(self, actorFilm):
        '''
        Returns a string value of the release month of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            String value of release month.
        '''
        return ""

	def getBestActorPicCriticScore(self, actorFilm):
        '''
        Returns an int value of the Metacritic score of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            Int value of Metacritic score.
        '''
        return 0

	def getBestActorPicSynopsis(self, actorFilm):
        '''
        Returns a string value of the synopsis of the Best Actor winning film.

        PARAMETERS:
            actorFilm

        RETURN:
            String value of synposis.
        '''
        return ""

	def getBestActressPic(self, year):
        '''
        Returns a string value of the Best Actress winning film.

        PARAMETERS:
            year

        RETURN:
            String value of Best Actress winning film for the specified year.
        '''
        return ""

	def getBestActressName(self, year):
        '''
        Returns a string value of the name of the Best Actress winning actress.

        PARAMETERS:
            year

        RETURN:
            String value of name of Best Actress winning actress.
        '''
        return ""

	def getBestActressRating(self, actressFilm):
        '''
        Returns a float value of the IMDb rating of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            Float value of Best Actress winning film.
        '''
        return 0

	def getBestActressPicDuration(self, actressFilm):
        '''
        Returns a int value of the duration of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            Int value of duration of Best Actress winning film.
        '''
        return 0

	def getBestActressPicGenre(self, actressFilm):
        '''
        Returns a string value of the genre of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            String value of genre of the Best Actress winning film.
        '''
        return ""

	def getBestActressPicSubgenre(self, actressFilm):
        '''
        Returns a string value of the subgenre of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            String value of subgenre of Best Actress winning film.
        '''
        return ""

	def getBestActressPicReleaseMonth(self, actressFilm):
        '''
        Returns a string value of the month of release of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            String value of month of release.
        '''
        return ""

	def getBestActressCriticScore(self, actressFilm):
        '''
        Returns a int value of the Metacritic score of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            Int value of Metacritic score.
        '''
        return 0

	def getBestActressPicSynopsis(self, actressFilm):
        '''
        Returns a string value of the synopsis of the Best Actress winning film.

        PARAMETERS:
            actressFilm

        RETURN:
            String value of synposis.
        '''
        return ""

	def getBestDirectorPic(self, year):
        '''
        Returns a string value of the Best Director winning film for a specified year.

        PARAMETERS:
            year

        RETURN:
            String value of Best Director winning film for specific year.
        '''
        return ""

	def getBestDirectorName(self, year):
        '''
        Returns a string value of the name of the Best Director for a specific year.

        PARAMETERS:
            year

        RETURN:
            String value of Best Director for a specific year.
        '''
        return ""

	def getBestDirectorPicRating(self, directorFilm):
        '''
        Returns a float value of the IMDb rating of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            Float value of IMDb rating of Best Director winning film.
        '''
        return 0

	def getBestDirectorPicDuration(self, directorFilm):
        '''
        Returns a int value of the duration of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            Int value of duration of Best Director winning film.
        '''
        return 0

	def getBestDirectorPicGenre(self, directorFilm):
        '''
        Returns a string value of the genre of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            String value of genre.
        '''
        return ""

	def getBestDirectorPicSubgenre(self, directorFilm):
        '''
        Returns a string value of the subgenre of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            String value of subgenre.
        '''
        return ""

	def getBestDirectorPicReleaseMonth(self, directorFilm):
        '''
        Returns a string value of the month of release of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            String value of month of release.
        '''
        return ""

	def getBestDirectorPicCriticScore(self, directorFilm):
        '''
        Returns a int value of the Metacritic score of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            Int value of Metacritic score.
        '''
        return 0

	def getBestDirectorPicSynopsis(self, directorFilm):
        '''
        Returns a string value of the synopsis of the Best Director winning film.

        PARAMETERS:
            directorFilm

        RETURN:
            String value of synposis.
        '''
        return ""

	
