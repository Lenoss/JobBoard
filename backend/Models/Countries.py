from Models.model import Model


class Countries(Model):
    KEY = 'country_id'

    def post(self, name):
        sql = "INSERT INTO countries (name) VALUES(%s);"
        self.cursor.execute(sql, (name))
        self.conn.commit()
        return "Le pays à bien été ajouté"

    def patch(self, name, id):
        sql = "UPDATE countries SET name= %s WHERE country_id= %s;"
        self.cursor.execute(sql, (name, id))
        self.conn.commit()
        return "Le pays à bien été modifié"