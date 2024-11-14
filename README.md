SQLAlchemy Challenge

1. Before You Begin

1.1. Create a New Repository: Name the repository sqlalchemy-challenge. Do not add this assignment to an existing repository.
1.2. Clone the Repository: Clone the newly created repository to your local computer.
1.3. Setup Your Local Repository: Create a directory for this challenge, such as SurfsUp. Add the following files to this folder:
    •    Jupyter Notebook for your analysis.
    •    app.py for your Flask API.
    •    The Resources folder containing your data files (e.g., hawaii.sqlite).
1.4. Push Changes to GitHub: Commit your files with appropriate messages. Push them to your GitHub repository.

2. Files

Use the provided files:
    •    climate_starter.ipynb
    •    hawaii.sqlite

3. Instructions

3.1 Part 1: Analyze and Explore the Climate Data

Goal: Perform basic climate analysis and data exploration using Python, SQLAlchemy, Pandas, and Matplotlib.

3.1.1 Setup

    1.    Use SQLAlchemy create_engine() to connect to your SQLite database.
    2.    Use SQLAlchemy automap_base() to reflect tables into classes, and save references to the station and measurement tables.
    3.    Link Python to the database by creating a SQLAlchemy session.
    4.    Close your session at the end of your notebook.

3.1.2 Precipitation Analysis

    1.    Find the most recent date in the dataset.
    2.    Query the last 12 months of precipitation data:

    •    Select only date and prcp values.
    •    Load the results into a Pandas DataFrame and explicitly set column names.
    •    Sort the DataFrame by date.

    3.    Plot the results using the Pandas plot method (e.g., date on X-axis, prcp on Y-axis).
    4.    Use Pandas to print summary statistics for the precipitation data.

3.1.3 Station Analysis

    1.    Query the total number of stations in the dataset.
    2.    Identify the most active stations:

    •    List stations and observation counts in descending order.
    •    Determine the station ID with the highest number of observations.

    3.    For the most active station:

    •    Calculate the minimum, maximum, and average temperatures.
    •    Query the last 12 months of tobs data.
    •    Plot the results as a histogram with bins=12.

    4.    Close your session.

3.2 Part 2: Design Your Climate App

Goal: Use Flask to create API routes based on the queries developed in Part 1.

Routes

    1.    Homepage /: List all available routes.
    2.    Precipitation /api/v1.0/precipitation: Query the last 12 months of precipitation data. Convert the results into a dictionary (date as key, prcp as value). Return the JSON representation.
    3.    Stations /api/v1.0/stations: Return a JSON list of all stations in the dataset.
    4.    Temperature Observations /api/v1.0/tobs: Query the dates and temperature observations of the most active station for the previous year. Return a JSON list of temperature observations.
    5.    Dynamic Routes:

    •    /api/v1.0/<start>: Return the minimum, average, and maximum temperatures for dates greater than or equal to the start date.
    •    /api/v1.0/<start>/<end>: Return the minimum, average, and maximum temperatures for the specified date range.

4. Hints

    1.    Use joins between the station and measurement tables for some queries.
    2.    Use Flask’s jsonify function to convert data into JSON responses.

5. Requirements

5.1 Jupyter Notebook Database Connection (10 points)

    1.    Use create_engine() to connect to the database (1 point).
    2.    Reflect tables into classes using automap_base() (3 points).
    3.    Save references to station and measurement classes (4 points).
    4.    Link Python to the database with a SQLAlchemy session (1 point).
    5.    Close the session at the end of the notebook (1 point).

5.2 Precipitation Analysis (16 points)

    1.    Query the most recent date in the dataset (8/23/2017) (2 points).
    2.    Query the last year of precipitation data (4 points).
    3.    Load results into a Pandas DataFrame with date and prcp columns (2 points).
    4.    Sort the DataFrame by date (2 points).
    5.    Plot results with date on the X-axis and prcp on the Y-axis (4 points).
    6.    Print summary statistics for precipitation data (2 points).

5.3 Station Analysis (16 points)

    1.    Query the total number of stations (2 points).
    2.    List stations and observation counts, and identify the most active station (2 points).
    3.    Query min, max, and average temperatures for the most active station (3 points).
    4.    Query the last 12 months of tobs data for the most active station (3 points).
    5.    Save results into a Pandas DataFrame (2 points).
    6.    Plot a histogram with bins=12 for tobs data (4 points).

5.4 Flask API (40 points)

    1.    Static Routes (25 points):

    •    /api/v1.0/precipitation: Return JSON of last year’s precipitation data (6 points).
    •    /api/v1.0/stations: Return JSON of all stations (6 points).
    •    /api/v1.0/tobs: Return JSON of last year’s temperature observations for the most active station (6 points).

    2.    Dynamic Routes (15 points):

    •    /api/v1.0/<start>: Min, avg, and max temperatures from the start date (6 points).
    •    /api/v1.0/<start>/<end>: Min, avg, and max temperatures for the date range (9 points).

5.5 Coding Conventions (8 points)

    1.    Place imports at the top of the file (2 points).
    2.    Use lowercase for function and variable names (2 points).
    3.    Avoid repeating logic (2 points).
    4.    Write concise and maintainable code (2 points).

5.6 Deployment and Submission (6 points)

    1.    Submit a GitHub link with all files included (2 points).
    2.    Use the command line to add files to the repository (2 points).
    3.    Include appropriate commit messages (2 points).

5.7 Comments (4 points)

    1.    Add concise and relevant comments to explain your code (4 points).
