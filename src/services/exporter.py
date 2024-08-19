import pandas as pd
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.weather_schema import WeatherData


class Exporter:
    """
    Класс для экспорта данных о погоде в файл Excel.
    """

    def __init__(self, path) -> None:
        """
        Инициализирует объект Exporter.
        Args:
            path (str): Путь к директории для сохранения файла Excel.
        """
        self.path = path  # os path

    async def export_to_excel(self, session: AsyncSession):
        """
        Экспортирует последние 10 записей о погоде из базы данных в файл Excel.

        Args:
            session: Объект сессии SQLAlchemy для взаимодействия с базой данных.
        """
        query = select(WeatherData).order_by(WeatherData.id.desc()).limit(10)
        result = await session.execute(query)
        weather_data = result.scalars().all()

        df = pd.DataFrame(
            [
                (
                    wd.temperature,
                    wd.wind_direction,
                    wd.wind_speed,
                    wd.pressure,
                    wd.precipitation,
                )
                for wd in weather_data
            ],
            columns=[
                "Temperature",
                "Wind Direction",
                "Wind Speed",
                "Pressure",
                "Precipitation",
            ],
        )
        df.to_excel(f"{self.path}/weather_data.xlsx", index=False)
