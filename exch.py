from flask_restful import Resource
import sqlite3




class Exch(Resource):
    TABLE_NAME = 'exch'

    @staticmethod
    def get(exch):
        conn = sqlite3.connect("stk.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM {Exch.TABLE_NAME} WHERE exch=?"
        result = cursor.execute(query, (exch,))
        row = result.fetchone()

        conn.close()

        if row:
            return {'exch': {'exch': row[0], 'exch_name': row[1], 'currency_code': row[2]}}

        return {'message': 'Item not found'}, 404


class ExchList(Resource):
    TABLE_NAME = 'exch'

    @staticmethod
    def get():
        conn = sqlite3.connect("stk.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM {ExchList.TABLE_NAME}"
        result = cursor.execute(query)

        exch_list = []

        for row in result:
            exch_list.append(
                {'exch': {'exch': row[0], 'exch_name': row[1], 'currency_code': row[2]}})
        conn.close()

        return {'ExchList': exch_list}
