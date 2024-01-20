import requests

url_path_yandex = 'https://cloud-api.yandex.net'
token_yandex_disk = ""


def create_a_folder(yandex_token, name_dir):
        headers = {"Authorization": f'OAuth {yandex_token}'}
        params = {'path': name_dir}
        response = requests.put(f'{url_path_yandex}/v1/disk/resources', params=params, headers=headers)
        return response.status_code

