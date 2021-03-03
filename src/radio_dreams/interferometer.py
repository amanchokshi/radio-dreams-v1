import numpy as np
import pandas as pd


class ArrayConfig:
    """A class used to represent the positions of antennas in an interferometer

    Antenna positions are usually defined with respect to the array centre.

    E - East of the center in metres
    N - North of center in metres
    H - Height above sea level in metres

    Convert these coordinates to a Earth Centered Earth Fixed (ECEF) cartesian
    system with axes pointing towards

    X - (h = 0, δ = 0)
    Y - (h = -6, δ = 0)
    Z - (δ = 90)

    h - hour angle
    δ - declination

    .. code-block:: python

        from radio_dreams import interferometer

        mwa_latitude = -26.7033194444

        # An instance of the interferometer.ArrayConfig class for the MWA
        mwa = interferometer.ArrayConfig(array_csv="../arrays/mwa_phase2.csv", latitude=mwa_latitude)

        # Access the original E, N, H positions of tiles and tile names
        E = mwa.east
        N = mwa.north
        H = mwa.height
        T = mwa.tiles

        # Access X, Y, Z coordinates of tiles
        x, y, z = mwa.enh_xyz()


    """

    def __init__(self, array_csv, latitude):
        self.array_csv = array_csv
        self.latitude = latitude

        # Read array layout csv file
        df = pd.read_csv(self.array_csv)
        self.east = df["East"].to_numpy()
        self.north = df["North"].to_numpy()
        self.height = df["Height"].to_numpy()
        self.tiles = df["Tile"]

    def enh_xyz(self):
        """Convert from local E, N, H to X, Y, Z coordinates"""

        sin_lat = np.sin(self.latitude)
        cos_lat = np.cos(self.latitude)

        x = self.height * cos_lat - self.north * sin_lat
        y = self.east
        z = self.height * sin_lat + self.north * sin_lat

        return x, y, z
