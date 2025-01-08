"""pjPyLib utils unittests."""

from pjpylib import utils


def test_simple_uuid():
    """Test simple_uuid()."""
    _uuid = utils.simple_uuid()
    assert isinstance(_uuid, str)

def test_make_uuid():
    """Test make_uuid()."""
    _uuid = utils.make_uuid(["test", "this"])
    assert isinstance(_uuid, str)
