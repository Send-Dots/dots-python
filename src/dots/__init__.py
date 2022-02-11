import requests

api_key = None
client_id = None
api_base = 'https://pls.senddots.com/api'

_session = requests.Session()

from dots.invoice import Invoice
from dots.transaction import Transaction
from dots.user import User
from dots.payout_link import PayoutLink