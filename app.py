import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
from flask import Flask, jsonify, render_template

database_path = 'Resources/movie_swears.db'
engine = create_engine(f'sqlite:///{database_path}')
Base = automap_base()
Base.prepare(engine, reflect=True)
movie_swear = Base.classes.movie_swear

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
        session = Session(engine)
        results = session.execute("SELECT * FROM movie_swear")
        response = [dict(row.items()) for row in results]
        all_results = json.dumps(response)

        session.close()
        movie_swear_json = all_results
        return(movie_swear_json)

if __name__ == '__main__':
    app.run(debug=True)