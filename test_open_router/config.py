from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_BASE: str | None = None
    API_KEY: str
    API_MODEL: str = 'gpt-5-mini'
    model_config = SettingsConfigDict(env_file=".env")

cnf = Settings()
