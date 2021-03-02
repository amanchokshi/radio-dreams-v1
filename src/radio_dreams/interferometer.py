import numpy as np
import pandas as pd


class Telescope:
    """Calculate local X, Y, Z coordinates of an a array's antennas."""

    def __init__(self, array_csv, latitude):
        self.array_dir = array_csv
        self.latitude = latitude

    def read_array(self):

        df = pd.read_csv(self.array_csv)
        e = df["East"].to_numpy()
        n = df["North"].to_numpy()
        h = df["Height"].to_numpy()
        tiles = df["Tile"]

        return np.array([tiles, e, n, h])


if __name__ == "__main__":

    mwa = Telescope("../data/arrays/mwa_phase2.csv")

    print(mwa.read_array()[0])
