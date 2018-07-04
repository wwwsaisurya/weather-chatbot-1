from abc import ABC, abstractmethod
from typing import Dict
from bin.forecast import WEATHER_ID
from bin.web_api.requests import Request, SafeBotRequest
from bin.web_api.urls import CommonUrl


class Weather(ABC):
    """Abstraction of a weather."""

    @abstractmethod
    def data_records(self) -> Dict[str, str]:
        pass


class EmptyWeatherDataOf(Weather):
    """Represent empty weather data."""

    def __init__(self, weather: Weather) -> None:
        self._weather: Weather = weather

    def data_records(self) -> Dict[str, str]:
        try:
            return self._weather.data_records()
        except IndexError:
            pass


class OpenWeatherMap(Weather):
    """Concrete weather object."""

    def __init__(self, city: str) -> None:
        self._req: Request = SafeBotRequest(
            CommonUrl('http://api.openweathermap.org/data/2.5/weather?q=', city, '&units=metric&appid=', WEATHER_ID))

    def data_records(self) -> Dict[str, str]:
        return self._req.get().json()
