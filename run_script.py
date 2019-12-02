import os
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='data/logs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if not os.path.isdir('data'):
    os.mkdir('data')

from commute_time import save_trip

save_trip.main()

