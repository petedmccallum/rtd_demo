"""
Carbon Intensity - API demo

Toy function for demonstration of 'readthedocs'.
"""

import requests

def carbon_now():
    """
    This function provides the live grid carbon intensity data from the API:
    https://api.carbonintensity.org.uk/


    Returns
    -------
    live_gen_mix : dict
        The current generation mix (as dict) is provided as a single output argument.

    """

    # API call to https://api.carbonintensity.org.uk/intensity for current CI
    headers = {
    'Accept': 'application/json'
    }
    r1 = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)


    # Relevant data fields
    kgco2 = r1.json()['data'][0]['intensity']['actual']
    kgco2f = r1.json()['data'][0]['intensity']['forecast']
    dt_from = r1.json()['data'][0]['from']
    dt_to = r1.json()['data'][0]['to']


    # Compose message
    msg1 = f"Between {dt_from[11:16]} and {dt_to[11:16]} ({dt_from[:10]}), the carbon intensity for the UK grid"\
        f" was {kgco2} kgCO2/kWh (forecasted at {kgco2f}). "\
        f"\nSee https://carbon-intensity.github.io/api-definitions/?python#carbon-intensity-api-v2-0-0"\
        f"for more info"
    print(msg1)


    # API call to https://api.carbonintensity.org.uk/intensity for current energy mix breakdown
    r2 = requests.get('https://api.carbonintensity.org.uk/intensity/factors', params={}, headers = headers)

    live_gen_mix = r2.json()['data'][0]
    print(f"Live generation mix:\n{live_gen_mix}")

    return live_gen_mix
