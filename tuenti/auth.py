import hashlib
from requests.auth import AuthBase


class TuentiAuthentication(AuthBase):
    """
    Attaches HTTP Tuenti Authentication to the given Request object.
    """
    device_family = 'MDI3MDFmZjU4MGExNWM0YmEyYjA5MzRkODlmMjg0MTU6MC4yMjk5ODcwMCAxMzI0NDg5NjY0'

    def __init__(self, auth_data, installation_id):
        auth_data.update({
            'device-family': self.device_family,
            'installation-id': installation_id})
        self.auth_data = auth_data

    @classmethod
    def from_auth_token(cls, user, auth_token, installation_id):
        auth_data = {'user': user, 'auth-token': auth_token}
        return cls(auth_data, installation_id)

    @classmethod
    def from_credentials(cls, user, password, installation_id):
        password = hashlib.md5(password).hexdigest()
        auth_data = {'user': user, 'password': password}
        return cls(auth_data, installation_id)

    def __call__(self, r):
        auth_header = ','.join(['%s=%s' % e for e in self.auth_data.items()])
        r.headers['X-Tuenti-Authentication'] = auth_header
        return r


class TuentiAuthorization(AuthBase):
    """
    Attaches HTTP Tuenti Authorization to the given Request object.
    """
    def __init__(self, sid):
        self.sid = sid

    def __call__(self, r):
        r.headers['X-Tuenti-Authorization'] = 'sess-token=%s' % self.sid
        return r
