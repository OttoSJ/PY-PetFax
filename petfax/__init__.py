from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFax!"

    from . import pet
    app.register_blueprint(pet.bp)
    from . import fact
    app.register_blueprint(fact.bp)
    return app

    app.config['SQLALCHENY_DATABASE_URL'] = 'postgres://postgress:Rookie121215@localhost:5432/petfax'
    app.config['SQLALCHENY_TRACK_MODIFICATIONS'] = False
