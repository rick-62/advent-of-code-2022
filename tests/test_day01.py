#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_advent_of_code_2022
----------------------------------

Tests for `advent_of_code_2022` module.
"""

import pytest


from advent_of_code_2022 import day01


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
