from django.contrib.auth import get_user_model
from django.urls import reverse
from murr_card.models import MurrCard
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

Murren = get_user_model()

class MurrTests(APITestCase):
    def setUp(self):
        user1 = Murren.objects.create_user(
                                           username='dan',
                                           password='12345',
                                           email='integrity@mail.com')
        user1.save()
        user2 = Murren.objects.create_user(
                                          username='Frost',
                                          password='1q2w3e',
                                          email='integrity1@mail.com')
        user2.save()
        self.one_murr = MurrCard.objects.create(
            title=1,
            content="hello, it's me",
            owner=user1,
        )
        self.two_murr = MurrCard.objects.create(
            title=2,
            content="Halo, dat's not me",
            owner=user2,
        )
    """Удаление мурра, где  id user1 = 1, аутентифицирую его с помощью force-login(не требует генерации токенов)"""
    """Возвращает 204, удаление прошло успешно. Я не стал передавать иные параметры, так как удаление просто не проходит, выводит ошибку типа данных"""
    def test_delete_murr_valid_params(self):
        user1 = Murren.objects.get(pk=1)
        self.client.force_login(user=user1)
        delete_path = reverse('MurrCardView')
        user_request = self.client.delete(delete_path, data={'murr_id': 1, 'owner_id': 1}, format='json')
        self.assertEqual(user_request.status_code, 204)
        
    """Удаление с неправильными параметрами id user2 = 2, возвращает 400, так как owner_id должен быть 1."""
    def test_delete_murr_invalid_params(self):
        user2 = Murren.objects.get(pk=2)
        self.client.force_login(user=user2)
        delete_path = reverse('MurrCardView')
        user_request = self.client.delete(delete_path, data={'murr_id': 1, 'owner_id': 1}, format='json')
        self.assertEqual(user_request.status_code, 400)

    """Оба теста проходят"""
    
    
    
    """Это функция принудительной генерпции токена и можно обойтись без её использования, я  сглупил когда решил её добавить"""
#    def manually_generate_token(user):
#
#        refresh = RefreshToken.for_user(user)
#        print(refresh.access_token)
#
#        return {
#            'refresh': str(refresh),
#            'access': str(refresh.access_token),
#        }
#   manually_generate_token(user=user7)
