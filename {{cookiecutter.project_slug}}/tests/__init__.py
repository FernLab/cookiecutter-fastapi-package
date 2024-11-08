# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Unit test package for {{ cookiecutter.project_slug }}."""

import os

import {{ cookiecutter.project_slug }}

ROOT_DIR = \
    os.path.abspath(os.path.join(
        os.path.dirname({{ cookiecutter.project_slug }}.__file__), ".."))

os.environ['service_namespace'] = 'test-service'

