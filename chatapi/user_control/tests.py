from rest_framework.test import APITestCase

from user_control.views import get_random, get_access_token, get_refresh_token

# Create your tests here.

class TestGenericFunction(APITestCase):

    def test_get_random(self):
        rand1 = get_random(10)
        rand2 = get_random(10)
        rand3 = get_random(15)

        # Check that we are getting a result
        self.assertTrue(rand1)

        # Check that rand1 is not equal to rand2
        self.assertNotEqual(rand1, rand2)

        # CHeck that the length of result is what is expected
        self.assertEqual(len(rand1), 10)
        self.assertEqual(len(rand3), 15)

    def test_get_access_token(self):
        payload = {
            'id': 1
        }

        token = get_access_token(payload=payload)

        # Check that we obtained result
        self.assertTrue(token)

    def test_get_refresh_token(self):

        token = get_refresh_token()

        # Check that we obtained result
        self.assertTrue(token)


class TestAuth(APITestCase):

    login_url = '/user/login/'
    register_url = '/user/register/'
    refresh_url = 'user/refresh/'

    def test_register(self):
        payload = {
            'username': 'the_tk_official',
            'password': 'the_tk_off1c1al'
        }

        response = self.client.post(self.register_url, data=payload)

        # Check that we obtain a status of 201
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        payload = {
            'username': 'the_tk_official',
            'password': 'the_tk_off1c1al'
        }

        # Register
        self.client.post(self.register_url, data=payload)

        response = self.client.post(self.login_url, data=payload)

        # Check that we obtain a status of 201
        self.assertEqual(response.status_code, 200)

        # Check that we obtained both the refresh and access token
        result = response.json()
        self.assertTrue(result['access'])
        self.assertTrue(result['refresh'])

    def test_refresh(self):
        payload = {
            'username': 'the_tk_official',
            'password': 'the_tk_off1c1al'
        }

        # Register
        self.client.post(self.register_url, data=payload)

        response = self.client.post(self.login_url, data=payload)
        refresh = response.json()['refresh']

        # Get refresh
        responce = self.client.post(self.refresh_url, data={'refresh': refresh})

        # Check that we obtain a status of 201
        self.assertEqual(response.status_code, 200)

        # Check that we obtained both the refresh and access token
        result = response.json()
        self.assertTrue(result['access'])
        self.assertTrue(result['refresh'])
