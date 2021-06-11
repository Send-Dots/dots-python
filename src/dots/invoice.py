import base64
import requests

import dots
from dots import token

class Invoice():

    def __init__(self):
        pass

    def create(self, amount, expires_in, items, breakdown, requested_information):
        
        json = {
            'amount': amount,
            'expires_in': expires_in,
            'items': items,
            'breakdown': breakdown,
            'requested_information': requested_information,
        }

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = requests.post(dots.api_base + '/invoice/create', json=json, headers=headers)
        data = response.json()

        if data['success']:
            return data['invoice']
        else:
            response.raise_for_status()


    def get(self, invoice_id):
        
        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = requests.get(dots.api_base + '/invoice/get/' + invoice_id, headers=headers)
        data = response.json()

        if data['success']:
            return data['invoice']
        else:
            response.raise_for_status()
