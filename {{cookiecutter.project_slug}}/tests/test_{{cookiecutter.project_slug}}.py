#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import {{ cookiecutter.project_slug }}
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
    See more at: https://doc.pytest.org/en/latest/explanation/fixtures.html
    """

def test_content(response):
    """Sample pytest test function which prints the package version."""
    assert {{ cookiecutter.project_slug }}.__version__ == "{{ cookiecutter.version }}"


class Test{{ cookiecutter.project_slug|title }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    @classmethod
    def setup_class(cls):
        """Run once for the entire class to set up any state."""
        print("Setting up Test_{{ cookiecutter.project_slug|title }} class")

    @classmethod
    def teardown_class(cls):
        """Run once after all tests in the class have run."""
        print("Tearing down Test_{{ cookiecutter.project_slug|title }} class")

    def setup_method(self, method):
        """Run before each test method to set up clean state."""
        print(f"Setting up for {method.__name__}")

    def teardown_method(self, method):
        """Run after each test method to clean up."""
        print(f"Tearing down {method.__name__}")

    def test_000_something(self):
        """Test something."""
        print({{ cookiecutter.project_slug }}.__version__)
