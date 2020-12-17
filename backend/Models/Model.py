from Models.connect import Connect


class Model(Connect):
    KEY = None

    def __init__(self):
        super().__init__()

    def get_all_elements(self):
        sql = f"select * from {type(self).__name__.lower()}"
        self.cursor.execute(sql)
        elements = self.cursor.fetchall()
        return elements

    def get_one_element(self, id):
        sql = f"select * from {type(self).__name__.lower()} where {self.KEY} = %s"
        print(sql)
        print(id)
        self.cursor.execute(sql, (id))
        element = self.cursor.fetchone()
        return element

    def delete_element(self, id):
        sql = f"DELETE FROM {type(self).__name__.lower()} WHERE {self.KEY} = %s;"
        self.cursor.execute(sql, (id))
        self.cursor.fetchall()
        self.conn.commit()
        return "L'élément à bien été supprimé."

