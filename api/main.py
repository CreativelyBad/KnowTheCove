from flask import Flask

import api.utils as utils
import api.data as data

app = Flask(__name__)

@app.route('/')
def main():
    date = data.get_tomorrow()
    temps = data.get_temp()
    wind = data.get_wind()
    tides = data.get_tides()
    utils.write_index(date | temps | wind | tides)