from pylgtv import WebOsClient

import sys
import logging
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient('192.168.0.102')
    webos_client.launch_app_with_content_id('youtube.leanback.v4','https://www.youtube.com/watch?v=NM22Xh0SD6g')
    webos_client.set_volume(15)

    for app in webos_client.get_apps():
        print(app)
except:
    print("Error connecting to TV")