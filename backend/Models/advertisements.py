from Models.model import Model


class Advertisements(Model):
    KEY = 'advertisement_id'

    def get_all_elements(self):
        sql = "SELECT a.advertisement_id, contract_types.contract, a.wages, a.title, a.description, a.is_valid, a.formation, a.experience, " \
          "a.sector, cities.city_name AS city_name, countries.name AS country_name, companies.title AS company_name " \
          "FROM advertisements a INNER JOIN cities cities ON cities.city_id = a.city_id INNER JOIN " \
          "countries countries ON cities.country_id = countries.country_id INNER JOIN companies companies ON " \
          "companies.company_id = a.company_id INNER JOIN contract_types ON contract_types.type_id = a.contract_type_id"
        self.cursor.execute(sql)
        elements = self.cursor.fetchall()
        return elements

    def post(self, title, description, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation):
        sql = "INSERT INTO advertisements (title, description, is_valid, company_id, city_id, start_date, add_date, " \
            "sector, contract_type_id, experience, formation) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.cursor.execute(sql, (title, description, False, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation))
        self.conn.commit()
        return "The advertisement has been added"

    def patch(self, title, description, is_valid, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation, advertisement_id):
        sql = "UPDATE advertisements SET title=%s, description=%s, is_valide=%s, company_id=%s, city_id=%s, " \
              "start_date=%s, add_date=%s, sector=%s, contract_type_id=%s, experience=%s, " \
              "formation=%s WHERE advertisement_id=%s;"
        self.cursor.execute(sql, (title, description, is_valid, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation, advertisement_id))
        self.conn.commit()
        return "The advertisement has been updated"
