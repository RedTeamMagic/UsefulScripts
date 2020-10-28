#!/usr/bin/python3

import sys
import requests

requests.packages.urllib3.disable_warnings()

endpoint = '/CTCWebService/CTCWebServiceBean/ConfigServlet'

with open(sys.argv[1], 'r') as my_file:
        #print(my_file.read())

    for line in my_file:
        #print(line.rstrip())
        url = 'https://' + line.rstrip() + endpoint
        #print(url)
        r = requests.get(url, verify=False)
        #print(r.text)
        statuscode = str(r.status_code)
        if (statuscode == "200"):
            print(url + ',' + statuscode)
