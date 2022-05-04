from turtle import dot
import dots

class PayoutLink():

    @classmethod
    def create(cls, amount, delivery, payee=None):

        json = {
            'amount': amount,
            'delivery': delivery
        }

        if payee is not None:
            json['payee'] = payee

        response = dots._session.post(dots.api_base + '/payouts/create_payout_link', json=json, auth=(dots.client_id, dots.api_key))
        response.raise_for_status()

        data = response.json()

        if data['success']:
            return data['payout_link']
        else:
            response.raise_for_status()
