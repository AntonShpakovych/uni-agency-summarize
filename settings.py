from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_name: str
    max_length: int
    min_length: int
    redis_url: str
    model_config = SettingsConfigDict(
        env_file=".env",
        protected_namespaces=["settings_"]
    )
