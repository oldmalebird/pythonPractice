# -*- coding: utf-8 -*-
"""
Retrieve fao.org
"""

import requests
r = requests.get('http://www.fao.org/')
print(r.text)
print(r.status_code)
