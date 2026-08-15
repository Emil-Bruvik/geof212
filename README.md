# GEOF212 — Python exercises

Python materials for the course "physical climatology" at the University of Bergen, Norway.

## Setup

```
conda env create -f environment.yml
conda activate geof212env
jupyter lab
```

Launch `jupyter lab` from *inside* the activated `geof212env` environment. Mixing a JupyterLab
installed in a different (e.g. base) environment with the kernel from `geof212env` is what causes
the "old Python 3.8 / old JupyterLab" conflicts — `environment.yml` now installs a modern,
self-contained JupyterLab, so there's no need to reach into another environment for it.

If your existing `geof212env` predates this update, remove and recreate it rather than updating
in place:

```
conda env remove -n geof212env
conda env create -f environment.yml
```

## Data

Exercises 4, 6, 7 and 8 read monthly-mean ERA5 fields from:

```
/Data/gfi/share/era5/geof212_exercises/
```

Exercise 3 reads CMIP5/NorESM data from `/Data/gfi/share/ModData/CMIP5_ATMOS/atmos/historical/`
(unchanged).

### `cds_requests/`

Some variables needed by exercises 4, 6 and 8 (clear-sky TOA radiation, evaporation, turbulent
surface wind stress) aren't in the local ERA5 archive and have to be pulled from the Copernicus
Climate Data Store. `cds_requests/` has one `cdsapi` request script per exercise; see the
docstring in each script for one-time setup (installing `cdsapi`, registering a CDS API key,
accepting the dataset's terms of use).
