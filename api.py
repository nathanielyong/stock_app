from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from exch import Exch, ExchList
from stk_price import StkPriceDate, StkPrice

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(Exch, '/Exch/<string:exch>')
api.add_resource(ExchList, '/ExchList')
api.add_resource(StkPrice, '/StkPrice/<string:stk>')
api.add_resource(StkPriceDate, '/StkPrice/<string:stk>/date')

if __name__ == '__main__':
    app.run(port=5000) 
