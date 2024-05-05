"""
Конфигурация приложения
"""
from pydantic_settings import BaseSettings
from pydantic import root_validator


class Settings(BaseSettings):

    # FIXME Спрятать значения по умолчанию
    OPEN_WEATHER_API_KEY: str = '77ef2f83676a9a70bff26e3d90ea02c1'

    DB_USER: str = 'postgres'
    DB_PASSWORD: int = '1469'

    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432

    DB_NAME: str = 'postgres'

    DB_URL: str = None

    @root_validator(pre=True, skip_on_failure=False)
    def generate_db_url(cls, value):
        value['DB_URL'] = f"postgresql+asyncpg://{value.get('DB_USER')}:{value.get('DB_PASSWORD')}@{value.get('DB_HOST')}:{value.get('DB_PORT')}/{value.get('DB_NAME')}"
        return value

    class Config:
        """
        Подкласс конфигурации для BaseSettings
        """
        env_file = '.env'

settings = Settings()
