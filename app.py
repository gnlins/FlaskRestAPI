from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

initialized = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def cria_banco():
    global initialized
    print('cria_banco out :', initialized)
    if not initialized:
        banco.create_all()
        initialized = True
        print('cria_banco inside', initialized)

# @app.before_first_request
# def cria_banco():
#     banco.create_all()

# with app.app_context():
#     banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
