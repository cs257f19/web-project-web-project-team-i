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

        Returns: a database connection.
        
        Note: exits if a connection cannot be established.
        '''
        try:
            connection = psycopg2.connect(host = "localhost",database=user, user=user, password=password)

        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def execute_query(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as e:
            print("Connection error: ", e)
            return None
        return result
            


    def get_winner(self, connection, year, category):
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

            query = "SELECT " + award + person + " FROM winners WHERE yearOfRelease = " + str(year)
            result = self.execute_query(connection, query)
        
        except Exception as e:
            print("Connection error: ", e)
            return None

        return result



    def get_by_year(self, connection, year, category):
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
            print(query)
            picture = self.execute_query(connection, query)

            item = "all_items"
            print(picture, item)
            result = self.get_by_picture(connection, item, picture)
        
        except Exception as e:
            print("Connection error: ", e)
            return None

        return result




    def get_by_picture(self, connection, item, picture):
        '''
        Returns a xxxxxxxxxxx.

        PARAMETERS:
            int xxxxxxxxxxxx

        RETURN:
            String xxxxxxxxxxxxxxx.
        '''
        try:
            if item == "all_items":
                item = "*"
            query = "SELECT " + item + " FROM films WHERE picture = '"  + picture + "'"
            result = self.execute_query(connection, query)


        except Exception as e:
            print("Connection error: ", e)
            return None

        return result



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


    for result in results:
        if result is not None:
            print("Query results: " + str(result[0]) +  str(result[1]))
        else:
            print("The result was None.")

    connection.close()

if __name__ == "__main__":
    main()
