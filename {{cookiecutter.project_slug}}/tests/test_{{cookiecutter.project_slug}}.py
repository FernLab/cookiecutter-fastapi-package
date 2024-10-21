#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else -%}
import unittest
{%- endif %}

import {{ cookiecutter.project_slug }}
{%- if cookiecutter.use_pytest == 'y' %}
import os
from fastapi.testclient import TestClient

from {{ cookiecutter.project_slug }}.create_app import app
import {{ cookiecutter.project_slug }}.core.env as environment

SERVICE_NAMESPACE = environment.SERVICE_NAMESPACE


class Test{{ cookiecutter.project_slug|title }}():

    @classmethod
    def setup_class(self):
        """Set up test fixtures."""
        self.app = TestClient(app)
        self.endpoint_prefix = ''

        if 'service_namespace' in os.environ and \
                os.environ['service_namespace'] == SERVICE_NAMESPACE:
            self.endpoint_prefix = f'{SERVICE_NAMESPACE}'

    def teardown_class(self):
        print("teardown_class called once for the class")

    def setup_method(self):
        print("setup_method called for every method")

    def teardown_method(self):
        print("teardown_method called for every method")

    def test_api_home_200(self):
        response = self.app.get(f"{self.endpoint_prefix}/")
        assert response.status_code == 200

    def test_api_home_404_url_not_found(self):
        response = self.app.get(f"{self.endpoint_prefix}/NotFound")
        assert response.status_code == 404

    def test_api_items_200(self):
        response = self.app.get(f"{self.endpoint_prefix}/item")
        assert response.status_code == 200

    def test_api_items_404_url_not_found(self):
        response = self.app.get(f"{self.endpoint_prefix}/item_NotFound")
        assert response.status_code == 404

    def test_api_item_by_id_200(self):
        response = self.app.get(f"{self.endpoint_prefix}/item/1")
        assert response.status_code == 200

    def test_api_item_by_id_404_not_found(self):
        response = self.app.get(f"{self.endpoint_prefix}/item/5")
        assert response.status_code == 404

    def test_api_item_by_id_404_url_not_found(self):
        response = self.app.get(f"{self.endpoint_prefix}/item_NotFound/5")
        assert response.status_code == 404


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function which prints the package version."""
    assert {{ cookiecutter.project_slug }}.__version__ == "{{ cookiecutter.version }}"
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- endif %}
