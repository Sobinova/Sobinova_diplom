import sender_stand_request
import data


def test_get_order_by_track_number():
    new_order = sender_stand_request.post_order()
    track = sender_stand_request.get_track()
    order_back = sender_stand_request.get_order(data.body)
    assert order_back.status_code == 200


test_get_order_by_track_number()

