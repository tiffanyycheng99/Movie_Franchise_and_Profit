import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
from flask import Flask

eng = create_engine("postgresql://postgres:postgres@movie-swear-db.cfgivq9r1u3j.us-west-2.rds.amazonaws.com:5432/moviesweardb")
con = eng.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)
#movie_swear = Base.classes.movie_swear