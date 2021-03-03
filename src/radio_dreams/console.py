import click
from matplotlib import pyplot as plt

from radio_dreams import interferometer

from . import __version__


@click.command()
@click.version_option(version=__version__)
def radio_dreams():
    """The Radio Dreams Python project."""

    click.secho("Radio Dreams\n", fg="blue")

    print("Author: Aman Chokshi")
    print(f"V:{__version__}\n")


@click.command()
@click.option(
    "--array", prompt="Path to array csv file", help="Path to array layout csv file"
)
@click.option("--latitude", prompt="Array latitude", help="Latitude of array")
def plot_array(array, latitude):
    """Plot the layout antennas for an interferometer"""
    mwa = interferometer.ArrayConfig(array_csv=array, latitude=latitude)

    plt.style.use("seaborn")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mwa.east, mwa.north, marker="s", color="seagreen")
    ax.set_aspect(aspect=1)
    ax.set_xlabel("East [m]")
    ax.set_ylabel("North [m]")
    ax.set_title("Array layout")

    plt.tight_layout()
    plt.show()
