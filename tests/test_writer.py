import pytest

from src.common.writer import write_data


def test_invalid_writer():

    config = {
        "destination": {
            "format": "json",
            "path": "dummy"
        }
    }

    with pytest.raises(ValueError):
        write_data(None, config)