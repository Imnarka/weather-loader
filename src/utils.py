"""
Разлчные утилиты
"""
def get_wind_direction_str(deg: int) -> str:
    """
    Преобразование DEG в направление 
    (Север, Юг, Запад, восток) и производные
    Args:
        deg (int): значение в грудсах
    Return:
        drirection (str): направление
    """
    directions = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
    index = int((deg + 22.5) / 45) % 8
    return directions[index]


def get_weather_data(data: dict) -> dict:
    """
    Маппинг полученных данных
    Args:
        data (dict): словарь данных, полученный от API
    Return:
        weather_data (dict): отфильтрованный словарь данных для БД 
    """
    precipitation_mapping = { 
        "rain": data.get("rain", {}), 
        "snow": data.get("snow", {}), 
    }
    
    weather_data = { 
        "temperature": data['main']['temp'] - 273.15, 
        "wind_direction": get_wind_direction_str(data['wind']['deg']), 
        "wind_speed": data['wind']['speed'], 
        "pressure": data['main']['pressure'] * 0.75, 
    }

    precipitation_type = next((key for key, value in precipitation_mapping.items() if value), None)
    if precipitation_type:
        precipitation_amount = precipitation_mapping[precipitation_type].get("1h", 0)
        weather_data["precipitation"] = {"type": precipitation_type, "amount": precipitation_amount}

    return weather_data
