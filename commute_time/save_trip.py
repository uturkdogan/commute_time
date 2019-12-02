import sqlalchemy
from sqlalchemy.orm import sessionmaker

import datetime
import logging

from commute_time import models
from commute_time.models.trip import Trip

import location

logger = logging.getLogger(__name__)

def get_current_location():
    """Returns current location in a tuple of (latitude, longitude)
    """
    if not location.is_authorized():
        print('Location not authorized.')
        raise SystemExit
    location.start_updates()
    current_location = location.get_location()
    location.stop_updates()
    return (current_location['latitude'], current_location['longitude'])

def record_trip(engine):
    """Records a trip, if there are any open trips, it closes them.
    If not it creates a trip.
    """
    # engine = sqlalchemy.create_engine('sqlite://data/trips.db')
    # Create all tables
    models.create_all(engine)
    
    # Get Current location
    latitude, longitude = get_current_location()
    
    # Create session
    session = sessionmaker(bind=engine)()
    open_trips = session.query(Trip).filter_by(completed=False).order_by(Trip.id.desc())
    last_open_trip = open_trips.first()
    if last_open_trip:
        last_open_trip.end_lat = latitude
        last_open_trip.end_long = longitude
        last_open_trip.end_timestamp = datetime.datetime.now()
        last_open_trip.completed = True
        logger.info('Ending trip %s with %s, %s', last_open_trip, last_open_trip.end_lat, last_open_trip.end_long)
    else:
        new_trip = Trip()
        new_trip.start_lat = latitude
        new_trip.start_long = longitude
        logger.info('Starting a new trip')
        session.add(new_trip)
    session.commit()
    session.close()

def main():
    engine = sqlalchemy.create_engine('sqlite:///data/trips.db')
    record_trip(engine)
    engine.dispose()
