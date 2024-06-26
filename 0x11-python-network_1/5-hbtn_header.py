#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the
response header using requests and sys package.
"""

import requests
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    result = requests.get(url_arg)
    x_request_id = result.headers.get("X-Request-Id")
    print(x_request_id)
