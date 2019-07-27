import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import  StringProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout

from kivymd.theming import ThemeManager
from kivymd.list import OneLineAvatarListItem, ILeftBody
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
class PopUpMenu(BaseDialogForDemo):
    pass
class LabelChamp(MDLabel):
    pass
class LabelPop(MDLabel):
    pass
class GridPop(GridLayout):
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
        self.set_items()

    def callbackMenu(self, y):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = y

    def tierChamp(self, y):
        names = listNames()
        nm = names[y-1]
        return SmartTileWithLabel(source='images/champs/%d.png' % y,  text=nm,
                                  font_style= 'Caption', mipmap=True, on_release=lambda z=nm: self.popChamp(y))

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
        self.main_widget.ids.champsgrid.add_widget(MDLabel(text=''))
        self.main_widget.ids.champsgrid.add_widget(MDLabel(text=''))
        self.main_widget.ids.champsgrid.add_widget(MDLabel(text=''))

    def set_allchamps(self):
        self.main_widget.ids.champsgrid.clear_widgets()
        for x in range(1,52):
            self.main_widget.ids.champsgrid.add_widget(
                self.tierChamp(x))

    def set_items(self):
        for x in range(1,9):
            self.main_widget.ids.itembase.add_widget(
                self.itemTileB(x, 1)
            )
        for y in range(9,45):
            self.main_widget.ids.itemgrid.add_widget(
                self.itemTileB(y , 0)
            )

    def itemTileB(self, y, z):
        name = itemsNames()
        nm = name[y - 1]
        if z== 1:
            return SmartTileWithLabel(source='images/items/%d.png' % y, text=nm,
                                      font_style='Caption', mipmap=True, on_release=lambda z=nm: self.popItemBase(y))
        return SmartTileWithLabel(source='images/items/%d.png' % y, text=nm,
                                  font_style='Caption', mipmap=True, on_release=lambda z=nm: self.popItemCom(y))

    def popItemBase(self, y):
        name = itemsNames()
        desc = itemsDescription()
        nm = name[y-1]
        dc = desc[y-1]
        popUp = PopUpMenu(size_hint=(None, None), size=(dp(200), dp(65)))
        box = BoxLayout(spacing=dp(10), orientation='vertical')
        lbl = MDLabel(text=nm, font_style='H6', theme_text_color='Primary', halign='center')
        lb2 = MDLabel(text=dc, theme_text_color='Primary', halign='center')
        box.add_widget(lbl)
        box.add_widget(lb2)
        popUp.add_widget(box)
        popUp.open()

    def popItemCom(self, y):
        name = itemsNames()
        desc = itemsDescription()
        madef = madeOf()
        great = greatOn()
        nm = name[y - 1]
        dc = desc[y - 1]
        popUp = PopUpMenu(size_hint=(None, None), size=(dp(200), dp(400)))
        box = BoxLayout(spacing=dp(10), orientation='vertical')
        lbl = MDLabel(text=nm, font_style='H6', theme_text_color='Primary', halign='center')
        lb2 = MDLabel(text=dc, theme_text_color='Primary', halign='center')
        made = MDLabel(text='Made of:', theme_text_color='Primary')
        boxMade = BoxLayout(orientation='horizontal')
        img1 = Image(source='images/items/%d.png' % madef[y-9][0])
        plus  = MDLabel(text="+", theme_text_color='Primary', halign='center', size_hint_x=dp(0.1))
        img2 = Image(source='images/items/%d.png' % madef[y-9][1])
        grt = MDLabel(text='Great on:', theme_text_color='Primary')
        boxgreat = GridPop(cols=3)
        if great[y-9][0] != 0:
            for champs in great[y-9]:
                chmp = Image(source='images/champs/%d.png' % champs)
                boxgreat.add_widget(chmp)
        else:
            grt = MDLabel(text='')
        boxMade.add_widget(img1)
        boxMade.add_widget(plus)
        boxMade.add_widget(img2)
        box.add_widget(lbl)
        box.add_widget(lb2)
        box.add_widget(made)
        box.add_widget(boxMade)
        box.add_widget(grt)
        box.add_widget(boxgreat)
        popUp.add_widget(box)
        popUp.open()

    def popChamp(self, y):
        name = listNames()
        cost = listCosts()
        orig = listOrigins()
        clas = listClasses()
        best = listBest()
        popUp = PopUpMenu(size_hint=(None, None), size=(dp(200), dp(300)))
        box = BoxLayout(spacing=dp(10), orientation='vertical')
        lb1 = MDLabel(text=name[y-1], font_style='H6', theme_text_color='Primary', halign='center')
        lb2 = MDLabel(text='Cost: %d' % cost[y-1], theme_text_color='Primary')
        lb3 = MDLabel(text=orig[y-1], theme_text_color='Primary', halign='center')
        lb4 = MDLabel(text=clas[y - 1], theme_text_color='Primary', halign='center')
        lb5 = MDLabel(text='Best items: ', theme_text_color='Primary')
        boxgreat = GridPop(cols=3)
        if best[y-1][0] != 0:
            for items in best[y-1]:
                itm = Image(source='images/items/%d.png' % items)
                boxgreat.add_widget(itm)
        else:
            lb5 = MDLabel(text='')
        box.add_widget(lb1)
        box.add_widget(lb2)
        box.add_widget(lb3)
        box.add_widget(lb4)
        box.add_widget(lb5)
        box.add_widget(boxgreat)
        popUp.add_widget(box)
        popUp.open()

MyApp().run()
