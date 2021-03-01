{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{subgroup}}/{{slug}}{%- endset -%}
{% else -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{slug}}{%- endset -%}
{% endif -%}
#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

version = {}
with open("{{ cookiecutter.project_slug }}/version.py") as version_file:
    exec(version_file.read(), version)

req = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %}]

req_setup = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %}]

req_test = ['coverage', 'nose', 'nose2', 'nose-htmloutput', {%- if cookiecutter.use_pytest == 'y' %} 'pytest>=3',{%- endif %} 'rednose', 'urlchecker']

req_doc = ['sphinx-argparse', 'sphinx_rtd_theme', 'sphinx-autodoc-typehints']

req_lint = ['flake8', 'pycodestyle', 'pydocstyle']

req_dev = req_setup + req_test + req_doc + req_lint

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}=bin.{{ cookiecutter.project_slug }}_cli:main',
        ],
    },
    {%- endif %}
    extras_require = {
        "doc": req_doc,
        "test": req_test,
        "lint": req_lint,
        "dev": req_dev
    },
    install_requires=req,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    long_description = readme,
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    setup_requires=req_setup,
    test_suite='tests',
    tests_require=req_test,
    url='{{ projecturl }}',
    version=version['__version__'],
    zip_safe=False,
)
