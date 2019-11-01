import psycopg2
import getpass

class DataSource:
    def __init__(self):
        pass

    def connect(self, user, password):
        '''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: a database connection.

		Note: exits if a connection cannot be established.
		'''
        try:
            connection = psycopg2.connect(host = "localhost",database='kuritar', user=user, password=password)
            # cur = connection.cursor()

        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
        # finally:
        #     if connection is not None:
        #         connection.close()
        #         print("Database connection closed.")
        # return connection
        #Make connection an instance variable

    # def disconnect(self):
    #     connection.close()



    def getBestPicture(self, connection, year):
        '''
        Returns a list of all of the Best Picture winners from the specified starting year until the specified ending year.

        PARAMETERS:
            year

        RETURN:
            a string value of the Best Picture winner for the specified year
        '''

        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            print(yearOfRelease, "jjj")
            query = "SELECT	picture FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            print(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            picture = result[0]


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return picture



    def getBestPicAvgRating(self, start=0, end=0):
        '''
        Returns a float of the average IMDB rating of Best Picture Winners from the specified starting year until the specified ending year.

        PARAMETERS:
            start = starting year
			end = ending year

        RETURN:
            float value of the average IMDB Rating of Best Picture winner for the specified year range
        '''
        try:
            cursor = self.connection.cursor()
            query = "SELECT	rating FROM movies WHERE yearOfRelease BETWEEN "  + start + " AND " + end
            cursor.execute(query)
            ratings = cursor.fetchall()

            total = 0.0
            for rating in ratings:
                total += rating

            avgRating = total / (len(ratings)+1)

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return avgRating

    def getBestPicAvgScore(self, start=0, end=0):
        '''
                Returns a float of the average Metacritic score of Best Picture Winners from the specified starting year until the specified ending year.

                PARAMETERS:
                    start = starting year
                    end = ending year

                RETURN:
                    float value of the average Metacritic score of Best Picture winner for the specified year range
                '''
        try:
            cursor = connection.cursor()
            query = "SELECT	criticScore FROM movies WHERE yearOfRelease BETWEEN " + start + " AND " + end
            cursor.execute(query)
            scores = cursor.fetchall()

            total = 0.0
            for score in scores:
                if score == 0:
                    return "The value was not found."
                else:
                    total += score

            avgScore = total / (len(scores) + 1)

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return avgScore

    def getBestPicNoms(self, picture):
        '''
        Returns an integer value of the number of nominations that the Best Picture winner earned.

        PARAMETERS:
            picture

        RETURN:
            Integer value for number of nominations earned
        '''
        try:
            cursor = connection.cursor()
            query = "SELELCT nominations FROM movies WHERE picture = "  + picture

            cursor.execute(query)
            result = cursor.fetchall()

            nominations = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return nominations

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

    # def getBestPicRating(self, picture):
    #     '''
    #     Returns a float value of the IMDb rating of the Best Picture winner.

    #     PARAMETERS:
    #         picture

    #     RETURN:
    #         Float value of IMDb rating of Best Picture winner.
    #     '''
    #     return 0

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


# def main():
# 	# Replace these credentials with your own
# 	user = 'kuritar'
# 	password = getpass.getpass()
#
# 	# Connect to the database
# 	connection = connect(user, password)
#
# 	# Execute a simple query:
# 	results = getBestPicAvgRating(connection, 1950, 1970)
#
# 	if results is not None:
# 		print("Query results: ")
# 		for item in results:
# 			print(item)
#
# 	# Disconnect from database
# 	connection.close()
    #
	# main()

def main():
    ds = DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    result = ds.getBestPicture(connection, 2000)

    if result is not None:
	    print("Query results: " + result)

    connection.close()

    # Connect to the database
    # ds = DataSource()
    # ds.connect(user, password)

    # Disconnect from database
    # ds.disconnect()


if __name__ == "__main__":
    main()
