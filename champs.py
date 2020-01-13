import sqlite3
from kivymd.uix.imagelist import SmartTileWithLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from widgets import PopUpMenu, CImage

class Champs():
    def __init__(self):
        self.con = sqlite3.connect("./DataTFT")
        self.cur = self.con.cursor()

    def get_all(self):
        list_champs = []
        self.cur.execute("SELECT name, cost,img FROM champs")
        champs = self.cur.fetchall()
        for i in champs:
            smart = SmartTileWithLabel(source='images/champs/%s' % i[2], text=i[0],
                               font_style='Caption', mipmap=True, on_release=lambda z:self.popup_champ(z))
            list_champs.append(smart)
        return list_champs



    def popup_champ(self, champ):
        self.cur.execute("SELECT * FROM champs WHERE name=?", (champ.text,))
        info = self.cur.fetchall()
        popup = PopUpMenu(size_hint=(None, None), size=(dp(200), dp(300)))
        box = BoxLayout(orientation='vertical')
        info = info[0]
        o = info[2].split(",")
        n = info[3].split(",")
        lb1 = MDLabel(text=info[0], font_style='H6', theme_text_color='Primary', halign='center')
        lb2 = MDLabel(text='Cost: %s' % info[1], theme_text_color='Primary', halign='center')
        boxOrig = GridLayout(cols=2)
        boxClass = GridLayout(cols=2)
        if (len(o) > 1):
            lb3 = MDLabel(text=o[0], theme_text_color='Primary', halign='left')
            imgOrig = CImage(source='images/origins/%s.png' % o[0], )
            lb4 = MDLabel(text=o[1], theme_text_color='Primary', halign='left')
            imgOrig2 = CImage(source='images/origins/%s.png' % o[1])
            boxOrig.add_widget(imgOrig)
            boxOrig.add_widget(lb3)
            boxOrig.add_widget(imgOrig2)
            boxOrig.add_widget(lb4)
        else:
            lb3 = MDLabel(text=o[0], theme_text_color='Primary', halign='left')
            imgOrig = CImage(source='images/origins/%s.png' % o[0])
            boxOrig.add_widget(imgOrig)
            boxOrig.add_widget(lb3)
        if (len(n) > 1):
            lb5 = MDLabel(text=n[0], theme_text_color='Primary', halign='left')
            imgClass = CImage(source='images/classes/%s.png' % n[0])
            lb6 = MDLabel(text=n[1], theme_text_color='Primary', halign='left')
            imgClass2 = CImage(source='images/classes/%s.png' % n[1])
            boxClass.add_widget(imgClass)
            boxClass.add_widget(lb5)
            boxClass.add_widget(imgClass2)
            boxClass.add_widget(lb6)
        else:
            lb5 = MDLabel(text=n[0], theme_text_color='Primary', halign='left')
            imgClass = CImage(source='images/classes/%s.png' % n[0])
            boxClass.add_widget(imgClass)
            boxClass.add_widget(lb5)
        box.add_widget(lb1)
        box.add_widget(lb2)
        box.add_widget(boxOrig)
        box.add_widget(boxClass)
        popup.add_widget(box)
        popup.open()