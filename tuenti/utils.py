# -*- coding: utf-8 -*-
import os
import binascii


def generate_random_installation_id():
    return binascii.b2a_hex(os.urandom(8))
