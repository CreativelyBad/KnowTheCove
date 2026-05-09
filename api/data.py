import asyncio
from bs4 import BeautifulSoup as bs
from env_canada import ECWeather as ecw
import httpx
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def get_tomorrow():
    tz = ZoneInfo("America/Vancouver")
    
    now = datetime.now(tz)
    tomorrow = now + timedelta(days=1)
    
    return {'date': tomorrow.strftime("%A, %B %d, %Y")}

def get_temp():
    ec = ecw(coordinates=(49.323, -122.948))
    asyncio.run(ec.update())
    temp = ec.daily_forecasts

    return {
        'temp_high': temp[1]['temperature'],
        'temp_low': temp[2]['temperature']
    }

def get_wind():
    url = 'https://weather.gc.ca/marine/forecast_e.html?mapID=02&siteID=06400'
    response = httpx.get(url)
    soup = bs(response.text, 'html.parser')
    wind = soup.find(class_='textSummary').get_text()
    return {'wind': wind}

def get_tides():
    url = 'https://www.tide-forecast.com/locations/Deep-Cove-British-Columbia/tides/latest'
    response = httpx.get(url)
    soup = bs(response.text, 'html.parser')
    tomorrow_heading = soup.find('h4', string=lambda t: t and 'tomorrow' in t.lower())

    if tomorrow_heading:
        tide_data = []
        
        # find the table right after it
        table = tomorrow_heading.find_next('table')
        
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 3:
                # "3:49 AM (Wed 06 May)" -> "3:49 AM"
                time = cells[1].get_text(strip=True).split('(')[0].strip()
                
                tide_data.append({
                    'type': cells[0].get_text(strip=True),
                    'time': time,
                    'height': cells[2].get_text(strip=True)
                })
    
    return {'tides': tide_data}
