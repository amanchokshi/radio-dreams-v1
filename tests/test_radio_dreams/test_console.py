from os import path
from pathlib import Path

import click.testing
import pytest

from radio_dreams import console

# Save the path to this directory
dirpath = path.dirname(__file__)

# Obtain path to directory with test_data
test_data = path.abspath(path.join(dirpath, "../test_data"))


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_radio_dreams_succeeds(runner):
    result = runner.invoke(console.radio_dreams)
    assert result.exit_code == 0


def test_plot_array_succeeds(runner):
    result = runner.invoke(
        console.plot_array,
        [f"--array_csv={test_data}/test_mwa.csv", f"--out_dir={test_data}"],
    )
    assert result.exit_code == 0

    array_png = Path(f"{test_data}/test_mwa_array.png")
    assert array_png.is_file()

    if array_png.is_file():
        array_png.unlink()
