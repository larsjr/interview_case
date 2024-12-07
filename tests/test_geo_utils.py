import pytest
from geo_utils import normalize_longitude


@pytest.mark.parametrize(
    "longitude, expected_normalized",
    [
        (181, -179),  # Just above 180
        (-181, 179),  # Just below -180
        (359, -1),  # Wrap-around near 360
        (-359, 1),  # Wrap-around near -360
        (90, 90),  # Already normalized
        (-90, -90),  # Already normalized
        (450, 90),  # More than one full rotation positive
        (-450, -90),  # More than one full rotation negative
        (1080, 0),  # Multiple rotations positive
        (-1080, 0),  # Multiple rotations negative
    ],
)
def test_normalize_longitude(longitude, expected_normalized):
    normalized = normalize_longitude(longitude)
    assert normalized == pytest.approx(expected_normalized)
