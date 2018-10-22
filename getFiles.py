#!/usr/bin/env python
import requests
import os
import json
import outputFormat

headers = {
"Authorization": "Bearer %s" % os.environ['LEECHBOT_TOKEN'], 
"User-Agent": "allenmiao"
}