"""Command-line interface."""

from pathlib import Path

import click
from matplotlib import pyplot as plt

from radio_dreams import __version__, interferometer


@click.command()
@click.version_option(version=__version__)
def radio_dreams():
    """Radio Dreams python project."""
    click.secho("Radio Dreams\n", fg="blue")

    print("Author: Aman Chokshi")
    print(f"V:{__version__}\n")


@click.command()
@click.option(
    "--array_csv", help="Path to array layout csv file", type=str, required=True
)
@click.option(
    "--out_dir",
    help="Output directory to save plots",
    type=str,
    default="./dream-plots",
    show_default=True,
)
def plot_array(array_csv, out_dir):
    """Plot the layout antennas for an interferometer."""
    array_csv = Path(array_csv)
    mwa = interferometer.ArrayConfig(array_csv=array_csv)

    # Make out_dir if doesn't exist
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    plt.style.use("seaborn")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mwa.east, mwa.north, marker="s", color="seagreen", alpha=0.8)
    ax.set_aspect(aspect=1)
    ax.set_xlabel("East [m]")
    ax.set_ylabel("North [m]")
    ax.set_title(f"{array_csv.stem} array layout")

    plt.tight_layout()
    plt.savefig(f"{out_dir}/{array_csv.stem}_array.png", dpi=300)
