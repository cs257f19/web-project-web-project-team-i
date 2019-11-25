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

        Returns: a database connection

        Note: exits if a connection cannot be established
        '''
        try:
            connection = psycopg2.connect(host = "localhost",database=user, user=user, password=password)

        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def execute_query(self, connection, query):
        '''
        Returns a string containing the result of the query

        PARAMETERS:
            String query entered by user

        RETURN:
            String of query result
        '''
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as e:
            print("Connection error: ", e)
            return None
        return result


    def get_winner(self, connection="", year=0, category=""):
        '''
        Returns a string containing winners of the specified year and category

        PARAMETERS:
            int year for the year of release to be examined
            String category for the Oscar awards cateogry to be examined

        RETURN:
            String containing name of picture and person that won the specified category in the specified year
        '''

        try:
            if category == "picture":
                award = "bestPicture"
                person = ""
            elif category == "actor":
                award = "bestActor"
                person = ", actor"
            elif category == "actress":
                award = "bestActress"
                person = ", actress"
            elif category == "director":
                award = "bestDirector"
                person = ", director"

            if year > 1926 and year < 2019:
                get_year = ""
                year_query =  " WHERE yearOfRelease = " + str(year)
            else:
                get_year = ", yearOfRelease"
                year_query = ""


            query = "SELECT " + award + person + get_year + " FROM winners" + year_query
            result = self.execute_query(connection, query)
        except Exception as e:
            print("Connection error: ", e)
            return None

        return result



    def get_by_year(self, connection, year, category):
        '''
        Returns a string containing winning pictures for the specified year and category

        PARAMETERS:
            int year for the year of release to be examined
            String category for the Oscar awards cateogry to be examined

        RETURN:
            String containing names of pictures that won the specified category in the specified year
        '''
        try:
            if category == "picture":
                award = "bestPicture"
            elif category == "actor":
                award = "bestActor"
                person = ", actor"
            elif category == "actress":
                award = "bestActress"
                person = ", actress"
            elif category == "director":
                award = "bestDirector"
                person = ", director"


            query = "SELECT " + award + " FROM winners WHERE yearOfRelease = " + str(year)
            picture = self.execute_query(connection, query)

            item = "*"
            result = self.get_by_picture(connection, item, picture[0][0])

        except Exception as e:
            print("Connection error: ", e)
            return None

        return result




    def get_by_picture(self, connection="", item = "*", picture=""):
        '''
        Returns a string containing awards won by the specified picture.

        PARAMETERS:
            String item
            String picture for the picture to examine

        RETURN:
            String containing all the awards won by the specified picture
        '''
        try:
            if item == "genre":
                query = "SELECT subgenre FROM films WHERE picture = '"  + picture + "'"
                if self.execute_query(connection, query) != []:
                    subgenre = self.execute_query(connection, query)[0][0]
                    if subgenre == "Drama" or subgenre == "NA":
                        query = "SELECT genre FROM films WHERE picture = '"  + picture + "'"
                        genre = self.execute_query(connection, query)[0][0]
                        result = genre
                    else:
                        result = subgenre
                else:
                    query = "SELECT genre FROM films WHERE picture = '"  + picture + "'"
                    genre = self.execute_query(connection, query)[0][0]
                    result = genre

            else:
                query = "SELECT DISTINCT " + item + " FROM films WHERE picture = '"  + picture + "'"
                result = self.execute_query(connection, query)

        except Exception as e:
            print("Connection error: ", e)
            return None

        return result


    def get_pictures(self, connection, start, end):
        '''
        Returns an array containing all awarded pictures in the year range.

        PARAMETERS:
            int the beginning year of the range
            int the ending year of the range

        RETURN:
            Array containing all awarded pictures
        '''
        start = start - 1
        end = end - 1

        try:
            query = "SELECT DISTINCT bestPicture, bestActor, bestActress, bestDirector FROM winners WHERE yearOfRelease BETWEEN " + str(start) + " AND "  + str(end)
            result = self.execute_query(connection, query)

        except Exception as e:
            print("Connection error: ", e)
            return None

        return result

    def get_Score(self, connection, start, end):
        '''
        Returns an array of integers which include Metacritic scores of Best Picture winners in the year range.

        PARAMETERS:
            int the beginning year of the range
            int the ending year of the range

        RETURN:
            Array of integers of average scores of all Best Picture winners in the year range.
        '''

        start = start - 1
        scores = []
        bestPics = []
        category = "picture"


        try:
            for year in range(start, end+1):
                bestPic = self.get_winner(connection, year, category)
                bestPics.append(bestPic)
            for picture in bestPics[0]:
                picture = picture[0]
                if "'" in picture:
                    picture = picture.replace("'", "''")
                query = "SELECT score FROM films WHERE picture = '"  + picture + "'"
                score = self.execute_query(connection, query)[0][0]
                scores.append(score)

        except Exception as e:
            print("Connection error: ", e)
            return None

        return scores

    def get_avgScore(self, connection, scores):
         '''
         Returns an integer value of average Metacritic scores of Best Picture winners in the year range.

         PARAMETERS:
             scores - array of int metacritic scores

         RETURN:
             Integer of average Metacritic score of specific year range.
         '''

         total = 0.0
         for score in scores:
             total += score
         avgScore = total/len(scores)

         return round(avgScore, 1)

    def get_Rating(self, connection, start, end):
        '''
        Returns an array of integers which include IMDb ratings of Best Picture winners in the year range.

        PARAMETERS:
            int the beginning year of the range
            int the ending year of the range

        RETURN:
            Array of integers of average ratings of all Best Picture winners in the year range.
        '''

        start = start - 1
        end = end - 1
        ratings = []
        bestPics = []
        category = "picture"


        try:
            for year in range(start, end+1):
                bestPic = self.get_winner(connection, year, category)
                bestPics.append(bestPic)
            for picture in bestPics[0]:
                picture = picture[0]
                if "'" in picture:
                    picture = picture.replace("'", "''")
                query = "SELECT rating FROM films WHERE picture = '"  + picture + "'"
                rating = self.execute_query(connection, query)[0][0]
                ratings.append(rating)

        except Exception as e:
            print("Connection error: ", e)
            return None

        return ratings

    def get_avgRating(self, connection, ratings):
         '''
         Returns an integer value of average IMDb ratings of Best Picture winners in the year range.

         PARAMETERS:
             ratings - array of float IMDB ratings

         RETURN:
             Float of average IMDb rating of specific year range.
         '''

         total = 0.0
         for rating in ratings:
             total += rating

         avgRating = total/len(ratings)

         return round(avgRating, 1)

    def get_genre(self, connection, pictures):
        '''
        Returns an array of sets which include genre name and corresponding number of films in that genre within a given year.

        PARAMETERS:
            Integer the beginning year of the range
            Integer the ending year of the range

        RETURN:
            Array of sets which have genre and count
        '''
        genres = []
        try:
            for pictureArray in pictures:
                for picture in pictureArray:
                    if "'" in picture:
                        picture = picture.replace("'", "''")
                    query = "SELECT subgenre FROM films WHERE picture = '"  + picture + "'"
                    if self.execute_query(connection, query) != []:
                        subgenre = self.execute_query(connection, query)[0][0]
                        if subgenre == "Drama" or subgenre == "NA":
                            query = "SELECT genre FROM films WHERE picture = '"  + picture + "'"
                            genre = self.execute_query(connection, query)[0][0]
                            genres.append(genre)
                        else:
                            genres.append(subgenre)

        except Exception as e:
            print("Connection error: ", e)
            return None

        return genres


    def count_genre(self, connection, genres):
        '''
        Returns an integer which specifies the number of times a specific genre has won in a decade.

        PARAMETERS:
            Array of sets which have genre and count

        RETURN:
            Integer of count of number of times a specific genre has won in a decade
        '''
        samples = ['Drama', 'Sport', 'History', 'Comedy', 'Biography', 'Crime', 'Adventure', 'Action', 'Western', 'Musical', 'Romance', 'Thriller', 'Mystery', 'Sci-Fi', 'Family']
        counts = []
        for sample in samples:
            counts.append([sample, 0])
        for genre in genres:
            for count in counts:
                if genre == count[0]:
                    count[1] += 1
        return counts


def main():
    ds = DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    results = []

    film = "Green Book"
    year = 2000
    category = "actor"
    item = "genre"

    result_pictures = ds.get_pictures(connection, 1928, 2017)
    pictures = result_pictures
    result_genre = ds.get_genre(connection, pictures)
    # result_score = ds.get_Score(connection, 1927, 2018)
    # results.append(["result_score", result_score])
    # result_avgScore = ds.get_avgScore(connection, result_score)
    # results.append(["result_avgScore", result_avgScore])

    result_testScore = ds.get_Score(connection, 1927, 1929)
    results.append(["result_testScore", result_testScore])

    categories = ["picture","actor","actress","director"]
    infos = []

    for year in range(1930, 1940):
        # winners = []
        # winners.append({"award":"Award", "film":"Film", "person":"Person"})
        for category in categories:
            result = ds.get_winner(connection, year, category)
            print(year, result)

    for result in results:
        if result is not None:
            print("Query results: " + str(result[0]) +  str(result[1]))
        else:
            print("The result was None.")

    connection.close()

if __name__ == "__main__":
    main()
