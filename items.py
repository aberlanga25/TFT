import sqlite3
from kivymd.uix.imagelist import SmartTileWithLabel

class Items():
    def __init__(self):
        self.con = sqlite3.connect("./DataTFT")
        self.cur = self.con.cursor()

    def get_all_items(self):
        list_items = []
        self.cur.execute("SELECT name, descript,img FROM items")
        items = self.cur.fetchall()
        for i in items:
            smart = SmartTileWithLabel(source='images/items/%s' % i[2], text=i[0],
                                       font_style='Caption', mipmap=True)
            list_items.append(smart)
        return list_items