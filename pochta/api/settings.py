from typing import List

from pochta.utils import HTTPMethod


class Settings:
    def __init__(self, client) -> None:
        """
        Инициализация API Настроек.

        :param client: API клиент Доставки
        """
        self._client = client

    def user_shipping_points(self) -> List[dict]:
        """
        Текущие точки сдачи пользователя.

        :return: Возвращает список текущих точек сдачи.
        """
        url = '/1.0/user-shipping-points'

        res = self._client.request(HTTPMethod.GET, url)
        return res.json()

    def user_settings(self) -> dict:
        """
        Текущие настройки пользователя.

        :return: Все настройки пользователя
        """
        url = '/1.0/settings'

        res = self._client.request(HTTPMethod.GET, url)
        return res.json()
