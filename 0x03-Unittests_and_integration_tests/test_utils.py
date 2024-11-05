#!/usr/bin/env python3
"""testing utils functions."""
from parameterized import parameterized
from utils.py import access_nested_map
import unittest
from typing import (
        Mapping,
        Sequence,
        Any,
)


class TestAessNestedMap(unittest.TastCase):
    """Teatting utils functions and classes."""

    @parameterized.expand([
        ({"a": 1}, ("a")),
        ({"a": {"b": 2}}, ("a")),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(nm: Mapping, pt: Sequence, result: Any) -> Any:
        """test method for access_nested_map function."""
        self.assertEqual(access_nested_map(nm, pt), result)


if __name__ == "__main__":
    unittest.main()
