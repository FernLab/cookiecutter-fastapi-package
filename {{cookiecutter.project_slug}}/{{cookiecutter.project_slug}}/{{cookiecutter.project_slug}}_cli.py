#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam
"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}

import argparse
{%- endif %}
import sys

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}


def get_argparser():
    """
    Get a console argument parser for {{ cookiecutter.project_name }} and return them as `argparse.ArgumentParser`.

    Returns
    -------
    argparse.ArgumentParser
        The argument parser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")

    return parser


def main():
    """
    Console script for {{cookiecutter.project_slug}}.

    Returns
    -------
    int
        The exit code.
    """
    argparser = get_argparser()
    parsed_args = argparser.parse_args()

    print("Arguments: " + str(parsed_args._))
    print("Replace this message by putting your code into {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}_cli")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
