"""
Get geohash codes of current and the 8 around coordinates.
Used Geohash.
Implement by Bryan Yang
"""
import Geohash

LAT_RANGE_MIN = -90  # latitude scope[-90, 90]
LAT_RANGE_MAX = 90
LONG_RANGE_MIN = -180  # longitude scope[-180, 180]
LONG_RANGE_MAX = 180


class GeoHashAround(object):
    def __init__(self, latitude, longitude, precision=8):
        self.lat = latitude
        self.long = longitude
        self.precision = precision
        self.min_lat_unit = 0
        self.min_long_unit = 0
        self.lat_cut_times = self.long_cut_times = (5 * int(self.precision)) / 2

    def get_around_geohashs(self):
        around_geohashs = {}
        self._get_min_lat_unit()
        self._get_min_long_unit()
        # north
        around_geohashs['n'] = Geohash.encode(self.lat + self.min_lat_unit, self.long, self.precision)
        around_geohashs['c'] = Geohash.encode(self.lat, self.long, self.precision)
        around_geohashs['s'] = Geohash.encode(self.lat, self.long + self.min_long_unit, self.precision)
        # northwest
        around_geohashs['nw'] = Geohash.encode(
            self.lat - self.min_lat_unit, self.long + self.min_long_unit, self.precision)
        # southwest
        around_geohashs['sw'] = Geohash.encode(
            self.lat - self.min_lat_unit, self.long - self.min_long_unit, self.precision)
        # northeast
        around_geohashs['ne'] = Geohash.encode(
            self.lat + self.min_lat_unit, self.long + self.min_long_unit, self.precision)
        # southeast
        around_geohashs['se'] = Geohash.encode(
            self.lat + self.min_lat_unit, self.long - self.min_long_unit, self.precision)
        return around_geohashs

    def _get_min_lat_unit(self):
        self.min_lat_unit = LAT_RANGE_MAX - LAT_RANGE_MIN
        i = 0
        while i < self.lat_cut_times:
            i += 1
            self.min_lat_unit = self.min_lat_unit / 2.0

    def _get_min_long_unit(self):
        self.min_long_unit = LONG_RANGE_MAX - LONG_RANGE_MIN
        i = 0
        while i < self.long_cut_times:
            i += 1
            self.min_long_unit = self.min_long_unit / 2.0


if __name__ == '__main__':
    gha = GeoHashAround(30.7224323343, 103.8239765167, precision=6)
    gha.get_around_geohashs()
