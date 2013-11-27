# -*- coding: utf-8 -*-
import os
import sys
import string
import unittest
import random

from tuenti import TuentiSocialMessenger


class TestTuentiSocialMessenger(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.user = os.environ.get('TUENTIUSER') or sys.argv[0]
        password = os.environ.get('TUENTIPASSWORD') or sys.argv[1]
        self.t = TuentiSocialMessenger.from_credentials(self.user, password)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.tuenti_logout(self.t)

    def tuenti_logout(self, tuenti_inst):
        tuenti_inst.request('Auth_closeSession',
                            {'installationId': tuenti_inst.installation_id})

    def test_token_auth(self):
        auth_token, installation_id = self.t.get_auth_data()
        tuenti_token = TuentiSocialMessenger.from_auth_token(
            self.user, auth_token, installation_id)
        session_data = tuenti_token.request(
            'Auth_getSessionInfo', {'installationId': self.t.installation_id})
        self.assertTrue('userId' in session_data)
        self.tuenti_logout(tuenti_token)

    def test_create_account(self):
        t_empty = TuentiSocialMessenger()
        generate_random = lambda: ''.join(
            random.sample(string.ascii_lowercase, 8))
        params = {
            'email': '%s@chon.is' % generate_random(),
            'name': generate_random(),
            'last': generate_random(),
            'password': generate_random(),
            'installationId': t_empty.installation_id,
            'deviceFamily': 'MDI3MDFmZjU4MGExNWM0YmEyYjA5MzRkODlmMjg0MTU6'
                            'MC4yMjk5ODcwMCAxMzI0NDg5NjY0'
        }
        data = t_empty.request(
            'Registration_createNewAccountWithPassword', params)
        self.assertEqual(data['session']['newUser'], True)
        self.tuenti_logout(t_empty)

    def test_simple_request(self):
        data = self.t.request('User_getRelationshipData')
        self.assertEqual(
            data.keys(),
            [u'timestamp', u'contacts', u'weak', u'friends', u'blocked'])

if __name__ == '__main__':
    unittest.main()
