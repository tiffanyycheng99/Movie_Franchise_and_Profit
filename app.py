import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
from flask import Flask

eng = create_engine("postgresql://postgres:postgres@movie-swear-db.cfgivq9r1u3j.us-west-2.rds.amazonaws.com:5432/moviesweardb")
con = eng.connect()
Base = automap_base()
Base.prepare(eng, reflect=True)
movieSwear = Base.classes.movieSwear

session = Session(eng)

app = Flask(__name__)

@app.route("/")
def home():
        return (f"Welcome to the Data of Movies and Swear Words.<br/><br/>"
                "Available Route:<br/>" 
                "/api/v1.0/get_movie_swear<br/>")

@app.route("/api/v1.0/get_movie_swear")
def get_movie_swear():
        session = Session(eng)
        results = session.execute('SELECT * FROM "movieSwear"')
        response = [dict(row.items()) for row in results]
        all_results = json.dumps(response)

        session.close()
        movie_swear_json = all_results
        return(movie_swear_json)

if __name__ == '__main__':
    app.run(debug=True)