"""Plot layout of antennas in interferometric array."""

from pathlib import Path

import click
from matplotlib import pyplot as plt

from radio_dreams import __version__, interferometer


@click.command()
@click.option(
    "--array_csv",
    help="Path to array layout csv file",
    default="./arrays/mwa_phase2.csv",
    type=str,
)
@click.version_option(version=__version__)
def plot_array(array_csv):
    """Plot the layout antennas for an interferometer."""
    array_csv = Path(array_csv)
    mwa = interferometer.ArrayConfig(array_csv=array_csv)

    plt.style.use("seaborn")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mwa.east, mwa.north, marker="s", color="seagreen", alpha=0.8)
    ax.set_aspect(aspect=1)
    ax.set_xlabel("East [m]")
    ax.set_ylabel("North [m]")
    ax.set_title(f"{array_csv.stem} array layout")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_array()
