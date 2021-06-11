import base64

import dots

def get_auth_token():
    token = base64.b64encode(bytes(dots.client_id + ':' + dots.api_key, 'utf-8')).decode('utf-8')
