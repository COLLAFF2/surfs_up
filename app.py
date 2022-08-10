# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# import SQLalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify

# set up dtabase engine for flask
engine = create_engine("sqlite:///hawaii.sqlite")

 # reflect database
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station 

# create session link from python to database
session = Session(engine)

# define flask app
app = Flask(__name__)

# define the welcome route
@app.route("/")

# create welcome function
#add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


