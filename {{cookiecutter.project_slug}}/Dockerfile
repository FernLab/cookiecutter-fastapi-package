#syntax=docker/dockerfile:experimental
# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


# # Container for building the environment
FROM condaforge/miniforge3:latest
RUN apt-get update -y

# Create mamba environment
COPY /tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml /root/
RUN mamba env create -f /root/environment_{{ cookiecutter.project_slug }}.yml

# Activate the environment
SHELL ["conda", "run", "-n", "{{ cookiecutter.project_slug }}", "/bin/bash", "-c"]

# Install Package
ADD . /{{ cookiecutter.project_slug }}/
RUN pip install -e /{{ cookiecutter.project_slug }}/

# Change working directory to help fastapi to find package
WORKDIR /{{ cookiecutter.project_slug }}

# Run the application using FastAPI CLI
CMD fastapi run {{ cookiecutter.project_slug }}/create_app.py --host 0.0.0.0 --port 8881

# These are not working!!!
# CMD ["fastapi", "run", "{{ cookiecutter.project_slug }}/create_app.py", "--host", "0.0.0.0", "--port", "8881"]