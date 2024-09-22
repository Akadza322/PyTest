import requests
import pytest

class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth y0_AgAAAAB446_BAADLWwAAAAERzsmHAACTyfNsMTJMWa2De5IvR1dusst3EQ'
        }

    @pytest.mark.parametrize(
        'param, value, status_code',
        (
            ['path', 'Image', 201],
            ['pat', 'Image', 400],
            ['path', 'Image', 409]
        )
    )
    def test_create_folder(self, param, value, status_code):
        params = {param: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers, params=params)
        assert response.status_code == status_code