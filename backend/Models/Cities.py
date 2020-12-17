from Models.model import Model


class Cities(Model):
    KEY = 'city_id'

    def get_all_elements(self):
        sql = "SELECT cities.city_id, cities.city_name, cities.zipcode, countries.name FROM cities cities INNER JOIN countries countries on cities.country_id = countries.country_id"
        self.cursor.execute(sql)
        elements = self.cursor.fetchall()
        return elements

    def findByName(self, city_name):
        sql = "select * from cities where {} = %s"
        self.cursor.execute(sql, (city_name))
        elements = self.cursor.fetchall()
        return elements

    def post(self, city_name, country_id, zipcode):
        sql = "INSERT INTO cities (city_name, country_id, zipcode) VALUES(%s, %s, %s);"
        self.cursor.execute(sql, (city_name, country_id, zipcode))
        self.conn.commit()
        return "La ville à bien été ajoutée"

    def patch(self, city_name, country_id, zipcode, id):
        sql = "UPDATE cities SET city_name= %s, country_id= %s, zipcode= %s WHERE city_id= %s;"
        self.cursor.execute(sql, (city_name, country_id, zipcode, id))
        self.conn.commit()
        return "La ville à bien été ajoutée"