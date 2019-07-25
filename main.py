import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import  StringProperty
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

from kivymd.theming import ThemeManager
from kivymd.list import OneLineAvatarListItem, ILeftBody
from kivymd.utils.cropimage import crop_image
from kivymd.label import MDLabel
from kivymd.imagelists import SmartTile, SmartTileWithLabel
from kivymd.menus import MDDropdownMenu

from champs import *
from basedialog import BaseDialogForDemo

class MDCustomIconItem(OneLineAvatarListItem):
    icon = StringProperty('')
    text = StringProperty()
    def _set_active(self, active, list):
        pass
class AvatarSampleWidget(ILeftBody, Image):
    pass
class MySmartTile(SmartTile):
    pass
class PreviousDialogCoffee(BaseDialogForDemo):
    pass
class LabelChamp(MDLabel):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'
    theme_cls.theme_style = 'Dark'
    title = "TFT"
    main_widget = None
    icon = 'images/Logo.png'
    toolbar = None
    filterMenu = []
    instance_filtermenu = None
    filter_list = [
        "All",
        "Assassin",
        "Blademaster",
        "Brawler",
        "Demon",
        "Dragon",
        "Elementalist",
        "Exile",
        "Glacial",
        "Guardian",
        "Gunslinger",
        "Imperial",
        "Knight",
        "Noble",
        "Ninja",
        "Phantom",
        "Pirate",
        "Ranger",
        "Robot",
        "Shapeshifter",
        "Sorcerer",
        "Wild",
        "Void",
        "Yordle",
    ]

    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget

    def callbackMenu(self, y):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = y

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

    def tierChamp(self, x):
        names = listNames()
        return SmartTileWithLabel(source='images/champs/%d.png' % x,  text=str(names[x-1]),
                                  font_style= 'Subtitle1', mipmap=True)
    def set_tiers(self):
        t1 = tier1()
        t2 = tier2()
        t3 = tier3()
        t4 = tier4()
        t5 = tier5()

        for x in t1:
            self.main_widget.ids.tier1.add_widget(self.tierChamp(x))
        for y in t2:
            self.main_widget.ids.tier2.add_widget(self.tierChamp(y))
        for z in t3:
            self.main_widget.ids.tier3.add_widget(self.tierChamp(z))
        for w in t4:
            self.main_widget.ids.tier4.add_widget(self.tierChamp(w))
        for v in t5:
            self.main_widget.ids.tier5.add_widget(self.tierChamp(v))

    def openFilter(self, instance):
        self.set_Filtermenu()
        self.instance_filtermenu = MDDropdownMenu(items=self.filterMenu, max_height=dp(500), width_mult=4)
        self.instance_filtermenu.open(instance)

    def addButton(self):

        if self.main_widget.ids.scr_mngr.current == 'champs':
            self.main_widget.ids.toolbar.right_action_items.append(
                ['filter', lambda x: self.openFilter(x)]
            )
        else:
            self.main_widget.ids.toolbar.right_action_items = []
    def set_Filtermenu(self):
        if not len(self.filterMenu):
            for name_item in self.filter_list:
                self.filterMenu.append(
                    {
                        "viewclass": "OneLineIconListItem",
                        "text": name_item,
                        "icon": 'images/classes/1.png',
                        "on_release": lambda x=name_item: self.filterEvent(x),
                    }
                )

    def filterEvent(self, name_item):
        if name_item == 'All':
            self.set_allchamps()
        else:
            self.set_fitlerchamps(name_item)

    def set_fitlerchamps(self, name):
        self.main_widget.ids.champsgrid.clear_widgets()
        clas = listClasses()
        orig = listOrigins()
        for x in range(1,52):
            n = clas[x-1].split()
            o = orig[x-1].split()
            if(len(n)>1):
                if n[0] == name or n[1] == name:
                    self.main_widget.ids.champsgrid.add_widget(
                        self.tierChamp(x))
            elif n[0] == name:
                self.main_widget.ids.champsgrid.add_widget(
                    self.tierChamp(x))
            if(len(o)>1):
                if o[0] == name or o[1] == name:
                    self.main_widget.ids.champsgrid.add_widget(
                        self.tierChamp(x))
            elif o[0] == name:
                self.main_widget.ids.champsgrid.add_widget(
                    self.tierChamp(x))
    def set_allchamps(self):
        self.main_widget.ids.champsgrid.clear_widgets()
        for x in range(1,52):
            self.main_widget.ids.champsgrid.add_widget(
                self.tierChamp(x)
            )

    def on_start(self):
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
        self.set_allchamps()
        self.set_tiers()

MyApp().run()
