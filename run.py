#!/usr/bin/env python3

import os
import requests
import json
import locale

directory = 'supplier-data/descriptions/'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r') as f:
            tempList = []
            tempList = f.read().split('\n')
            weight = locale.atoi(tempList[1].strip("lbs"))
            img_name = filename.strip(".txt")+".jpeg"
            dict = {
                'name':tempList[0],
                'weight': weight,
                'description':tempList[2],
                'image_name':img_name
            }

            headers = {'content-type':'application/json'}
            response = requests.post("http://IP/fruits/", data=json.dumps(dict), headers=headers, verify=False)
            if not response.ok:
                raise Exception("POST failed with status code {}".format(response.status_code))