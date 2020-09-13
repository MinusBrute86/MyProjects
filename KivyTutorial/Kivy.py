import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)  # Inheritable Properties
        self.cols = 1  # Main grid layout

        self.inside = GridLayout()      # Gridception / using .inside parameter
        self.inside.cols = 2            # ^^^

        # First Name Widget
        self.inside.add_widget(Label(text="First Name: "))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        # Middle Initial Widget
        self.inside.add_widget(Label(text="Middle Name: "))
        self.middlename = TextInput(multiline=False)
        self.inside.add_widget(self.middlename)

        # Last Name Widget
        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        # Email Widget
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        # Button
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)  # Calls pressed() function
        self.add_widget(self.submit)

    # When Button is Pressed
    def pressed(self, instance):
        first = self.firstname.text
        middle = self.middlename.text
        last = self.lastname.text
        mail = self.email.text

        print("First Name:", first)
        print("Middle Name:", middle)
        print("Last Name:", last)
        print("Email:", mail + "\n")


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()