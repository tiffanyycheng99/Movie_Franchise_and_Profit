# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# import json
from flask import Flask, render_template

# eng = create_engine("postgresql://postgres:postgres@movie-swear-db.cfgivq9r1u3j.us-west-2.rds.amazonaws.com:5432/moviesweardb")
# con = eng.connect()
# Base = automap_base()
# Base.prepare(eng, reflect=True)
# movieSwear = Base.classes.movieSwear

# session = Session(eng)

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/api/v1.0/timeseries_viz")
def timeseries_viz():
        return render_template("timeseries_viz.html")

@app.route("/api/v1.0/contentrating_viz")
def contentrating_viz():
        return render_template("contentrating_viz.html")

@app.route("/api/v1.0/content_rating_ML")
def content_rating_ML():
        return render_template("content_rating_ML.html")

@app.route("/api/v1.0/breakeven_ML")
def breakeven_ML():
        return render_template("breakeven_ML.html")

@app.route("/api/v1.0/bonus_visuals")
def bonus_visuals():
        return render_template("bonus_visuals.html")

if __name__ == '__main__':
    app.run(debug=True)