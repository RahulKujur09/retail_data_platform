import pytest

from src.common.reader import read_data

def test_invalid_format():
    config = {
        "source" : {
            "format" : "json",
            "path" : "dummy_path"
        }
    }

    with pytest.raises(ValueError):
        read_data(None, config)