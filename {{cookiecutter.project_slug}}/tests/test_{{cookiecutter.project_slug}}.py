#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam
"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import {{ cookiecutter.project_slug }}
from fastapi.testclient import TestClient

from {{ cookiecutter.project_slug }}.create_app import app


class Test{{ cookiecutter.project_slug|title }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    @classmethod
    def setup_class(cls):
        """Run once for the entire class to set up any state."""
        print("Setting up Test_{{ cookiecutter.project_slug|title }} class")

        cls.app = TestClient(app)
        cls.endpoint = 'test-service'

    @classmethod
    def teardown_class(cls):
        """Run once after all tests in the class have run."""
        print("Tearing down Test_{{ cookiecutter.project_slug|title }} class")

    def setup_method(self, method:callable):
        """
        Run before each test method to set up clean state.

        Parameters
        ----------
        method : callable
            The test method to set up for.

        Notes
        -----
        This method is called before each test method to ensure a clean state.
        """
        print(f"Setting up for {method.__name__}")

    def teardown_method(self, method:callable):
        """
        Run after each test method to clean up.

        Parameters
        ----------
        method : callable
            The test method to clean up after.

        Notes
        -----
        This method is called after each test method to clean up any resources.
        """
        print(f"Tearing down {method.__name__}")

    def test_api_home_200(self):
        """Test the API endpoint [GET] / for 200_OK."""
        response = self.app.get(f"{self.endpoint}/")
        assert response.status_code == 200

    def test_api_home_404_url_not_found(self):
        """Test the API endpoint [GET] / for 404_NOT_FOUND."""
        response = self.app.get(f"{self.endpoint}/NotFound")
        assert response.status_code == 404

    def test_api_items_200(self):
        """Test the API endpoint [GET] /item for 200_OK."""
        response = self.app.get(f"{self.endpoint}/item")
        assert response.status_code == 200

    def test_api_items_404_url_not_found(self):
        """Test the API endpoint [GET] /item for 404_NOT_FOUND."""
        response = self.app.get(f"{self.endpoint}/item_NotFound")
        assert response.status_code == 404

    def test_api_item_by_id_200(self):
        """Test the API endpoint [GET] /item/{id} for 200_OK."""
        response = self.app.get(f"{self.endpoint}/item/1")
        assert response.status_code == 200

    def test_api_item_by_id_404_not_found(self):
        """Test the API endpoint [GET] /item/{id} for 404_NOT_FOUND."""
        response = self.app.get(f"{self.endpoint}/item/5")
        assert response.status_code == 404

    def test_api_item_by_id_404_url_not_found(self):
        """Test the API endpoint [GET] /item/{id} for 404_NOT_FOUND."""
        response = self.app.get(f"{self.endpoint}/item_NotFound/5")
        assert response.status_code == 404
