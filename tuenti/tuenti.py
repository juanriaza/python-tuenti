# -*- coding: utf-8 -*-
import json
import functools

import requests

from .auth import TuentiAuthentication
from .auth import TuentiAuthorization
from .utils import generate_random_installation_id


__all__ = ['TuentiSocialMessenger']


class TuentiSocialMessenger(object):
    """
    Tuenti Social Messenger API.
    """
    api_url = 'https://api-msngr.tuenti.com/'
    user_agent = 'Dalvik/1.6.0 (Linux; U; Android 4.4; Nexus 4 Build/KRT16S) '\
                 'Tuenti/4.0.8/92040008'

    def __init__(self, user=None, auth_token=None, password=None,
                 installation_id=None):
        if not installation_id:
            self.installation_id = generate_random_installation_id()
        else:
            self.installation_id = installation_id
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.user_agent})
        if auth_token:
            self.session.auth = TuentiAuthentication.from_auth_token(
                user, auth_token, self.installation_id)
            req_dict = {
                'method': 'AppUpdate_checkUpdate',
                'params': {'userAgent': self.user_agent, 'version': '1.2'},
                'return_request': True}
            data = self.request(**req_dict)
            sess_token = self.__parse_auth_header(data[0])['sess-token']
            self.session.auth = TuentiAuthorization(sess_token)
        elif password:
            self.session.auth = TuentiAuthentication.from_credentials(
                user, password, self.installation_id)
            req_dict = {
                'method': 'Auth_getSessionInfo',
                'params': {'installationId': self.installation_id},
                'return_request': True}
            session_data = self.request(**req_dict)
            session_req, session_content = session_data
            self.auth_data = self.__parse_auth_header(session_req)
            sess_token = self.auth_data['sess-token']
            self.session.auth = TuentiAuthorization(sess_token)

    def __getattr__(self, name):
        f = functools.partial(self.request, name)
        return f

    @classmethod
    def from_credentials(cls, user, password):
        return cls(user=user, password=password)

    @classmethod
    def from_auth_token(cls, user, auth_token, installation_id):
        return cls(user=user, auth_token=auth_token,
                   installation_id=installation_id)

    def __parse_auth_header(self, session_req):
        parse_func = requests.utils.parse_dict_header
        auth_header = session_req.headers['x-tuenti-authorization']
        tuenti_auth = parse_func(auth_header)
        return tuenti_auth

    def __build_data(self, iterable):
        data = {'requests': iterable, 'version': 'msngr-2', 'screen': 'xhdpi'}
        return json.dumps(data)

    def get_auth_data(self):
        return self.auth_data['auth-token'], self.installation_id

    def request(self, method, params=None, return_request=False,
                extra_requests=None):
        params = params or {}
        extra_requests = extra_requests or {}
        if return_request:
            request, data = self.mrequest(
                ((method, params),), return_request, extra_requests)
            return request, data[0]
        else:
            data = self.mrequest(
                ((method, params),), return_request, extra_requests)
            return data[0]

    def mrequest(self, iterable, return_request=False, extra_requests=None):
        extra_requests = extra_requests or {}
        data = self.__build_data(iterable)
        req = self.session.post(self.api_url, data=data, **extra_requests)
        if return_request:
            return req, req.json()
        else:
            return req.json()
