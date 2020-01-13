import scrapper
import sqlite3
from os import path

class updater():
    def __init__(self):
        self.scrapper = scrapper.Scrapper()
        self.version = self.scrapper.get_version()
        self.con = sqlite3.connect("./DataTFT")
        self.cur = self.con.cursor()

    def search(self, name, table):
        sql = "SELECT count(*) FROM %s WHERE name = ?" %table
        self.cur.execute(sql, (name,))
        data = self.cur.fetchone()[0]
        if data==0:
            return False
        return True

    def update_items(self):
        updated = self.scrapper.get_items()
        sql_update = "UPDATE items SET descript=?, img=?, made=?, name=? WHERE id=?"
        sql_insert = "INSERT INTO items(name,descript,img,made) VALUES (?,?,?,?)"
        for i in updated:
            if self.search(i['name'], "items"):
                self.cur.execute(sql_update,(i['desc'],i['img'],i['made'],i['name'],i['id']))
                self.con.commit()
            else:
                self.cur.execute(sql_insert,(i['name'],i['desc'],i['img'],i['made']))
            if not path.exists('images/items/%s' %i['img']):
                self.scrapper.requests_image(i['img'],item=1)

    def update_champs(self):
        updated = self.scrapper.get_champs()
        sql_update = "UPDATE champs SET class=?,cost=? ,img=?, item1=?,item2=?,item3=?, name=?, origin=?, tier=? WHERE id=?"
        sql_insert = "INSERT INTO champs(class,cost,img, item1,item2,item3, name, origin, tier) VALUES (?,?,?,?,?,?,?,?,?)"
        for i in updated:
            if self.search(i['name'], "champs"):
                self.cur.execute(sql_update, (i['clase'], i['cost'],i['img'], i['item1'],i['item2'],i['item3'],
                                              i['name'], i['origin'],i['tier'],i['id']))
                self.con.commit()
            else:
                self.cur.execute(sql_insert, (i['clase'], i['cost'],i['img'], i['item1'],i['item2'],i['item3'],
                                              i['name'], i['origin'],i['tier']))
            if not path.exists('images/champs/%s' % i['img']):
                self.scrapper.requests_image(i['img'])


