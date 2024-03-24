import configuration
import requests
import data


def post_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.body,
                         headers=data.headers)


def get_track():
    response = post_order()
    track = response.json()['track']
    return track


def get_order(body):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_BY_TRACK_NUMBER + str(get_track()),
                        json=data.body, headers=data.headers)
