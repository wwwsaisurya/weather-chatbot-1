from abc import ABC, abstractmethod
from typing import Dict, Any


class City(ABC):
    """Abstraction of a city weather data records."""

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def temp(self) -> float:
        pass

    @abstractmethod
    def country(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Summary(ABC):
    """Abstraction of a summary."""

    @abstractmethod
    def get(self) -> Dict[str, Any]:
        pass


class CityWeather(City):
    """Some city weather data records."""

    def __init__(self, weather_data: Dict[Any, Any]) -> None:
        self._weather_data: Dict[Any, Any] = weather_data

    def description(self) -> str:
        return self._weather_data.get('weather')[0].get('description')

    def temp(self) -> float:
        return self._weather_data.get('main').get('temp')

    def country(self) -> str:
        return self._weather_data.get('sys').get('country')

    def name(self) -> str:
        return self._weather_data.get('name')


class CityWeatherSummary(Summary):
    """City weather summary."""

    def __init__(self, weather_data: Dict[Any, Any]) -> None:
        self._city_weather: City = CityWeather(weather_data)

    def get(self) -> Dict[str, Any]:
        return dict(
            description=self._city_weather.description(),
            temperature=self._city_weather.temp(),
            country=self._city_weather.country(),
            name=self._city_weather.name()
                    )
