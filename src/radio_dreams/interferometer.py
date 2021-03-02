import numpy as np
import pandas as pd


class Telescope:
    """Calculate local X, Y, Z coordinates of an a array's antennas."""

    def __init__(self, array_csv, latitude):
        self.array_csv = array_csv
        self.latitude = latitude

    def read_array(self):

        print(self.array_csv)
        df = pd.read_csv(self.array_csv)
        e = df["East"].to_numpy()
        n = df["North"].to_numpy()
        h = df["Height"].to_numpy()
        tiles = df["Tile"]

        return np.array([tiles, e, n, h])


if __name__ == "__main__":

    mwa = Telescope("../arrays/mwa_phase2.csv", -27.0)

    print(mwa.read_array()[0])
    print(mwa.read_array()[1][-1])
