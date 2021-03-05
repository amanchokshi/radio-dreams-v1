"""Tests radio_dreams.interferometer."""

from os import path

from radio_dreams.interferometer import ArrayConfig

# Save the path to this directory
dirpath = path.dirname(__file__)

# Obtain path to directory with test_data
test_data = path.abspath(path.join(dirpath, "../test_data"))


def test_ArrayConfig():
    """Instance of ArrayConfig with test_mwa.csv array to test outputs."""
    mwa = ArrayConfig(array_csv=f"{test_data}/test_mwa.csv", latitude=-27)
    x, y, z = mwa.enh_xyz()

    # Test __init__
    assert mwa.east[0] == -1999.81
    assert mwa.north[0] == 206.85
    assert mwa.height[0] == 372.921
    assert mwa.tiles[0] == "LBA1"

    # Test enh_xyz
    assert x[0] == 88.88166409864053
    assert y[0] == -1999.81
    assert z[0] == -554.4790283870071


def test_ArrayConfig_no_args(capfd):
    """It prints exception for missing latitude arg."""
    ArrayConfig(array_csv=f"{test_data}/test_mwa.csv").enh_xyz()

    out, err = capfd.readouterr()
    assert "missing 1 required argument: 'latitude'" in out


def test_ArrayConfig_freqs():
    """It outputs freq array and compares results."""
    mwa = ArrayConfig(
        array_csv=f"{test_data}/test_mwa.csv",
        latitude=-27,
        freq_start=160e6,
        freq_bands=24,
        bandwidth=1 * +6,
    )

    assert mwa.freqs()[0] == 160.0e6


def test_ArrayConfig_freqs_no_args(capfd):
    """It prints exception for missing args."""
    ArrayConfig(array_csv=f"{test_data}/test_mwa.csv", latitude=-27).freqs()

    out, err = capfd.readouterr()
    assert "missing required arguments" in out
