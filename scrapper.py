import requests, json
from io import open as iopen
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

class Scrapper():
    def __init__(self):
        self.url = "http://localhost:5000/"

    def get_items(self):
        page = requests.get(self.url+"api/items")
        js = json.loads(page.content)["json_list"]
        return js

    def get_champs(self):
        page = requests.get(self.url + "api/champs")
        js = json.loads(page.content)["json_list"]
        return js

    def get_version(self):
        page = requests.get("https://lolchess.gg/")
        coverpage = page.content
        soup1 = BeautifulSoup(coverpage, 'html5lib')
        coverpage_item = soup1.find_all('li', class_='toggle_set')
        for i in coverpage_item:
            x = i.find('a').get_text()
            return x[:-1]

    def requests_image(self, file_url, item=None):
        if item:
            file_url = self.url +'static/items/'+file_url
        else:
            file_url = self.url + 'static/champs/' + file_url
        suffix_list = ['jpg', 'gif', 'png', 'tif', 'svg', ]
        file_name = urlsplit(file_url)[2].split('/')[-1]
        file_suffix = file_name.split('.')[1]
        i = requests.get(file_url)
        if file_suffix in suffix_list and i.status_code == requests.codes.ok:
            if item:
                with iopen('images/items/'+file_name, 'wb') as file:
                    file.write(i.content)
            else:
                with iopen('images/champs/' + file_name, 'wb') as file:
                    file.write(i.content)
        else:
            return False

