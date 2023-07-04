# syntax=docker/dockerfile:1

# Using the Ubuntu image (our OS)
FROM ubuntu:18.04

# Avoid questions on geography
ARG DEBIAN_FRONTEND=noninteractive

# Update package manager (apt-get) 
# and install (with the yes flag `-y`)
# Python and Pip
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip

ENV PYENV=production

# Copy our script into the container
COPY script.py /script.py

# Create directories
# RUN mkdir /input_test
COPY input_test /input_test
RUN mkdir /output_test

# Normally we'd also copy any requirements file
# COPY requirements.txt /requirements.txt

# And we would install our Python dependencies
# RUN pip install -r requirements.txt

# We can run the script immediately when the image is run, if we want.
# Alternatively, we should let this to the executing party?
# ENTRYPOINT ["python3", "/frequencies.py"]
