from flask import Flask, jsonify, request
import xarray as xr
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/get_max_wave_height', methods=['POST'])
def get_max_wave_height():
    try:
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        data = xr.open_dataset(r"C:\Users\nikic\Downloads\waves_2019-01-01.nc")

        nearest_point = data.sel(latitude=latitude, longitude=longitude, method='nearest')

        max_wave_height = nearest_point.hmax.max().values.tolist()
        if np.isnan(max_wave_height):
            max_wave_height = None
        response = {
            'max_wave_height': max_wave_height
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
