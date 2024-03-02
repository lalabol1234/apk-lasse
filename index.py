from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button

class SwipeButton(ButtonBehavior, Label):
    def on_swipe(self, gesture):
        if gesture['dir'] == 'right':
            self.show_login_popup()

    def show_login_popup(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(TextInput(font_size='20sp', multiline=False, hint_text="Enter Code", password=True))
        content.add_widget(Button(text="Submit", font_size='20sp', on_press=self.dismiss_popup))

        popup = Popup(title='Lala-Home Login', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def dismiss_popup(self, instance):
        instance.parent.parent.dismiss()

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        swipe_button = SwipeButton(text="Swipe to Login", font_size='20sp')
        swipe_button.bind(on_swipe=swipe_button.on_swipe)

        self.add_widget(swipe_button)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
