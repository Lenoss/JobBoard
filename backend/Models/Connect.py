import pymysql
import sys

class Connect:
    def __init__(self):
        self.conn = pymysql.connect(host='13.74.223.149',
                             user='asoupady',
                             password='Epitech2020!',                             
                             db='jobboard',
                             charset='utf8',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def connection(self):
        return self.conn

    def __del__(self):
        return self.conn.close()