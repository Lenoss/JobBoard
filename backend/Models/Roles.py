from Models.model import Model


class Roles(Model):
    KEY = 'role_id'

    def post(self, title):
        sql = "INSERT INTO roles (title) VALUES(%s);"
        self.cursor.execute(sql, (title))
        self.conn.commit()
        return "Le role à bien été ajouté"

    def put(self, title, id):
        sql = "UPDATE roles SET title=%s WHERE role_id=%s;"
        self.cursor.execute(sql, (title, id))
        self.conn.commit()
        return "Le role à bien été modifié"