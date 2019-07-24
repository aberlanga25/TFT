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
from kivymd.imagelists import SmartTile

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

class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'
    theme_cls.theme_style = 'Dark'
    title = "TFT"
    main_widget = None
    icon = 'images/Logo.png'

    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget

    def callback(self, instance, value):
        print("Pressed item menu %d" % value)

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
        champLay = GridLayout(rows=2,)
        champLay.add_widget(MySmartTile(source='images/champs/%d.png' % x, size_hint_y=None))
        champLay.add_widget(
            MDLabel(text=str(names[x - 1]), size_hint_y=None, font_style="Subtitle2", theme_text_color='Primary',
                    halign='center', valign='top', size=(dp(10),dp(10))))
        return champLay
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


    def set_champs(self):
        costs = listCosts()
        orig = listOrigins()
        names = listNames()
        clas = listClasses()
        for x in range(1,52):
            champLay = GridLayout(cols=2)
            champLay.add_widget(MySmartTile(source='images/champs/%d.png' %x,  size_hint_y=None))
            champLay.add_widget(MDLabel(text=str(names[x-1]), size_hint_y=None, font_style="Subtitle2", theme_text_color='Primary', halign='center'))
            self.main_widget.ids.champsgrid.add_widget(champLay)
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(costs[x-1]), size_hint_y=None, font_style="Subtitle2",halign='center', theme_text_color='Primary'))
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(orig[x-1]), size_hint_y=None,  font_style="Subtitle2", halign='center', theme_text_color='Primary'))
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(clas[x-1]), size_hint_y=None, font_style="Subtitle2", halign='center', theme_text_color='Primary'))

    def createSmart(self):
        smart = MDLabel(text="hi", font_style="H6")
        return smart

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
        self.set_champs()
        self.set_tiers()

MyApp().run()
