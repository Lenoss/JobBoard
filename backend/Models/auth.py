from Models.model import Model


class Auth(Model):
    KEY = 'user_id'

    def findbyname(self, username):
        sql = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(sql, username)
        elements = self.cursor.fetchall()
        return elements

    def register(self, username, email, password):
        sql = "INSERT INTO users (username, email, password, role_id) VALUES(%s, %s, %s, %s);"
        self.cursor.execute(sql, username, email, password, 1 )
        self.conn.commit()
        return "New user has been added"

    def login (self, user, password):
        pass