"""
Модуль-раннер
"""

import os
import asyncio
import aioconsole
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from services.weather_api import WeatherAPI
from services.exporter import Exporter
from db_config import async_session_maker
from models.weather_schema import WeatherData
from utils import get_weather_data

weather_api = WeatherAPI(
    api_endpoint="http://api.openweathermap.org/data/2.5/weather",
)

excel_exporter = Exporter(path=os.path.dirname(os.path.abspath(__file__)))


async def fetch_and_add_weather_data(lat: str, lon: str, appid: str):
    """
    Получает данные о погоде из API и добавляет их в базу данных.

    Args:
        lat (str): Широта местоположения.
        lon (str): Долгота местоположения.
        appid (str): ключ API для доступа к данным о погоде.
    """
    session = async_session_maker()
    while True:
        data = await weather_api.fetch_weather_data(
            params={
                "lat": lat,
                "lon": lon,
                "appid": appid,
            }
        )
        query = insert(WeatherData).values(get_weather_data(data))
        await session.execute(query)
        await session.commit()
        await asyncio.sleep(180)

        await session.close()


async def handle_export_command(session: AsyncSession):
    """
    Обработчик команды экспорта данных в Excel

    Args:
        session (AsyncSession): Асинхронная сессия подключения к БД
    """
    while True:
        command = await aioconsole.ainput(
            "Введите 'export' для экспорта данных в Excel: "
        )
        if command.strip().lower() == "export":
            await excel_exporter.export_to_excel(session)
        else:
            print("Неверная команда. Попробуйте снова.")


async def main():
    export_task = asyncio.create_task(
        handle_export_command(session=async_session_maker())
    )
    await fetch_and_add_weather_data(
        lat="55.698539",
        lon="37.359577",
        appid="77ef2f83676a9a70bff26e3d90ea02c1",
    )


if __name__ == "__main__":
    asyncio.run(main())
