from s2 import s2


def get_s2_id(lat: float, lon: float, level: int = 16) -> str:
    """Return s2 id for given lat, lon and level.
    :param lat: Latitude of point.
    :param lon: Longitude of point.
    :param level: resolution level.
    :return: S2 id.
    """
    return s2.geo_to_s2(lat, lon, level)


def convert_miles_to_km(distance: float) -> float:
    """Return Distnace in kilometers.
    :param distance: distance in miles.
    :return:
    """
    return distance * 1.6093435


def convert_seconds_to_hours(seconds: float) -> float:
    """Return time in hours.

    :param seconds:
    :return:
    """
    return seconds / 3600
