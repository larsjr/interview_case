from __future__ import annotations


def normalize_longitude(longitude: float) -> float:
    """
    Longitude ranges from -180 to 180 degrees. On map with infinite scroll,
    the values can go beyond these values, and we need to normalize it to be between
    [-180, 180].
    """
    return (longitude + 180) % 360 - 180
