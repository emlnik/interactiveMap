import xarray as xr
import matplotlib.pyplot as plt
import json

with open('config.json', 'r') as f:
    config = json.load(f)

data = xr.open_dataset(r"C:\Users\nikic\Downloads\waves_2019-01-01.nc")

try:

    nearest_point = data.sel(latitude=config['latitude'], longitude=config['longitude'], method='nearest')

    # Extract time, latitude, and longitude from the nearest_point
    time = nearest_point.time.data
    latitude = nearest_point.latitude.data
    longitude = nearest_point.longitude.data

    max_wave_height = nearest_point.hmax.max().values

    plt.scatter(longitude, latitude, color='red', label='Selected Point')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'Max Wave Height at nearest point to (0.0, 0.0) on {time}')
    plt.legend()
    plt.text(longitude, latitude, f'Max Wave Height: {max_wave_height}', ha='right', va='bottom', color='black',
             fontsize=8)
    plt.show()

except Exception as e:
    print("Error:", e)
