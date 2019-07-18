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

    def check_data_login(self):
        username = self.scr_mngr.screen1.username.text
        password = self.scr_mngr.screen1.password.text

        print(username)
        print(password)
        if username == "KivyMD" and password == "kivy":
            self.ids["wrongpass"].text = ""
            self.change_screen("screen2")
        else:
            self.ids["wrongpass"].text = \
                "Wrong username or password, please try again"

    def change_screen(self, screen, *args):
        self.scr_mngr.transition.direction = 'left'
        self.scr_mngr.current = screen

    def back_to_chat(self):
        self.scr_mngr.transition.direction = 'right'
        self.scr_mngr.current = 'screen2'


class nav_layout(NavigationLayout):
    def print_text(self):
        print('hello')

    def check_data_login(self):
        username = self.ids.screen1.username.text
        password = self.ids.screen1.password.text

        print(username)
        print(password)
        if username == "KivyMD" and password == "kivy":
            self.change_screen("screen2")
            self.ids.wrongpass.text = ""
        else:
            self.ids.wrongpass.text = \
                "Wrong username or password, please try again"

    def change_screen(self, screen, *args):
        self.ids.scr_mngr.transition.direction = 'left'
        self.ids.scr_mngr.current = screen

    def back_to_chat(self):
        self.ids.scr_mngr.transition.direction = 'right'
        self.ids.scr_mngr.current = 'screen2'

    def logout(self):
        # logout function, returns to screen 1
        self.ids.scr_mngr.current = 'screen1'


KV = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSeparator kivymd.card.MDSeparator
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import CardTransition kivy.uix.screenmanager.CardTransition


<MDCustomIconItem>:
    text: root.text

    AvatarSampleWidget:
        source: root.icon


nav_layout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        drawer_logo: 'logo.png'
        NavigationDrawerToolbar:
            title: 'hello'
        NavigationDrawerIconButton:
            icon: 'settings'
            text: 'Account Settings'
            on_release: root.change_screen('screen3')
        NavigationDrawerIconButton:
            icon: 'face'
            text: 'Friends'
            on_release: root.print_text()
        NavigationDrawerIconButton:
            icon: 'logout'
            text: 'Logout'
            on_release: root.logout()
        NavigationDrawerDivider:
            height: dp(1)
    MyLayout:
        scr_mngr: scr_mngr
        orientation: 'vertical'


        ScreenManager:

            transition: CardTransition()
            id: scr_mngr
            screen1: screen2

            Screen:
                name: 'screen2'
                id: screen2

                Toolbar:
                    id: toolbar
                    title: "Welcome ! "
                    pos_hint: {'center_x': 0.5, 'center_y': 0.96}
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'DeepPurple'
                    background_hue: 'A400'
                    left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer() ]]
                    right_action_items: [['animation', lambda x: MDThemePicker().open()], ['camera', lambda x: print('hello')]]

                MDLabel:
                    font_style: 'Title'
                    theme_text_color: 'Primary'
                    text: "Data :"
                    height: self.texture_size[1] + dp(3)
                    halign: 'center'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}



            Screen:
                name: 'screen3'
                id: 'screen3'

                Toolbar:
                    id: tools
                    title: "Your Profile"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.96}
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'DeepPurple'
                    background_hue: 'A400'
                    left_action_items: [['arrow-left', lambda x: root.back_to_chat()]]
                MDLabel:
                    id: 'Profile_String'
                    font_size: 90
                    text: "Brian Zheng"
                    halign: 'center'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.85}
"""


class MDCustomIconItem(OneLineAvatarListItem):
    icon = StringProperty('')
    text = StringProperty()

    def _set_active(self, active, list):
        pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Navigation Drawer"
    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(KV)
        return self.main_widget

    def callback(self, instance, value):
        print("Pressed item menu %d" % value)

    def on_start(self):
        for i in range(15):
            self.main_widget.ids.nav_drawer.add_widget(
                MDCustomIconItem(
                    text="Item menu %d" % i,
                    icon='data/logo/kivy-icon-128.png',
                    on_release=lambda x, y=i: self.callback(x, y)))


MyApp().run()


ScrollView:
                    do_scroll_x: True
                    do_scroll_y: True
                    BoxLayout:
                        orientation: 'vertical'

                        Toolbar:
                            id: tools
                            title: "Items"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
                            md_bg_color: app.theme_cls.primary_color
                            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer() ]]
                        MDLabel:
                            text: "Base"
                            font_style: 'Title'
                            theme_text_color: 'Primary'
                            pos_hint: {'x': 0.05, 'center_y': 0.75}

                        GridLayout:
                            cols:4
                            row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
                            row_force_default: True
                            size_hint_y: None
                            height: self.minimum_height
                            padding: dp(20)
                            spacing: dp(20)
                            SmartTile:
                                mipmap: True
                                source: 'images/items/1.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/2.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/3.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/4.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/5.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/6.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/7.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/8.png'
                                box_color: 0,0,0,0

                        MDLabel:
                            text: "Combined"
                            font_style: 'Title'
                            theme_text_color: 'Primary'
                            pos_hint: {'x': 0.05, 'center_y': 0.75}

                        GridLayout:
                            cols:4
                            row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
                            row_force_default: True
                            size_hint_y: None
                            height: self.minimum_height
                            padding: dp(20)
                            spacing: dp(20)
                            SmartTile:
                                mipmap: True
                                source: 'images/items/11.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/12.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/13.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/14.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/15.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/16.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/17.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/18.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/22.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/23.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/24.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/25.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/26.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/27.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/28.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/33.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/34.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/35.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/36.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/37.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/38.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/44.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/45.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/46.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/47.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/48.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/55.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/56.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/57.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/58.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/66.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/67.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/68.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/77.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/78.png'
                                box_color: 0,0,0,0
                            SmartTile:
                                mipmap: True
                                source: 'images/items/88.png'
                                box_color: 0,0,0,0