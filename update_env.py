import os
import secrets
from cryptography.fernet import Fernet


def update_env(env_file='.env'):
    if not os.path.exists(env_file):
        print(f"File {env_file} not found!")
        return

    jwt_secret = secrets.token_urlsafe(32)
    fernet_key = Fernet.generate_key().decode()

    with open(env_file, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'AIRFLOW__API_AUTH__JWT_SECRET=' in content:
        content = content.replace(
            'AIRFLOW__API_AUTH__JWT_SECRET=',
            f'AIRFLOW__API_AUTH__JWT_SECRET={jwt_secret}'
        )
    else:
        content += f'\nAIRFLOW__API_AUTH__JWT_SECRET={jwt_secret}\n'

    if 'AIRFLOW__CORE__FERNET_KEY=' in content:
        content = content.replace(
            'AIRFLOW__CORE__FERNET_KEY=',
            f'AIRFLOW__CORE__FERNET_KEY={fernet_key}'
        )
    else:
        content += f'AIRFLOW__CORE__FERNET_KEY={fernet_key}\n'

    with open(env_file, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{env_file} updated!")
    print(f"🔑 JWT Secret: {jwt_secret}")
    print(f"🔑 Fernet Key: {fernet_key}")

if __name__ == "__main__":
    update_env()
