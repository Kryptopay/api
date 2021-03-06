#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import urllib
import json

username = 'username'
api_public_key = hashlib.sha1(username).hexdigest()
api_private_key = 'ab672eae321eb5a36064bd25bff614246118a6e4'
amount = '0.02'
order_nr = 'D32d3'
description = 'Computer'
company = 'computershop'
name = 'John'
surname = 'Tomson'
address = 'Warsaw,Soldier34/123'
url = 'https://mystore.com?invoice_id=058921123&status=ok'
url = urllib.quote_plus(url)
params = urllib.urlencode({'api_public_key': api_public_key,
                           'api_private_key': api_private_key,
                           'amount': amount,
                           'description': description,
                           'company': company,
                           'name': name,
                           'surname': surname,
                           'address': address,
                           'url': url})
json_url = "https://kryptopay.pl/api/create/?{0}".format(params)
json_data = urllib.urlopen(json_url)
json_feed = json.loads(json_data.read().decode())
transaction = json_feed['transaction']
print '<a href="https://kryptopay.pl/api/payments/?transaction={0}">redirect</a>'.format(transaction)
