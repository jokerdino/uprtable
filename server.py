from flask import Flask
from flask_migrate import Migrate

#from waitress import server

from model import Uprtable, db

import views

migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object("settings")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://barneedhar:barneedhar@localhost:5432/upr"
    
    app.add_url_rule("/", view_func=views.home_page, methods = ["GET","POST"])
    app.add_url_rule("/upload", view_func=views.upload, methods=["POST", "GET"])
    app.add_url_rule("/api/data/", view_func=views.data, methods=['GET','POST'])
  #  app.add_url_rule("/api/data/<string:period>", view_func=views.data, methods=['GET','POST'])
    app.add_url_rule("/view/", view_func=views.query_data, methods=['GET',"POST"])
    db.init_app(app)
    migrate.init_app(app, db)
    return app
    
if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
