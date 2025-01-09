"""pjPyLib Utilities."""

import hashlib
import uuid

FLAKE8_MAX_LINE_LENGTH_TEST = "This line is longer than 80 characters intentionally to check if flake8 pick it up as a failure or not."


def simple_uuid() -> str:
    """Return a simple UUID."""
    return str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1())))


def make_uuid(values: list) -> str:
    """Make a UUID from an MD5 hash of a list of values."""
    preShaMd5 = "-".join([str(value) for value in values])
    result = hashlib.md5(preShaMd5.encode())
    return str(uuid.UUID(result.hexdigest()))
