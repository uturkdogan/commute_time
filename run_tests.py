import os
import pytest
import logging
import commute_time

if not os.path.isdir('data'):
    os.mkdir('data')

logging.basicConfig(filename='data/logs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

pytest.main(['-x', 'tests'])
