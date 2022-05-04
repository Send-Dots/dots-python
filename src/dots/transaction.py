import base64
import requests

import dots
from dots import token


class Transaction():

    @classmethod
    def create(cls, user_id, amount, receipt=None, breakdown=None, notes=None, allow_debit=False):

        json = {
            'user_id': user_id,
            'amount': amount,
            'receipt': receipt,
            'breakdown': breakdown,
            'notes': notes,
            'allow_debit': allow_debit
        }

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(
            dots.api_base + '/transactions/create', json=json, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data['success']:
            return data['transaction']
        else:
            raise Exception(data['message'])

    @classmethod
    def get(cls, transaction_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.get(
            dots.api_base + '/transactions/get/transaction/' + transaction_id, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data['success']:
            return data['transaction']
        else:
            raise Exception(data['message'])
