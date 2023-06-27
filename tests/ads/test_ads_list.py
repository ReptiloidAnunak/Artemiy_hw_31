import pytest

from tests.factories import AdFactory
from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdFactory.create_batch(5)
    response = client.get("/ad/")
    resp_res = []
    for item in response.data["results"]:
        resp_res.append(item)

    exp_resp = []
    for item in AdSerializer(ads, many=True).data:
        exp_resp.append(item)

    assert response.status_code == 200
    assert resp_res == exp_resp
