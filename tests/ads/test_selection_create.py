import pytest
from ads.models import Ad


def test_selection_create(client, user_token, ad, user):
    response = client.post("/selection/create/",
                           {
                            "name": "Подборка Пахома",
                            "owner": user.id,
                            "items": [ad.id]
                            },
                           content_type = "application/json",
                           HTTP_AUTHORIZATION="Bearer " + user_token)

    expected_response = {
                        "id": 1,
                        "name": "Подборка Пахома",
                        "owner": user.id,
                        "items": [ad.id]
                        }
    assert response.status_code == 201
    assert response.data == expected_response
