import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The Radio Dreams Python project."""

    click.secho("Radio Dreams\n", fg="blue")

    click.echo("Author: Aman Chokshi")
    click.echo(f"V:{__version__}\n")

    click.echo("Imagined Interferometers")
