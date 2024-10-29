# # SPDX-License-Identifier: MIT
# # FileType: SOURCE
# # FileCopyrightText: 2024, FernLab at GFZ Potsdam


# # Container for building the environment
FROM condaforge/miniforge3:latest
RUN apt-get update -y

# Create mamba environment
COPY /tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml /root/
RUN mamba env create -f /root/environment_{{ cookiecutter.project_slug }}.yml

# Activate the environment
SHELL ["conda", "run", "-n", "{{ cookiecutter.project_slug }}", "/bin/bash", "-c"]

# Copy source code
COPY . /{{ cookiecutter.project_slug }}
RUN rm -rf /{{ cookiecutter.project_slug }}/tests

# Change directory to /{{ cookiecutter.project_slug }}
ENV APP_HOME /{{ cookiecutter.project_slug }}/
WORKDIR $APP_HOME