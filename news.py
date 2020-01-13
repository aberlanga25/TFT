import requests
from bs4 import BeautifulSoup
from kivymd.uix.label import MDLabel
from kivymd.uix.imagelist import SmartTile

from widgets import GridNews
import webbrowser


class News():

    def __init__(self):
        self.url = "https://www.esportstales.com"
        page = requests.get(self.url+"/teamfight-tactics")
        coverpage = page.content
        soup1 = BeautifulSoup(coverpage, 'html5lib')

        coverpage_news = soup1.find_all('article', class_='BlogList-item BlogList-item--list has-categories has-tags '
                                                          'has-comments')
        self.link = []
        self.title = []
        self.img = []
        self.text = []
        for n in range(0,8):
            self.link.append(coverpage_news[n].find('a')['href'])
            self.img.append(coverpage_news[n].find('img')["data-image"])
            self.title.append(coverpage_news[n].find('h2').get_text())
            self.text.append(coverpage_news[n].find('div', class_='Blog-excerpt').get_text())

    def get_list_of_sm(self):
        list = []
        for i in range(0,8):
            link = self.link[i]
            newgrid = GridNews()
            smart = SmartTile(source=self.img[i], on_release=lambda z=i: self.open_article(link))
            label = MDLabel(text=self.title[i], font_style='H6', theme_text_color='Primary', halign='center',
                            size_hint_y=0.5)
            text = MDLabel(text=self.text[i],font_style='Body1', theme_text_color='Primary', halign='center',
                           size_hint_y=0.5)
            newgrid.add_widget(smart)
            newgrid.add_widget(label)
            newgrid.add_widget(text)
            list.append(newgrid)
        return list

    def open_article(self, link):
        new_link = self.url+link
        webbrowser.open_new(new_link)



