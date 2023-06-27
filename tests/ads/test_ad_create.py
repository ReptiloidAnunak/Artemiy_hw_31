import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    response = client.post("/ad/create/",
                           {
                               "name": "Кнедлики с огуречной жижей",
                               "author": user.id,
                               "price": 66,
                               "description": "Восхитительное кушанье из лучших салонов Петрограда",
                               "category": category.id
                           },
                           content_type="application/json")

    expected_response = {
            "name": "Кнедлики с огуречной жижей",
            "author": user.id,
            "price": 66,
            "description": "Восхитительное кушанье из лучших салонов Петрограда",
            "category": category.id,
            "is_published": False,
            "image": None
             }

    assert response.status_code == 201
    assert response.data == expected_response
