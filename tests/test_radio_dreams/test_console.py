import click.testing
import pytest
from radio_dreams import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_radio_dreams_succeeds(runner):
    result = runner.invoke(console.radio_dreams)
    assert result.exit_code == 0
