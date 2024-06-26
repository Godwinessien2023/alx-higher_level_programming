#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with
the email as a parameter, and finally displays
the body of the response using requests and sys package only.
"""

import requests
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    email_ad = sys.argv[2]

    result = requests.post(url_arg, data={"email": email_ad})
    print(result.text)
