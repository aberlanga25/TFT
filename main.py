from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationLayout
from kivymd.list import OneLineAvatarListItem, ILeftBody



class MyLayout(BoxLayout):
    scr_mngr = ObjectProperty(None)
    def change_screen(self, screen, *args):
        self.scr_mngr.transition.direction = 'left'
        self.scr_mngr.current = screen
class nav_layout(NavigationLayout):
    def print_text(self):
        print('hello')

    def change_screen(self, screen, *args):
        self.ids.scr_mngr.transition.direction = 'left'
        self.ids.scr_mngr.current = screen


class MDCustomIconItem(OneLineAvatarListItem):
    icon = StringProperty('')
    text = StringProperty()

    def _set_active(self, active, list):
        pass
class AvatarSampleWidget(ILeftBody, Image):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGrey'
    theme_cls.theme_style = 'Dark'
    title = "TFT"
    main_widget = None

    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget

    def callback(self, instance, value):
        print("Pressed item menu %d" % value)

    def callbackItems(self):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = 'items'
    def callbackChamps(self):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = 'champs'
    def callbackTier(self):
        self.main_widget.ids.scr_mngr.transition.direction = 'right'
        self.main_widget.ids.scr_mngr.current = 'tier'

    def on_start(self):
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Items",
                icon='images/menu/items.png',
                on_release=lambda x: self.callbackItems()))
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Champions",
                icon='images/menu/champs.png',
                on_release=lambda x: self.callbackChamps()))
        self.main_widget.ids.nav_drawer.add_widget(
            MDCustomIconItem(
                text="Tier List",
                icon='images/menu/tier.png',
                on_release=lambda x: self.callbackTier()))


MyApp().run()