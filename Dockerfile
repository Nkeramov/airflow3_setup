# Image: Apache Airflow with Python dependencies
# This Dockerfile builds an Apache Airflow image with additional Python dependencies.
FROM apache/airflow:3.1.5

# Install dependencies for building Python packages
# Use the root user to install system dependencies
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \    
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    krb5-user \
    krb5-config \
    libkrb5-dev \
    libgssapi-krb5-2 \
    libsasl2-modules-gssapi-mit \
    && apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Switch to airflow user for Python package installation
USER airflow

# Copy the requirements file
# This file should be in the same directory as the Dockerfile
COPY requirements.txt /requirements.txt

# Install Python dependencies in a single layer
RUN pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir -r /requirements.txt

# Ensure we're running as airflow user
USER airflow
