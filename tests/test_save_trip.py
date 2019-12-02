import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os

from commute_time import save_trip
from commute_time.models.trip import Trip

def test_get_current_location():
    lat, long = save_trip.get_current_location()
    assert lat and long

def test_record_trip():
    engine = sqlalchemy.create_engine('sqlite:///data/test_trips.db')
    save_trip.record_trip(engine)
    assert os.path.isfile('data/test_trips.db')
    # check for open trip
    session = sessionmaker(bind=engine)()
    open_trips = session.query(Trip).filter_by(completed=False).order_by(Trip.id.desc())
    assert open_trips.count() == 1

