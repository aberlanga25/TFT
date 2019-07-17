
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.image import Image


from kivymd.list import BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.theming import ThemeManager
from kivymd.list import ILeftBody

# User defined imports
from kivy.core.window import Window

# Window.fullscreen = "auto"


class MainApp(App):
    theme_cls = ThemeManager()
    title = "TFT"
    main_widget = None

    def build(self):
        self.main_widget = Builder.load_file(
            os.path.join(os.path.dirname(__file__), "./main.kv")
        )
        self.theme_cls.theme_style = 'Dark'

#        self.main_widget.ids.text_field_error.bind(
#            on_text_validate=self.set_error_message,
#            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(self.main_widget)
        return self.main_widget



    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_1)

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass


if __name__ == '__main__':
    MainApp().run()