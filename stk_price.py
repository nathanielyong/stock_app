from flask_restful import Resource
from flask import request, abort
import sqlite3




class StkPrice(Resource):
    TABLE_NAME = 'stk_price'

    @staticmethod
    def get(stk):
        conn = sqlite3.connect("stk.db")
        cursor = conn.cursor()
        query = ("""SELECT stk_price.*, stk.stk_name 
                FROM stk_price
                INNER JOIN stk ON stk_price.stk = stk.stk 
                WHERE stk_price.stk=? 
                ORDER BY stk_date DESC
                """)
        result = cursor.execute(query, (stk,))
        row = result.fetchmany(25)
        conn.close()

        stk_list = []

        for row in result:
            stk_list.append({'stk_price': {'exch': row[0], 'stk': row[1], 'stk_date': row[2], 'open_price': float(row[3]), 'high_price': float(
                row[4]), 'low_price': float(row[5]), 'close_price': float(row[6]), 'volume': row[7], 'stk_name': row[8]}})

        return {'stk_list': stk_list}


class StkPriceDate(Resource):
    TABLE_NAME = 'stk_price'

    @staticmethod
    def get(stk):
        period1 = request.args.get('period1', type=str)
        period2 = request.args.get('period2', type=str)

        if not (period1 and period2):
            abort(400)

        conn = sqlite3.connect("stk.db")
        cursor = conn.cursor()
        query = (f"""SELECT stk_price.*, stk.stk_name 
                FROM stk_price
                INNER JOIN stk ON stk_price.stk = stk.stk 
                WHERE (stk_price.stk=? AND stk_date >= '{period1}' and stk_date <= '{period2}')
                ORDER BY stk_date DESC
                """)
        result = cursor.execute(query, (stk,))
        conn.close()
        
        stk_list = []

        for row in result:
            stk_list.append({'stk_price': {'exch': row[0], 'stk': row[1], 'stk_date': row[2], 'open_price': float(row[3]), 'high_price': float(
                row[4]), 'low_price': float(row[5]), 'close_price': float(row[6]), 'volume': row[7], 'stk_name': row[8]}})

        return {'stk_list': stk_list}
