#!/usr/bin/env python3

import requests
import os

url = "http://IP/upload"
directory = "supplier-data/images"

for filename in os.listdir(directory):
    if filename.endswith(".JPEG"):
        with open(os.path.join(),directory,filename), rb) as opened:
            r = requests.post(url, files={'file':opened})