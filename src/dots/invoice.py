import base64
import requests

import dots
from dots import token


class Invoice():

    @classmethod
    def create(cls, amount, expires_in=None, items=None, breakdown=None, requested_information=None, metadata=None):

        json = {
            'amount': amount,
        }

        if expires_in is not None:
            json['expires_in'] = expires_in

        if items is not None:
            json['items'] = items

        if breakdown is not None:
            json['breakdown'] = breakdown

        if requested_information is not None:
            json['requested_information'] = requested_information

        if metadata is not None:
            json['metadata'] = metadata

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(dots.api_base + '/invoice/create', json=json, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['invoice']
        else:
            response.raise_for_status()

    @classmethod
    def get(cls, invoice_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.get(dots.api_base + '/invoice/get/' + invoice_id, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['invoice']
        else:
            response.raise_for_status()
