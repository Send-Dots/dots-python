import base64

import dots

def get_auth_token():
    
    if dots.client_id == None or dots.api_key == None:
        raise AssertionError('api_key and/or client_id not set')

    token = base64.b64encode(bytes(dots.client_id + ':' + dots.api_key, 'utf-8')).decode('utf-8')
    return token
