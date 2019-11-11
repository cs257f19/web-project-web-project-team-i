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
            


    def get_year(self, connection, film, category):
        if category == "picture":
            column = "picture"
        elif category == "actor":
            column = "actor"
        elif category == "actress":
            column = "actress"
        elif category == "director":
            column = "director"

        query = "SELECT yearOfRelease FROM winners WHERE picture = '"  + film + "' AND " + column + " = " + category
        year = self.execute_query(connection, query)

        return year

    def get_picture_name(self, connection, year, category):
        '''
        Returns a xxxxxxxxxxx.

        PARAMETERS:
            int xxxxxxxxxxxx

        RETURN:
            String xxxxxxxxxxxxxxx.
        '''
        yearOfRelease = year - 1

        if category == "picture":
            column = "picture"
        elif category == "actor":
            column = "actor"
        elif category == "actress":
            column = "actress"
        elif category == "director":
            column = "director"

        query = "SELECT picture FROM winners WHERE yearOfRelease = "  + str(yearOfRelease) + " AND " + column + " = " + category
        picture = self.execute_query(connection, query)

        return picture

    def get_by_picture(self, connection, item, picture):
        '''
        Returns a xxxxxxxxxxx.

        PARAMETERS:
            int xxxxxxxxxxxx

        RETURN:
            String xxxxxxxxxxxxxxx.
        '''
        query = "SELECT	" + item + " FROM films WHERE picture = '"  + picture + "'"
        result = self.execute_query(connection, query)

        return result



def main():
    ds = DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    results = []

    film = " The Moon Light"
    year = 2000
    category = "picture"
    item = "synopsis"

    result_year = ds.get_year(connection, film, category)
    results.append(["result_year", result_year])
    result_film = ds.get_picture_name(connection, year, category)
    results.append(["result_film", result_film])    
    result_item = ds.get_by_picture(connection, item, film)
    results.append(["result_item", result_item])


    for result in results:
        if result is not None:
            print("Query results: " +  str(result[1]))
        else:
            print("The result was None.")

    connection.close()

if __name__ == "__main__":
    main()
