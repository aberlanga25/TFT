import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import  StringProperty
from kivy.uix.image import Image

from kivymd.theming import ThemeManager
from kivymd.list import OneLineAvatarListItem, ILeftBody
from kivymd.utils.cropimage import crop_image
from kivymd.label import MDLabel
from kivymd.imagelists import SmartTile

from champs import (listCosts, listOrigins, listNames)
from demo_apps.basedialog import BaseDialogForDemo

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


    def set_champs(self):
        costs = listCosts()
        orig = listOrigins()
        names = listNames()

        for x in range(1,52):
            self.main_widget.ids.champsgrid.add_widget(
                MySmartTile(source='images/champs/%d.png' %x,  size_hint_y=None, size_hint_x=0.3)
            )
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(names[x-1]), size_hint_y=None, font_style="Subtitle2", theme_text_color='Primary'))
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(costs[x-1]), size_hint_y=None, font_style="Subtitle2",halign='center', theme_text_color='Primary'))
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text=str(orig[x-1]), size_hint_y=None,  font_style="Subtitle2", theme_text_color='Primary'))
            self.main_widget.ids.champsgrid.add_widget(
                MDLabel(text="%d" % x, size_hint_y=None, font_style="Subtitle2", theme_text_color='Primary'))

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
        #self.set_items()

MyApp().run()
