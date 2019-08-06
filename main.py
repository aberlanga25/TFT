
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
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
class GridPop(GridLayout):
    pass
class MyImage(Image):
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
    filter_list = ["All", "Assassin", "Blademaster", "Brawler", "Demon", "Dragon", "Elementalist", "Exile", "Glacial",
        "Guardian", "Gunslinger", "Imperial", "Knight", "Noble", "Ninja", "Phantom", "Pirate", "Ranger", "Robot",
        "Shapeshifter", "Sorcerer", "Wild", "Void", "Yordle"]

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
                                  font_style='Caption', mipmap=True, on_release=lambda z=nm: self.popChamp(y))

    def set_tiers(self):
        for x in tier1():
            self.main_widget.ids.tier1.add_widget(self.tierChamp(x))
        for y in tier2():
            self.main_widget.ids.tier2.add_widget(self.tierChamp(y))
        for z in tier3():
            self.main_widget.ids.tier3.add_widget(self.tierChamp(z))
        for w in tier4():
            self.main_widget.ids.tier4.add_widget(self.tierChamp(w))
        for v in tier5():
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
                        "viewclass": "MDCustomIconItem",
                        "text": name_item,
                        "icon": 'images/classes/%s.png' % name_item,
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
        boxMade = GridPop(cols=3,padding=dp(10))
        img1 = MySmartTile(source='images/items/%d.png' % madef[y-9][0])
        plus  = MDLabel(text="+", theme_text_color='Primary', halign='center')
        img2 = MySmartTile(source='images/items/%d.png' % madef[y-9][1])
        grt = MDLabel(text='Great on:', theme_text_color='Primary')
        boxMade.add_widget(img1)
        boxMade.add_widget(plus)
        boxMade.add_widget(img2)
        box.add_widget(lbl)
        box.add_widget(lb2)
        box.add_widget(made)
        box.add_widget(boxMade)
        boxgreat = GridPop(cols=3, spacing=dp(10), padding=dp(10))
        if great[y-9][0] != 0:
            for champs in great[y-9]:
                chmp = MySmartTile(source='images/champs/%d.png' % champs)
                boxgreat.add_widget(chmp)
            box.add_widget(grt)
        else:
            popUp.size = (dp(200), dp(300))
        if y==28 or y==26 or y==22 or y==15:
            popUp.size = (dp(200), dp(500))
        if y==41:
            boxgreat.add_widget(MDLabel(text=''))
        box.add_widget(boxgreat)
        popUp.add_widget(box)
        popUp.open()

    def popMadeOf(self, y):
        names = listNames()
        nm = names[y-1]
        return MySmartTile(source='images/items/%d.png' % y, mipmap=True, on_release=lambda z=nm: self.popItemCom(y))


    def popChamp(self, y):
        name = listNames()
        cost = listCosts()
        orig = listOrigins()
        clas = listClasses()
        best = listBest()
        n = clas[y - 1].split()
        o = orig[y - 1].split()
        popUp = PopUpMenu(size_hint=(None, None), size=(dp(200), dp(300)))
        box = BoxLayout(orientation='vertical')
        lb1 = MDLabel(text=name[y-1], font_style='H6', theme_text_color='Primary', halign='center')
        lb2 = MDLabel(text='Cost: %d' % cost[y-1], theme_text_color='Primary')
        boxOrig = GridLayout(cols=2)
        if (len(o) > 1):
            lb3 = MDLabel(text=o[0], theme_text_color='Primary', halign='left')
            imgOrig = MyImage(source='images/classes/%s.png' % o[0], )
            lb4 = MDLabel(text=o[1], theme_text_color='Primary', halign='left')
            imgOrig2 = MyImage(source='images/classes/%s.png' % o[1])
            boxOrig.add_widget(imgOrig)
            boxOrig.add_widget(lb3)
            boxOrig.add_widget(imgOrig2)
            boxOrig.add_widget(lb4)
        else:
            lb3 = MDLabel(text=o[0], theme_text_color='Primary', halign='left')
            imgOrig = MyImage(source='images/classes/%s.png' % o[0])
            boxOrig.add_widget(imgOrig)
            boxOrig.add_widget(lb3)
        boxClass = GridLayout(cols=2)
        if(len(n)>1):
            lb5 = MDLabel(text=n[0], theme_text_color='Primary', halign='left')
            imgClass = MyImage(source='images/classes/%s.png' % n[0])
            lb6 = MDLabel(text=n[1], theme_text_color='Primary', halign='left')
            imgClass2 = MyImage(source='images/classes/%s.png' % n[1])
            boxClass.add_widget(imgClass)
            boxClass.add_widget(lb5)
            boxClass.add_widget(imgClass2)
            boxClass.add_widget(lb6)
        else:
            lb5 = MDLabel(text=n[0], theme_text_color='Primary', halign='left')
            imgClass = MyImage(source='images/classes/%s.png' % n[0])
            boxClass.add_widget(imgClass)
            boxClass.add_widget(lb5)
        lb7 = MDLabel(text='Best items: ', theme_text_color='Primary')
        boxgreat = GridPop(cols=3, spacing=dp(10), padding=dp(10))
        if best[y-1][0] != 0:
            if len(best[y-1])<2:
                boxgreat.add_widget(MDLabel(text=''))
            for items in best[y-1]:
                itm = self.popMadeOf(items)
                boxgreat.add_widget(itm)
            if len(best[y-1])<3:
                boxgreat.add_widget(MDLabel(text=''))
        else:
            lb7 = MDLabel(text='')
        box.add_widget(lb1)
        box.add_widget(lb2)
        box.add_widget(boxOrig)
        box.add_widget(boxClass)
        box.add_widget(lb7)
        box.add_widget(boxgreat)
        popUp.add_widget(box)
        popUp.open()


MyApp().run()
