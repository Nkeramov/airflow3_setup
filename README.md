# Airflow 3 setup example

This repository contains a basic setup for running Apache Airflow 3 using Docker. It includes:

- Dockerfile – Custom Airflow image with additional dependencies.
- docker-compose.yaml – Preconfigured services (scheduler, webserver, postgres, redis).
- .env – Environment variables (credentials, configurations).
- requirements.txt – Python dependencies for Airflow.

## Quick Start

1. Clone the repository.
2. Run the following command to build and start Airflow: `docker compose up --build`
3. Access the Airflow UI at: 🔗 http://localhost:8080
4. Use the credentials from .env.
