from s2 import s2


def get_s2_id(lat: float, lon: float, level: int = 16) -> str:
    """Return s2 id for given lat, lon and level.
    :param lat: Latitude of point.
    :param lon: Longitude of point.
    :param level: resolution level.
    :return: S2 id.
    """
    return s2.geo_to_s2(lat, lon, level)
