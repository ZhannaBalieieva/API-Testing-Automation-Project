from utils_1.api import Google_maps_api
from requests import Response
from utils_1.checking import Checking
import allure


@allure.epic('Test create place')
class Test_create_place():
    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):
        print('Method POST')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Method GET проверяет Method POST')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Method PUT')
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Method GET проверяет Method PUT')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('Method DELETE')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Method GET проверяет Method DELETE который уже должен быть 404')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')
