import app.utils as utils
import app.data as data

def main():
    date = data.get_tomorrow()
    temps = data.get_temp()
    wind = data.get_wind()
    tides = data.get_tides()
    utils.write_index(date | temps | wind | tides)

if __name__ == "__main__":
    main()