from Models.model import Model


class Companies(Model):
    KEY = 'company_id'

    def post(self, title, email, phone, user_id, logo):
        sql = "INSERT INTO companies (title, email, phone, user_id, logo) VALUES(%s, %s, %s, %s, %s);"
        self.cursor.execute(sql, (title, email, phone, user_id, logo))
        self.conn.commit()
        return "The company has been added"

    def patch(self, title, email, phone, user_id, logo, company_id):
        sql = "UPDATE companies SET title=%s, email=%s, phone=%s, user_id=%s, logo=%s WHERE company_id=%s;"
        self.cursor.execute(sql, (title, email, phone, user_id, logo, company_id))
        self.conn.commit()
        return "The company is up to date"
