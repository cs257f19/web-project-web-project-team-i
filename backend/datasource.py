# imdb and critic score naming
# exeption return None or exit()
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
                    print(self.execute_query(connection, query))
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

    # def get_avgScore(self, connection, start, end):


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
                # print(pictureArray)
                for picture in pictureArray:
                    # print(picture)
                    if "'" in picture:
                        genre = genre
                        # continue
                    else:
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
        samples = ['Drama', 'Sport', 'History', 'Comedy', 'Biography', 'Crime', 'Adventure', 'Action', 'Western', 'Musical', 'Romance', 'Thriller', 'Mystery', 'Sci-Fi', 'Family']
        counts = []
        for sample in samples:
            counts.append([sample, 0])
        for genre in genres:
            for count in counts:
                if genre == count[0]:
                    count[1] += 1
        return counts

    # def count_nominations(sef, connection, picture):
    #     movies = []
    #     try:
    #         query = "SELECT COUNT(*) FROM winners WHERE picture = " + picture + " OR bestActor = " + picture + " OR bestActress = " + picture + " OR bestDirector = " + picture
    #         result = self.execute_query(connection, query)


    #     except Exception as e:
    #         print("Connection error: ", e)
    #         return None

    #     return genres


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

    result_winner = ds.get_winner(connection, year, category)
    # results.append(["result_winner", result_winner])
    # result_film = ds.get_by_year(connection, year, category)
    # results.append(["result_film", result_film])
    result_item = ds.get_by_picture(connection, item, film)
    # results.append(["result_item", result_item])
    # result_pictures = ds.get_pictures(connection, 1927, 2018)
    # results.append(["result_pictures", result_pictures])
    
    # pictures = result_pictures
    # result_genre = ds.get_genre(connection, pictures)
    # results.append(["result_genre", result_genre])
    
    # result_count = ds.count_genre(connection, result_genre)
    # results.append(["result_count", result_count])
    
    for result in results:
        if result is not None:
            print("Query results: " + str(result[0]) +  str(result[1]))
        else:
            print("The result was None.")
    
    connection.close()

if __name__ == "__main__":
    main()