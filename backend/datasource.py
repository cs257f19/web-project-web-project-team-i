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
            query = "SELECT DISTINCT " + item + " FROM films WHERE picture = '"  + picture + "'"
            result = self.execute_query(connection, query)


        except Exception as e:
            print("Connection error: ", e)
            return None

        return result


    def get_pictures(self, connection, start, end):
        '''
        Returns a string containing awards won by the specified picture.

        PARAMETERS:
            String item
            String picture for the picture to examine

        RETURN:
            String containing all the awards won by the specified picture
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

    # def count_each_genre(self, connection, start, end):
    #     '''
    #     Returns an array of sets which include genre name and corresponding number of films in that genre within a given year.
        
    #     PARAMETERS:
    #         Integer the beginning year of the range
    #         Integer the ending year of the range

    #     RETURN:
    #         Array of sets which have genre and count
    #     '''

    #     try:
    #         query = "SELECT COUNT picture FROM films WHERE picture = '"  + picture + "'"
    #         result = self.execute_query(connection, query)


    #     except Exception as e:
    #         print("Connection error: ", e)
    #         return None

    #     return result        


def main():
    ds = DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    results = []

    film = "Moonlight"
    year = 2000
    category = "actor"
    item = "synopsis"

    result_winner = ds.get_winner(connection, year, category)
    results.append(["result_winner", result_winner])
    result_film = ds.get_by_year(connection, year, category)
    results.append(["result_film", result_film])
    result_item = ds.get_by_picture(connection, item, film)
    results.append(["result_item", result_item])
    result_pictures = ds.get_pictures(connection, 2000, 2018)
    results.append(["result_pictures", result_pictures])


    for result in results:
        if result is not None:
            print("Query results: " + str(result[0]) +  str(result[1]))
        else:
            print("The result was None.")

    connection.close()

if __name__ == "__main__":
    main()
