import json
import os
import threading

import requests


class Image:
    def __init__(self, url, name, path=None):
        self.url = self.validate_(url)
        self.name = name
        self.default_path = path if path else os.getcwd()

    def validate_(self, url):
        response = self.send_request(url)
        if response.status_code == 200:
            return url
        else:
            raise ValueError("wrong url")

    @staticmethod
    def send_request(url):
        while True:
            try:
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                continue
            except Exception as err:
                raise Exception(f"something goes wrong{err}")

    def download_(self):
        response = self.send_request(self.url)
        address = f"{self.default_path}/{self.name}"
        if response.status_code == 200:
            with open(address, "wb") as file:
                file.write(response.content)
        print("downloaded")


class ImageFromJson:
    def __init__(self, json_file_path):
        self.json_file_path = self.validate_path(json_file_path)
        self.image_dict_ = self.read_from_json()
        self.image_list = self.create_image_from_dict()

    @staticmethod
    def validate_path(path):
        if not os.path.exists(path):
            raise ValueError("Wrong path")
        return path

    def read_from_json(self):
        with open(self.json_file_path) as json_file:
            data = json.load(json_file)
            return data

    def create_image_from_dict(self):
        image_list = []
        for dict_ in self.image_dict_:
            image_list.append(Image(name=dict_["img_name"], url=dict_["img_url"]))
        return image_list

    def download_1(self):
        for image in self.image_list:
            image.download_()

    def threading_from_json(self):
        thread_list = []
        for item in self.read_from_json():
        # for item in self.create_image_from_dict():

            name = item["img_name"]
            url = item["img_url"]
            x = threading.Thread(target=self.download_1(), args=(name, url))
            thread_list.append(x)
            for thread in thread_list:
                thread.start()


json_to_image = ImageFromJson(json_file_path="image_links.json")
json_to_image.threading_from_json()
# json_to_image.create_image_from_dict()
# image_1 = Image("https://files.realpython.com/media/Parse-XML-With-Python_Watermarked.078af6a3f01c.jpeg", "first.png")
# print(image_1.download_())