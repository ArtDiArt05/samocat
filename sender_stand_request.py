import configuration
import requests
import data

def post_new_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=orders_body) 
def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))



