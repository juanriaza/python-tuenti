# python-tuenti

[![Build Status](https://travis-ci.org/juanriaza/python-tuenti.png?branch=master)](https://travis-ci.org/juanriaza/python-tuenti)
[![Pypi Package](https://badge.fury.io/py/python-tuenti.png)](http://badge.fury.io/py/python-tuenti)
[![Downloads](https://pypip.in/d/python-tuenti/badge.png)](https://crate.io/packages/python-tuenti/)

## Overview

Wrapper around the latest Tuenti API.

## Installation

Install using `pip`, including any optional packages you want...

	$ pip install python-tuenti

...or clone the project from github.

    $ git clone git@juanriaza/python-tuenti.git
    $ cd python-tuenti
    $ pip install -r requirements.txt

## How to use it?

With your credentials:

```python
from tuenti import TuentiSocialMessenger

user = 'yosoycani@hotmail.com'
password = 'olakase'

t = TuentiSocialMessenger.from_credentials(user, password)
```

…or you can retrieve some auth data and save it for later…

```python
auth_token, installation_id = t.get_auth_data()
```

…to use the API without your credentials:

```python
t = TuentiSocialMessenger.from_auth_token(user, auth_token, installation_id)
```

And fire some requests:

```python
# single request
data = t.request('Feed_getShareFeed', {'max': 20})

# with a shortcut
data = t.Feed_getShareFeed({'max': 20})

# multiple request
data = t.mrequest(('User_getRelationshipData'), ('Feed_getShareFeed', {'max': 20}), ...)
```

All the available requests are documented [here](https://github.com/juanriaza/python-tuenti/blob/master/API.md).

## Running the tests

    $ ./test_tuenti.py

## Changelog

### 1.1.0

**27th Nov 2013**

* Shortcut for fire a request.
* Registration test fixed.

### 1.0.0

**9th Jan 2012**

* First release.
