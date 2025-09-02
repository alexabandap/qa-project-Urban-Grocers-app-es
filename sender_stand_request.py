import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body, headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
auth_token = response.json()["authToken"]
print("Token obtenido:", auth_token)

def post_new_client_kit(kit_body, auth_token):
    headers= data.headers.copy()
    headers["Authorization"] =  f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=kit_body, headers=headers)
print("Kit body:", data.kit_body)
response = post_new_client_kit(data.kit_body, auth_token)
print(response.status_code)
print(response.json())

def get_new_user_token(user_body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body, headers=data.headers)

    print(response.status_code)
    print(response.json())

    return response.json()["authToken"]
auth_token = get_new_user_token(data.user_body)
print("Token obtenido:", auth_token)

