#!/usr/bin/env python3

import pytest
from byte_formatter import format_size


def test_format_size_binary():
    assert format_size(1024, binary=True) == "1.0 KiB"


def test_format_size_decimal():
    assert format_size(1000) == "1.0 KB"


def test_format_size_verbose():
    assert format_size(1024, binary=True, verbose=True) == "1.0 Kibibytes"


def test_negative_size():
    with pytest.raises(ValueError):
        format_size(-1)


def test_negative_precision():
    with pytest.raises(ValueError):
        format_size(1024, precision=-1)
