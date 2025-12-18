# Airflow 3 Setup Example

<div align="center">
    <img src="apache-airflow-logo.png" height="200">
</div>

This repository contains a basic setup for running Apache Airflow 3 using Docker.

It includes:
- Dockerfile – Custom Airflow image with additional dependencies.
- docker-compose.yaml – Preconfigured services (scheduler, webserver, postgres).
- .env – Environment variables (credentials, configurations).
- requirements.txt – Python dependencies for Airflow.

## 🚀 Quick Start

### Prerequisites
Clone repository:
```bash 
git clone https://github.com/Nkeramov/airflow3_setup.git
```
Switch to repo directory:
```bash 
cd airflow3_setup
```

### Configutation

The configuration file is located in the `.env` file. You can copy the `env.example` to `.env` and make your edits.
```bash
cp env.example .env
```

Generate JWT secret and Fernet key by running the `setup_env.py` script or add existing ones manually.
```
python3 setup_env.py
```

### Running

Run the following command to build and start Airflow: `docker compose up --build`

### Access

Access the Airflow UI at: 🔗 http://localhost:8080

## 🤝 Contributing

If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and create a pull request.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📚 References 

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Airflow® 3 is Generally Available!](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/)
