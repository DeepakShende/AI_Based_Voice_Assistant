#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests helper methods."""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import unittest
import nose

from google.modules.utils import _get_search_url


class UtilsTestCase(unittest.TestCase):
    """Tests for helper methods."""

    def test_get_search_url(self):
        url = _get_search_url("apple", 0, 10, "en")
        exp_url = "http://www.google.com/search?q=apple&start=0&num=10&nl=en"
        self.assertEqual(url, exp_url)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
