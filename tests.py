import json

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory, RequestsClient
from murr_card.models import MurrCard
Murren = get_user_model()

"""решить проблему  "одного" пользователя, существует только 1 юзер, для теста с невалидными данными нужно 2. """
"""не прилетает параметр 204"""

@pytest.mark.django_db
def test_delete_murr_valid_params(create_murren, create_murr):
    user1 = create_murren
    murr1 = create_murr.title
    client = APIClient()
    delete_path = reverse('MurrCardView')
    user_request = client.delete(delete_path, data={'murr_id': 1, 'owner_id': 1}, format='json')
    assert user_request.status_code == 204

@pytest.mark.django_db
def test_delete_murr_invalid_params(create_murren, create_murr):
    user1 = create_murren
    murr1 = create_murr.title
    client = APIClient()
    delete_path = reverse('MurrCardView')
    user_request = client.delete(delete_path, data={'murr_id': 1, 'owner_id': 2}, format='json')
    assert user_request.status_code == 400
