import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import  StringProperty
from kivy.uix.image import Image


from kivymd.theming import ThemeManager
from kivymd.list import OneLineAvatarListItem, ILeftBody
from kivymd.utils.cropimage import crop_image


class MDCustomIconItem(OneLineAvatarListItem):
    icon = StringProperty('')
    text = StringProperty()

    def _set_active(self, active, list):
        pass
class AvatarSampleWidget(ILeftBody, Image):
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
        for x in range(1..51):
            self.main_widget.ids.champsgrid.add_widget(
                Image(source='images/champs/%d.png' % x)
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
        self.set_champs()

MyApp().run()
