"""This module contains API bindings for https://openrouteservice.org/
API docs can be viewed on https://openrouteservice.org/dev/#/api-docs
"""

import requests

from secrets_file import openroute_api_key

API_ROOT = 'https://api.openrouteservice.org/v2/'
API_END_POINTS = {
    'directions_via_car': 'directions/{method}?api_key={api_key}&start={start_lat},{start_long}&end={end_lat},{end_long}'
}

def get_route(start, end):
    """Fetches a route from openrouteservice between start and end.
    Args:
        start (tuple): longitude, latitude
        end (tuple): longitude, latitude
    Returns:
        Dictionary of `distance` and `duration`
    """
    endpoint = API_ROOT + API_END_POINTS['directions_via_car']
    endpoint = endpoint.format(
        method='driving-car',
        api_key=openroute_api_key,
        start_lat=start[0],
        start_long=start[1],
        end_lat=end[0],
        end_long=end[1]
    )
    # 7print(endpoint)
    r = requests.get(endpoint)
    if r.status_code == 200:
        return r.json()
    else:
        print(r.text)
        raise Exception('Route couldnt be fetched. Status code: %s', r.status_code)
    

def get_travel_summary(start, end):
    """Returns travel time in minutes and travel distance in miles between two points
    Args:
        start (tuple): longitude, latitude
        end (tuple): longitude, latitude 
    Returns:
        Dictionary of `distance` and `duration`
    """
    route = get_route(start, end)
    summary = route['features'][0]['properties']['summary']
    time = int(summary['duration'] / 60)  # Convert to minutes
    distance = round(summary['distance'] * 0.000621, 2) # Convert to miles
    return {
        'duration': time,
        'distance': distance
    }

if __name__ == '__main__':
    print(
        get_travel_summary(
            (-121.9435584, 37.3273372), (-121.9308873, 37.3657848))
        )
