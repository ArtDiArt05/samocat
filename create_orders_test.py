import sender_stand_request
import data
import requests

# Дмитрий Артемов, 28-я когорта — Финальный проект. Инженер по тестированию плюс

def test_create_orders():
    response = sender_stand_request.post_new_orders(data.orders_body)
    track = response.json()["track"]
    response = sender_stand_request.get_orders_track(track)
    assert response.status_code == 200