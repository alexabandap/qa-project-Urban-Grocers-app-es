

import sender_stand_request
import data
from sender_stand_request import (auth_token, get_new_user_token)


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body ["name"] = name
    return current_body


def positive_assert(name):
    auth_token = get_new_user_token(data.user_body)
    kit_body = get_kit_body(name)
    response= sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]
    #assert response.json()["authToken"] == auth_token

def negative_assert_code_400(name):
    auth_token = get_new_user_token(data.user_body)
    kit_body = get_kit_body(name)
    response= sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    #assert response.json()["authToken"] == auth_token
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.json()}")


#Prueba 1

def test_1_caractere_get_success_response():
    positive_assert("a")

#Prueba 2
def test_511_caractere_get_error_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3
def test_0_caractere_get_error_response():
    negative_assert_code_400("")

#Prueba 4
def test_512_caractere_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5
def test_special_caractere_get_success_response():
    positive_assert("!№%@," )

#Prueba 6
def test_has_space_get_success_response():
    positive_assert(" A Aaa " )

#Prueba 7
def test_numbers_get_success_response():
    positive_assert("123")

#Prueba 8
def test_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

#Prueba 9
def test_different_parameter_number_get_error_response():
    negative_assert_code_400(123)

