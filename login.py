from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from datetime import datetime, timedelta

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(orientation='vertical', spacing=10, padding=20)

        self.background = Image(source='bild.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        self.clock_label = Label(text='', font_size=30, color=(1, 1, 1, 1))  # Set text color to white
        self.add_widget(self.clock_label)

        # Update the clock label every second
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, dt):
        # Get the current time in Germany
        germany_time = datetime.utcnow() + timedelta(hours=1)
        formatted_time = germany_time.strftime('%H:%M:%S')
        self.clock_label.text = formatted_time

class MyOSApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MyOSApp().run()
