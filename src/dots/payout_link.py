import dots
from dots import token


class PayoutLink():

    @classmethod
    def create(cls, amount, delivery, payee):

        json = {
            'amount': amount,
            'delivery': delivery
        }

        if payee is not None:
            json['payee'] = payee

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = dots._session.post(dots.api_base + '/payouts/create_payout_link', json=json, headers=headers)

        data = response.json()

        if data['success']:
            return data['payout_link']
        else:
            response.raise_for_status()
