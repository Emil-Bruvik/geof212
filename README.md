# GEOF212 — Python exercises

Python materials for the course "physical climatology" at the University of Bergen, Norway.

## Setup

Cyclone provides Anaconda as a shared module — load it instead of installing your own
Miniconda. It already includes Python, JupyterLab, numpy, matplotlib, xarray, pandas and
more; `cartopy` and `netCDF4` are the only packages missing, so those get added on top
with `pip install --user` (installs into your home directory, not the shared module):

```
module load Anaconda3
pip install --user -r requirements.txt
jupyter lab
```

No `conda create`, `conda activate`, or manual kernel registration needed. The module
uses a working default kernel, and packages installed with `pip install --user` are
visible from it automatically.

## Data

Exercises 4, 6, 7 and 8 read monthly-mean ERA5 fields (`year`/`month`/`lat`/`lon`,
2.5° grid) from:

```
/Data/gfi/scratch/GEOF212/erai/
```

Exercise 3 reads CMIP5/NorESM data from `/Data/gfi/share/ModData/CMIP5_ATMOS/atmos/historical/`
