"""
Описание схемы моделей БД
"""

from sqlalchemy import JSON, Numeric, String
from sqlalchemy.orm import mapped_column, Mapped

from db_config import Base


class WeatherData(Base):
    """
    Класс, представляющий данные о погоде, хранящиеся в базе данных.

    id (int): Уникальный идентификатор записи.
    temperature (float): Температура в градусах Цельсия.
    wind_direction (str): Направление ветра (например, "Север", "Юго-Запад").
    wind_speed (float): Скорость ветра в метрах в секунду.
    pressure (float): Атмосферное давление в мм ртутного столба.
    precipitation (dict): Информация об осадках, включая:
        - type (str): Тип осадков (например, "rain", "snow").
        - amount (float): Количество осадков за последний час (в мм).

    """

    __tablename__ = "weather_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column(
        doc="Температура",
        type_=Numeric(4, 2),
        nullable=False,
    )
    wind_direction: Mapped[str] = mapped_column(
        doc="Направление ветра",
        type_=String(),
        nullable=False,
    )
    wind_speed: Mapped[float] = mapped_column(
        doc="Скорость ветра",
        type_=Numeric(4, 2),
        nullable=False,
    )
    pressure: Mapped[float] = mapped_column(
        doc="Давление", type_=Numeric(5, 2), nullable=False
    )
    precipitation: Mapped[str] = mapped_column(
        doc="Осадки", type_=String(), nullable=True
    )
    precipitation: Mapped[dict] = mapped_column(
        doc="Осадки и их кол-во",
        type_=JSON(),
        nullable=True,
    )
