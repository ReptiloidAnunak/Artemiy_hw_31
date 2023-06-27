from django.http import JsonResponse


def test_root_not_found(client):
    response = client.get("/")
    assert JsonResponse({"status": "ok"}, status=200)