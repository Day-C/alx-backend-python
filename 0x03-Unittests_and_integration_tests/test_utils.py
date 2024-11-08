#!/usr/bin/env python3
"""testing utils functions."""
from parameterized import parameterized
from utils import access_nested_map
import unittest
from typing import (
        Mapping,
        Sequence,
        Any,
)


class TestAessNestedMap(unittest.TestCase):
    """Teatting utils functions and classes."""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result) -> Any:
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
