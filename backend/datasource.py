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

        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def getBestPicture(self, connection, year):
        '''
        Returns a list of all of the Best Picture winners from the specified year

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            a string value of the Best Picture winner for the specified year
        '''

        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT picture FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            picture = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return picture



    def getBestPicAvgRating(self, connection, start=0, end=0):
        '''
        Returns a float of the average IMDB rating of Best Picture Winners from the specified starting year until the specified ending year

        PARAMETERS:
            int start = starting year, obtained from yearOfRelease column of SQL table
			int end = ending year, obtained from yearOfRelease column of SQL table

        RETURN:
            float value of the average IMDB Rating of Best Picture winner for the specified year range
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT rating FROM movies WHERE yearOfRelease BETWEEN "  + str(start) + " AND " + str(end)
            cursor.execute(query)
            ratings = cursor.fetchall()

            total = 0.0
            for rating in ratings[0]:
                total += rating

            avgRating = total / (len(ratings)+1)

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return avgRating

    def getBestPicAvgScore(self, connection, start=0, end=0):
        '''
        Returns a float of the average Metacritic score of Best Picture Winners from the specified starting year until the specified ending year

        PARAMETERS:
            start = starting year, obtained from yearOfRelease column of SQL table
            end = ending year, obtained from yearOfRelease column of SQL table

        RETURN:
            float value of the average Metacritic score of Best Picture winner for the specified year range
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT	criticScore FROM movies WHERE yearOfRelease BETWEEN " + str(start) + " AND " + str(end)
            cursor.execute(query)
            scores = cursor.fetchall()

            total = 0.0
            for score in scores[0]:
                if score == 0:
                    return "The value was not found."
                else:
                    total += score

            avgScore = total / (len(scores[0]) + 1)

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return avgScore

    def getBestPicNoms(self, connection, picture):
        '''
        Returns an integer value of the number of nominations that the Best Picture winner earned.

        PARAMETERS:
            String picture, obtained from picture column in SQL table

        RETURN:
            Integer value for number of nominations earned
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT nominations FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            nominations = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return nominations

    def getBestPicRating(self, connection, picture):
        '''
        Returns an integer value of the IMDb rating of the Best Picture winner

        PARAMETERS:
            String picture, obtained from picture column of SQL table

        RETURN:
            Integer value of IMDb rating of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT rating FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            rating = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return rating


    def getBestPicDuration(self, connection, picture):
        '''
        Returns an integer value of the running time of the Best Picture winner.

        PARAMETERS:
            String picture, obtained from picture column of SQL table

        RETURN:
            Integer value of running time of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT duration FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            duration = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return duration

    def getBestPicGenre(self, connection, picture):
        '''
        Returns a string value of the genre of the Best Picture winner.

        PARAMETERS:
            String picture, obtained from picture column of SQL table

        RETURN:
            String of genre of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT genre FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            genre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return genre

    def getBestPicSubgenre(self, connection, picture):
        '''
        Returns a string value of the subgenre of the Best Picture winner.

        PARAMETERS:
            String picture, obtained from picture column of SQL table

        RETURN:
            String value of subgenre of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT subgenre FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            subgenre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return subgenre

    def getBestPicRelease(self, connection, picture):
        '''
        Returns month of release of the Best Picture winner.

        PARAMETERS:
            Stirng picture, obtained from picture column of SQL table

        RETURN:
            String value of release month of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT releaseMonth FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            month = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return month

    def getBestPicCriticScore(self, connection, picture):
        '''
        Returns integer value of the Metacritic rating of the Best Picture winner.

        PARAMETERS:
            String picture, obtained from picture column of SQL table.

        RETURN:
            Integer value of Metacritic rating of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT criticScore FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            score = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return score

    def getBestPicSynopsis(self, connection, picture):
        '''
        Returns a string value of the synopsis of the Best Picture winner.

        PARAMETERS:
            String picture, obtained from picture column of SQL table

        RETURN:
            String value of synopsis of Best Picture winner.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT synopsis FROM movies WHERE picture = '" + picture + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            synopsis = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return synopsis

    def getBestActorPic(self, connection, year):
        '''
        Returns a string value of the Best Actor winning film in given year.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of name of film that won Best Actor in the given year.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	actorFilm FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            title = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return title

    def getBestActorName(self, connection, year):
        '''
        Returns a string value of the Best Actor in given year.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of name of actor who won Best Actor in the given year.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	actorName FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            actor = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return actor

    def getBestActorPicRating(self, connection, actorFilm):
        '''
        Returns a float value of the IMDb rating of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            Float value of IMDb rating.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorRating FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            rating = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return rating

    def getBestActorPicDuration(self, connection, actorFilm):
        '''
        Returns an int value of the duration of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            Int value of duration.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorDuration FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            duration = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return duration

    def getBestActorPicGenre(self, connection, actorFilm):
        '''
        Returns a string value of the genre of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            String value of genre.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorGenre FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            genre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return genre

    def getBestActorPicSubgenre(self, connection, actorFilm):
        '''
        Returns a string value of the subgenre of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            String value of subgenre.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorSubgenre FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            subgenre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return subgenre

    def getBestActorPicReleaseMonth(self, connection, actorFilm):
        '''
        Returns a string value of the release month of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            String value of release month.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorReleaseMonth FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            month = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return month

    def getBestActorPicCriticScore(self, connection, actorFilm):
        '''
        Returns an int value of the Metacritic score of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            Int value of Metacritic score.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorCriticScore FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            score = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return score

    def getBestActorPicSynopsis(self, connection, actorFilm):
        '''
        Returns a string value of the synopsis of the Best Actor winning film.

        PARAMETERS:
            String actorFilm, obtained from actorFilm column of SQL table

        RETURN:
            String value of synposis.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actorSynopsis FROM movies WHERE actorFilm = '" + actorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            synopsis = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return synopsis

    def getBestActressPic(self, connection, year):
        '''
        Returns a string value of the Best Actress winning film.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of Best Actress winning film for the specified year.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	actressFilm FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            title = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return title

    def getBestActressName(self, connection, year):
        '''
        Returns a string value of the name of the Best Actress winning actress.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of name of Best Actress winning actress.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	actressName FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            actress = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return actress

    def getBestActressRating(self, connection, actressFilm):
        '''
        Returns a float value of the IMDb rating of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            Float value of Best Actress winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressRating FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            rating = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return rating

    def getBestActressPicDuration(self, connection, actressFilm):
        '''
        Returns a int value of the duration of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            Int value of duration of Best Actress winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressDuration FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            duration = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return duration

    def getBestActressPicGenre(self, connection, actressFilm):
        '''
        Returns a string value of the genre of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            String value of genre of the Best Actress winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressGenre FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            genre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return genre

    def getBestActressPicSubgenre(self, connection, actressFilm):
        '''
        Returns a string value of the subgenre of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            String value of subgenre of Best Actress winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressSubgenre FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            subgenre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return subgenre

    def getBestActressPicReleaseMonth(self, connection, actressFilm):
        '''
        Returns a string value of the month of release of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            String value of month of release.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressReleaseMonth FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            month = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return month

    def getBestActressCriticScore(self, connection, actressFilm):
        '''
        Returns a int value of the Metacritic score of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            Int value of Metacritic score.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressCriticScore FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            score = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return score

    def getBestActressPicSynopsis(self, connection, actressFilm):
        '''
        Returns a string value of the synopsis of the Best Actress winning film.

        PARAMETERS:
            String actressFilm, obtained from actressFilm column of SQL table

        RETURN:
            String value of synposis.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT actressSynopsis FROM movies WHERE actressFilm = '" + actressFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            synopsis = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return synopsis

    def getBestDirectorPic(self, connection, year):
        '''
        Returns a string value of the Best Director winning film for a specified year.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of Best Director winning film for specific year.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	directorFilm FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            title = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return title

    def getBestDirectorName(self, connection, year):
        '''
        Returns a string value of the name of the Best Director for a specific year.

        PARAMETERS:
            int year, obtained from yearOfRelease column of SQL table

        RETURN:
            String value of Best Director for a specific year.
        '''
        yearOfRelease = year - 1

        try:
            cursor = connection.cursor()
            query = "SELECT	directorFilm FROM movies WHERE yearOfRelease = "  + str(yearOfRelease)
            cursor.execute(query)
            result = cursor.fetchall()
            director = str(result[0])


        except:
            msg = "Something went wrong when executing the query."
            return msg

        return director

    def getBestDirectorPicRating(self, connection, directorFilm):
        '''
        Returns a float value of the IMDb rating of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            Float value of IMDb rating of Best Director winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorRating FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            rating = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return rating

    def getBestDirectorPicDuration(self, connection, directorFilm):
        '''
        Returns a int value of the duration of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            Int value of duration of Best Director winning film.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorDuration FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            duration = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return duration

    def getBestDirectorPicGenre(self, connection, directorFilm):
        '''
        Returns a string value of the genre of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            String value of genre.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorGnere FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            genre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return genre

    def getBestDirectorPicSubgenre(self, connection, directorFilm):
        '''
        Returns a string value of the subgenre of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            String value of subgenre.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorSugenre FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            subgenre = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return subgenre

    def getBestDirectorPicReleaseMonth(self, connection, directorFilm):
        '''
        Returns a string value of the month of release of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            String value of month of release.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorReleaseMonth FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            month = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return month

    def getBestDirectorPicCriticScore(self, connection, directorFilm):
        '''
        Returns a int value of the Metacritic score of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            Int value of Metacritic score.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorCriticScore FROM movies WHERE directorFilm = '" + directorFilm + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            score = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return score

    def getBestDirectorPicSynopsis(self, connection, directorFilm):
        '''
        Returns a string value of the synopsis of the Best Director winning film.

        PARAMETERS:
            String directorFilm, obtained from directorFilm column of SQL table

        RETURN:
            String value of synposis.
        '''
        try:
            cursor = connection.cursor()
            query = "SELECT directorSynopsis FROM movies WHERE directorFilm='" + directorFilm + "'"
            print(query)
            cursor.execute(query)
            print('query done')
            result = cursor.fetchall()
            print(result)
            synopsis = result[0]

        except:
            msg = "Something went wrong when executing the query."
            return msg

        return synopsis



def main():
    ds = DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    results = []

    year = 2000
    picture = 'Gladiator'

    start = 2000
    end = 2010

    results.append(['picture', ds.getBestPicture(connection, year)])
    results.append(['avgRating', ds.getBestPicAvgRating(connection, start, end)])
    results.append(['avgScore', ds.getBestPicAvgScore(connection, start, end)])
    results.append(['nominations', ds.getBestPicNoms(connection, picture)])
    results.append(['rating', ds.getBestPicRating(connection, picture)])
    results.append(['duration', ds.getBestPicDuration(connection, picture)])
    results.append(['genre', ds.getBestPicGenre(connection, picture)])
    results.append(['subgenre', ds.getBestPicSubgenre(connection, picture)])
    results.append(['critic score', ds.getBestPicCriticScore(connection, picture)])
    results.append(['synopsis', ds.getBestPicSynopsis(connection, picture)])

    actorPicture = ' American Beauty'

    results.append(['best actor picture', ds.getBestActorPic(connection, year)])
    results.append(['best actor name', ds.getBestActorName(connection, year)])
    results.append(['best actor rating', ds.getBestActorPicRating(connection, actorPicture)])
    results.append(['best actor duration', ds.getBestActorPicDuration(connection, actorPicture)])
    results.append(['best actor genre', ds.getBestActorPicGenre(connection, actorPicture)])
    results.append(['best actor subgenre', ds.getBestActorPicSubgenre(connection, actorPicture)])
    results.append(['best actor critic score', ds.getBestActorPicCriticScore(connection, actorPicture)])
    results.append(['best actor synopsis', ds.getBestActorPicSynopsis(connection, actorPicture)])

    # actressPicture = " Boys Don't Cry"

    # results.append(['best actress picture', ds.getBestActressPic(connection, year)])
    # results.append(['best actress name', ds.getBestActressName(connection, year)])
    # results.append(['best actress rating', ds.getBestActressRating(connection, actressPicture)])
    # results.append(['best actress duration', ds.getBestActressPicDuration(connection, actressPicture)])
    # results.append(['best actress genre', ds.getBestActressPicGenre(connection, actressPicture)])
    # results.append(['best actress subgenre', ds.getBestActressPicSubgenre(connection, actressPicture)])
    # results.append(['best actress critic score', ds.getBestActressCriticScore(connection, actressPicture)])
    # results.append(['best actress synopsis', ds.getBestActressPicSynopsis(connection, actressPicture)])

    # dirPicture = ' Gravity'

    # results.append(['best director picture', ds.getBestDirectorPic(connection, year)])
    # results.append(['best director name', ds.getBestDirectorName(connection, year)])
    # results.append(['best director rating', ds.getBestDirectorPicRating(connection, dirPicture)])
    # results.append(['best director duration', ds.getBestDirectorPicDuration(connection, dirPicture)])
    # results.append(['best director genre', ds.getBestDirectorPicGenre(connection, dirPicture)])
    # results.append(['best director subgenre', ds.getBestDirectorPicSubgenre(connection, dirPicture)])
    # results.append(['best director critic score', ds.getBestDirectorPicCriticScore(connection, dirPicture)])
    # results.append(['best director synopsis', ds.getBestDirectorPicSynopsis(connection, dirPicture)])

    for result in results:
        if result[1] is not None:
	        print("Query results of " + result[0] + ": " +  str(result[1]))
        else:
            print("The result was None.")

    connection.close()

if __name__ == "__main__":
    main()
