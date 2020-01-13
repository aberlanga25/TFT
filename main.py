from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.toast.kivytoast.kivytoast import toast

from widgets import MDCustomIconItem
import items, updater, champs, news, classes



class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.theme_style = 'Dark'
        self.title = "TFT"
        self.main_widget = None
        self.icon = 'images/Logo.png'
        self.toolbar = None
        self.filterMenu = []
        self.instance_filtermenu = None
        self.tftv = "v9.24b"

        super().__init__(**kwargs)

    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget

    def on_start(self):
        update = updater.updater()
        #v= update.version
        #if v != self.tftv:
        #    toast("Updating To %s" % v)
        #    update.update_items()

        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="News",
                icon='images/menu/items.png',
                on_release=lambda x: self.callbackMenu('news')))
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Items",
                icon='images/menu/items.png',
                on_release=lambda x: self.callbackMenu('items')))
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Champions",
                icon='images/menu/champs.png',
                on_release=lambda x: self.callbackMenu('champs')))
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Tier List",
                icon='images/menu/tier.png',
                on_release=lambda x: self.callbackMenu('tier')))
        #self.set_news()
        self.set_all_champs()
        self.set_all_items()

    def callbackMenu(self, y):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = y

    def addButton(self):
        if self.main_widget.ids.scr_mngr.current == 'champs':
            self.main_widget.ids.toolbar.right_action_items = []
        else:
            self.main_widget.ids.toolbar.right_action_items = []

    def set_news(self):
        nss = news.News()
        list_news = nss.get_list_of_sm()
        for x in range(0,8):
            self.main_widget.ids.newsgrid.add_widget(
                list_news[x]
            )

    def set_all_champs(self):
        ch = champs.Champs()
        list_champs = ch.get_all()
        self.main_widget.ids.champsgrid.clear_widgets()
        for i in list_champs:
            self.main_widget.ids.champsgrid.add_widget(
                i
            )

    def set_all_items(self):
        itm = items.Items()
        list_items = itm.get_all_items()
        oper = classes.operations()
        n = oper.check_item_base(len(list_items))
        for x in range(0,n):
            self.main_widget.ids.itembase.add_widget(
                list_items[x]
            )
        for x in range(n+1,len(list_items)):
            self.main_widget.ids.itemgrid.add_widget(
                list_items[x]
            )

if __name__ == "__main__":
    MyApp().run()