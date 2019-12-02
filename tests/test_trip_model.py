import pytest
import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from commute_time.models.trip import Trip

def test_test():
    assert True
    
def test_trip_model():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    Trip.__table__.create(engine)
    new_trip = Trip()
    session = sessionmaker(bind=engine)()
    session.add(new_trip)
    session.commit()
    q = session.query(Trip)
    assert q.count() > 0

