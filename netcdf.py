from __future__ import annotations
import xarray as xr
import datetime
from datetime import date


def get_highest_wave_height_for_date(
    filepath: str, latitude: float, longitude: float, date_: date
) -> float:
  """
  Get the  hightest wave height for a given day on the provided location
  by summing up all hourly values registered for that day.

  Args:
    filepath: Path to netcdf file
    latitude: Latitude to check
    longitude: Longitude to check
    date_: The date we want for which we want to find the max wave height

  Returns:
    The max wave height
  """
  end_date = date_ + datetime.timedelta(days=1)
  with xr.open_dataset(filepath) as ds:
      return (
          ds.sel(latitude=latitude, longitude=longitude)
          .sel(time=slice(date_, end_date))
          .hmax.values.max()
      )


if __name__ == "__main__":
    date_to_check = date(2019, 1, 1)
    latitude = 0.000
    longitude = 0.000
    hmax = get_highest_wave_height_for_date(
        "waves_2019-01-01.nc",
        latitude=latitude,
        longitude=longitude,
        date_=date_to_check,
    )
    print(f"Max wave height at ({latitude}, {longitude}) for {date_to_check} is {hmax}")
