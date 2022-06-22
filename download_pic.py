import json
from typing import Tuple

import requests
import threading


class Picture:

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def validation_url(self):
        try:
            requests.get(self.url)
        except Exception as err:
            print(f"something goes wrong {err}")

    def open_json(self):
        dict_ = {
            "name": self.name,
            "url": self.url
        }
        with open("new.json", "a") as photo:
            json.dump(dict_, photo)

    def read_json(self):

        with open("new.json") as json_file:
            data = json.load(json_file)
            return data


    def download_(self):
        with open(f"{self.name}.png", "wb") as img:
            if (requests.get(self.url)).status_code == 200:
                img.write((requests.get(self.url)).content)


photo_1 = Picture("first",
                  "https://play-lh.googleusercontent.com/CWzqShf8hi-AhV9dUjzsqk2URzdIv8Vk2LmxBzf-Hc8T-oGkLVXe6pMpcXv36ofpvtc")
# print(photo_1.download_())
# print(photo_1.open_json(), sep="\n")
print(photo_1.read_json())
