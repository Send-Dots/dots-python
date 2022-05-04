import base64
import requests

import dots
from dots import token


class User():

    @classmethod
    def create(cls, email, country_code, phone_number, first_name, last_name, username=None):

        json = {
            'email': email,
            'country_code': country_code,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
        }

        if username is not None:
            json['username'] = username

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/users/create', json=json, headers=headers)
        response.raise_for_status()

        data = response.json()

        if (data['success']):
            return data['verification_id']
        else:
            response.raise_for_status()

    @classmethod
    def get(cls, user_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.get(
            dots.api_base + '/users/get/' + user_id, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['user']
        else:
            response.raise_for_status()

    @classmethod
    def send_verification_token(cls, verification_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/users/send_verification_token', json={'verification_id': verification_id}, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return True
        else:
            print(data.message)
            response.raise_for_status()

    @classmethod
    def verify_user(cls, verification_id, verification_token):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/users/verify_user', json={'verification_id': verification_id, 'verification_token': verification_token}, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['user']['id']
        else:
            return False

    @classmethod
    def get_wallet(cls, user_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.get(
            dots.api_base + '/users/wallet/get/' + user_id, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['wallet']
        else:
            response.raise_for_status()

    @classmethod
    def generate_refill_link(cls, user_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/users/wallet/refill', json={'user_id': user_id}, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success'] == True:
            return data['link']
        elif data['success'] == False:
            raise Exception(data.message)
        else:
            response.raise_for_status()

    @classmethod
    def generate_payout_link(cls, user_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/users/wallet/payout', json={'user_id': user_id}, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success'] == True:
            return data['link']
        elif data['success'] == False:
            raise Exception(data.message)
        else:
            response.raise_for_status()

    @classmethod
    def get_transactions(cls, user_id, page=None):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        query = ''
        if page is not None:
            query = '?page=' + str(page)

        response = dots._session.get(
            dots.api_base + '/transactions/get/user/' + user_id + query, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['transactions']
        else:
            response.raise_for_status()
