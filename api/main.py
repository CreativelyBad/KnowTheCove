import utils
import data


def main():
    date = data.get_tomorrow()
    temps = data.get_temp()
    wind = data.get_wind()
    tides = data.get_tides()

    return utils.write_index(date | temps | wind | tides)

