"""
Модуль для работы с API OpenWeather
"""

from typing import Dict, Any
import aiohttp


class WeatherAPI:
    """
    Класс-обертка для работы с API open-weather
    """

    def __init__(self, api_endpoint: str) -> None:
        """
        Инициализирует объект WeatherAPI
        Args:
            api_endpoint (str): URL для обращения к API
        """
        self.api_endpoint = api_endpoint

    async def fetch_weather_data(self, params: Dict[str, Any]) -> Dict:
        """
        Метод для получения данных о погоде
        Args:
            params (List[Tuple]): Список параметров запроса
        Return:
            data (Dict): Результат запрос
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_endpoint, params=params) as response:
                data = await response.json()
                return data
