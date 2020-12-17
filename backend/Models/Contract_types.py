from Models.model import Model


class Contract_Types(Model):
    KEY = 'type_id'

    def post(self, contract):
        sql = "INSERT INTO contract_types (contract) VALUES(%s);"
        self.cursor.execute(sql, (contract))
        self.conn.commit()
        return "Le type à bien été ajoutée"

    def put(self, contract, id):
        sql = "UPDATE jobboard.contract_types SET contract = %s WHERE type_id = %s"
        self.cursor.execute(sql, (contract, id))
        self.conn.commit()
        return "Le type à bien été modifié"