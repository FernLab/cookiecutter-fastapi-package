# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam
"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """ {{ cookiecutter.full_name }} """
__email__ = " {{ cookiecutter.email }} "

from .version import __version__

__all__ = ["__version__"]
