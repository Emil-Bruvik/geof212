#!/usr/bin/env python3
"""
Download request for exercise 8 (wind-driven ocean circulation).

Missing from the local /Data/gfi/share/era5/ archive: ewss, nsss (turbulent
surface wind stress components). sst is not requested here since it's
already available locally.

Prerequisites (one-time):
  1. pip install "cdsapi>=0.7.7"
  2. Create $HOME/.cdsapirc with:
       url: https://cds.climate.copernicus.eu/api
       key: <YOUR-PERSONAL-ACCESS-TOKEN>
     (token from https://cds.climate.copernicus.eu/how-to-api, after logging in)
  3. Accept the dataset's Terms of Use at the bottom of:
       https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means

Run:
  python3 request_ex08_wind_stress.py

This blocks until the CDS has prepared the file (can take anywhere from
minutes to a couple of hours depending on queue load) and then downloads it.
"""

import cdsapi

DATASET = "reanalysis-era5-single-levels-monthly-means"

REQUEST = {
    "product_type": "monthly_averaged_reanalysis",
    "variable": [
        "eastward_turbulent_surface_stress",
        "northward_turbulent_surface_stress",
    ],
    "year": [str(y) for y in range(1979, 2018)],
    "month": [f"{m:02d}" for m in range(1, 13)],
    "time": "00:00",
    "data_format": "netcdf",
    "download_format": "unarchived",
}

TARGET = "/Data/gfi/share/era5/geof212_exercises/raw_cds_downloads/ex08_wind_stress_monthly_1979-2017.nc"

if __name__ == "__main__":
    client = cdsapi.Client()
    client.retrieve(DATASET, REQUEST, TARGET)
    print(f"Saved: {TARGET}")
