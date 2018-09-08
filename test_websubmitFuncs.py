#!/usr/bin/env python3
import unittest
import websubmitFuncs


class TestWebsubmitFuncs(unittest.TestCase):

    def test_get_filename_from_url(self):
        url = "https://campus.datacamp.com/courses/data-types-for-data-science/fundamental-data-types?ex=3"  # noqa: E501
        filename = "FunDatTypEx3.py"
        self.assertEqual(
                websubmitFuncs.get_filename_from_url(url),
                filename)


if __name__ == '__main__':
    unittest.main()
