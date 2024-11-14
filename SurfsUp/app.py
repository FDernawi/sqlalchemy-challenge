#import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from flask import Flask, jsonify
import datetime as dt

# Database setup
database_path = "/Users/faisaldernawi/Desktop/Training_And_Development/GW_Bootcamp/Homework/Module_10/Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{database_path}")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save database references to a table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# List all available routes
@app.route("/")
def welcome():
    """List all available API routes"""
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/<start_date><br/>"
        f"/api/v1.0/temp/<start_date>/<end_date><br/>"
    )

# Route for precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return JSON representation of last 12 months of precipitation data"""
    session = Session(engine)

    # Query the last 12 months of precipitation data
    latest_date = session.query(func.max(Measurement.date)).scalar()
    cutoff_date = dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > cutoff_date).all()
    session.close()

    # Create a dictionary from the results
    precip_data = [{date: prcp} for date, prcp in results]
    return jsonify(precip_data)

# Route for stations
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations"""
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    # Convert results to a list
    stations = [station[0] for station in results]
    return jsonify(stations)

# Route for temperature observations
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the last 12 months"""
    session = Session(engine)

    # Identify the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(
        func.count(Measurement.station).desc()).first()[0]

    # Query the last 12 months of temperature data for the most active station
    latest_date = session.query(func.max(Measurement.date)).scalar()
    cutoff_date = dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == most_active_station,
        Measurement.date > cutoff_date).all()
    session.close()

    # Create a list of temperature observations
    tobs_data = [{"Date": date, "Observed Temperature": tobs} for date, tobs in results]
    return jsonify(tobs_data)

# Route for temperature stats from start date
@app.route("/api/v1.0/temp/<start_date>")
def temps_start(start_date):
    """Return JSON with min, avg, and max temperature from start date"""
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(
        Measurement.date >= start_date).all()
    session.close()

    # Create a dictionary for the stats
    if results[0][0] is not None:
        temp_data = {
            "Minimum Temperature": results[0][0],
            "Average Temperature": results[0][1],
            "Maximum Temperature": results[0][2]
        }
    else:
        temp_data = {"error": "No data available for the given start date."}

    return jsonify(temp_data)

# Route for temperature stats between start and end dates
@app.route("/api/v1.0/temp/<start_date>/<end_date>")
def temps_start_end(start_date, end_date):
    """Return JSON with min, avg, and max temperature for a date range"""
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(
        Measurement.date >= start_date,
        Measurement.date <= end_date).all()
    session.close()

    # Create a dictionary for the stats
    if results[0][0] is not None:
        temp_data = {
            "Minimum Temperature": results[0][0],
            "Average Temperature": results[0][1],
            "Maximum Temperature": results[0][2]
        }
    else:
        temp_data = {"error": "No data available for the given date range."}

    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)