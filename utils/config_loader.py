import os
from dotenv import load_dotenv
import yaml

def load_config(env_name="local", project_root=None):
    # Если project_root не передан, берём текущую рабочую директорию
    if project_root is None:
        project_root = os.getcwd()  # для Jupyter это директория, откуда запущен ноутбук

    # Загружаем .env
    load_dotenv(os.path.join(project_root, ".env"))

    # Путь к YAML
    config_path = os.path.join(project_root, "config.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as f:
        yaml_config = yaml.safe_load(f)[env_name]

    # Добавляем приватные настройки
    yaml_config["MONGO_URI"] = os.getenv("MONGO_URI")
    yaml_config["QDRANT_URL"] = os.getenv("QDRANT_URL")

    return yaml_config
