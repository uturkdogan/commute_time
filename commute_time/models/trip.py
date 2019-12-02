from commute_time.models import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean

import datetime

class Trip(Base):
    __tablename__ = 'trips'
    
    id = Column(Integer, primary_key=True)
    start_long = Column(Float(precision=32, decimal_return_scale=None))
    start_lat = Column(Float(precision=32, decimal_return_scale=None))
    start_timestamp = Column(DateTime, default=datetime.datetime.now)
    end_long = Column(Float(precision=32, decimal_return_scale=None))
    end_lat = Column(Float(precision=32, decimal_return_scale=None))
    end_timestamp = Column(DateTime)
    completed = Column(Boolean, default=False)

