import dash
from dash import html
import dash_leaflet as dl
from dash.dependencies import Output, Input
from datetime import date
from netcdf import calculate_highest_wave_height_for_date
from geo_utils import normalize_longitude

MAP_ID = "map"
COORDINATE_CLICK_ID = "coordinate-click-output"
DATE = date(2019, 1, 1)
WAVE_DATA = "waves_2019-01-01.nc"

app = dash.Dash()
app.layout = html.Div(
    [
        html.H1(f"Get max wave height for given coordinate for {DATE}"),
        dl.Map(
            dl.TileLayer(),
            id=MAP_ID,
            style={"width": "100%", "height": "500px"},
            center=[0, 0],  # Center the map on the equator
            zoom=2,
        ),
        html.P("Coordinates (click on the map):"),
        html.Div(id=COORDINATE_CLICK_ID),
    ]
)


# Callback to handle click events and display coordinates
@app.callback(Output(COORDINATE_CLICK_ID, "children"), Input(MAP_ID, "clickData"))
def click_coord(event: dict | None):
    if event is not None:
        latitude, longitude = parse_latitude_and_longitude(event)
        max_wave_height = calculate_highest_wave_height_for_date(
            WAVE_DATA, DATE, latitude=latitude, longitude=longitude
        )
        return f"Max wave height for ({latitude:.3f}, {longitude:.3f}) is {max_wave_height}"
    else:
        return "Click on the map to see coordinates."


def parse_latitude_and_longitude(click_event: dict) -> tuple[float, float]:
    latitude = round(click_event["latlng"]["lat"], 3)
    longitude = normalize_longitude(round(click_event["latlng"]["lng"], 3))
    return latitude, longitude


if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8081, debug=True)


# TODOs that were sipped due to time constraint:
# 1. Add proper logging
# 2. Investigate typing for dash
# 3. Set up pre-commit checks
