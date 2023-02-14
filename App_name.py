import os
import sys

from kivy.app import App
from kivy.core.window import Window


class AppObj(App):
    """=== Class name: AppObj ========================================================================================
    Child of built in class: App
    This is the Parent application for a project.
    Instantiation should - contrary to what is used on the net - happen by assigning it to a variable name.
    :param window_content:
    ============================================================================================== by Sziller ==="""
    def __init__(self,
                 window_content: str,
                 app_title: str = "Sziller's App",
                 csm: float = 1.0):
        super(AppObj, self).__init__()
        self.title                      = app_title
        self.window_content             = window_content
        self.content_size_multiplier    = csm
        self.external_var: list         = []

    def change_screen(self, screen_name, screen_direction="left"):
        """=== Method name: change_screen ==============================================================================
        Use this screenchanger instead of the built-in method for more customizability and to enable further
        actions before changing the screen.
        Also, if screenchanging first needs to be validated, use this method!
        ========================================================================================== by Sziller ==="""
        smng = self.root  # 'root' refers to the only one root instance in your App. Here it is the actual ROOT
        smng.current = screen_name
        smng.transition.direction = screen_direction

    def build(self):
        return self.window_content


if __name__ == "__main__":
    from kivy.lang import Builder  # to freely pick kivy files

    display_settings = {0: {'fullscreen': False, 'run': Window.maximize},
                        1: {'fullscreen': False, 'size': (400, 800)},
                        2: {'fullscreen': False, 'size': (600, 400)},
                        3: {'fullscreen': False, 'size': (1000, 500)}}

    style_code = 1

    Window.fullscreen = display_settings[style_code]['fullscreen']
    if 'size' in display_settings[style_code].keys(): Window.size = display_settings[style_code]['size']
    if 'run' in display_settings[style_code].keys(): display_settings[style_code]['run']()

    try:
        content = Builder.load_file(str(sys.argv[1]))
    except IndexError:
        content = Builder.load_file("app_name.kv")

    application_title_in_window_head    = "MyDefaultApp"
    content_size_multiplier             = 1

    application = AppObj(window_content=content,
                         app_title=application_title_in_window_head,
                         csm=content_size_multiplier)

    data_from_app = application.external_var
    application.run()
